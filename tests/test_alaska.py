import pytest

from api.api import API
from config.config import DevelopmentConfig

api = API(DevelopmentConfig)


@pytest.fixture()
def clear_db():
    api.delete_all_bears()


@pytest.fixture()
def fill_db():
    data = [{'bear_type': 'POLAR', 'bear_name': 'FOO', 'bear_age': 20.0}]
    result_data = []
    for entry in data:
        response = api.add_bear(entry)
        entry_copy = entry.copy()
        entry_copy['bear_id'] = int(response.content)
        result_data.append(entry_copy)
    return result_data


@pytest.mark.parametrize("bear_type,bear_name,bear_age,expected_status_code", [
    ('POLAR', 'mikhail', 10, 200),
    ('GUMMY', 'foo', 0, 200)
])
def test_create_bear(bear_type, bear_name, bear_age, expected_status_code):
    data = {
        'bear_type': bear_type,
        'bear_name': bear_name,
        'bear_age': bear_age
    }
    response = api.add_bear(data)

    assert response.status_code == expected_status_code, \
        f"Expected status {expected_status_code}. Actual status {response.status_code}. Response text {response.text}"
    # created entry can also be verified field by field


@pytest.mark.parametrize("data,expected_status_code", [
    ({'bear_name': 'foo','bear_age': 10}, 400),
    ({'bear_type': 'POLAR','bear_age': 10}, 400)
])
def test_create_bear_with_missing_fields(data, expected_status_code):
    response = api.add_bear(data)

    assert response.status_code == expected_status_code, \
        f"Expected status {expected_status_code}. Actual status {response.status_code}. Response text {response.text}"


def test_read_all_bears_from_empty_db(clear_db):
    response = api.read_all_bears()

    assert response.status_code == 200, \
        f"Expected status 200. Actual status {response.status_code}. Response text {response.text}"
    assert response.json() == [], \
        f"Expected payload []. Actual payload {response.json()}"


def test_read_all_bears_from_filled_db(clear_db, fill_db):
    response = api.read_all_bears()

    assert response.status_code == 200,\
        f"Expected status 200. Actual status {response.status_code}. Response text {response.text}"
    assert response.json() == fill_db, \
        f"Expected payload {fill_db}. Actual payload {response.json()}"


def test_read_bear_by_id(clear_db, fill_db):
    existing_bear = fill_db[0]
    response = api.read_bear(existing_bear['bear_id'])

    assert response.status_code == 200,\
        f"Expected status 200. Actual status {response.status_code}. Response text {response.text}"
    assert response.json() == existing_bear,\
        f"Expected payload {existing_bear}. Actual payload {response.json()}"


def test_delete_all_bears_when_db_empty(clear_db):
    response = api.delete_all_bears()
    assert response.status_code == 200, \
        f"Expected status 200. Actual status {response.status_code}. Response text {response.text}"
