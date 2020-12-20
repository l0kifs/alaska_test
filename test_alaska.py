import json

import pytest
import requests

API_URL = 'http://127.0.0.1:8091'


@pytest.fixture()
def clear_db():
    requests.request('DELETE', f'{API_URL}/bear')


@pytest.fixture()
def fill_db():
    data = [{'bear_type': 'POLAR', 'bear_name': 'FOO', 'bear_age': 20.0}]
    result_data = []
    for entry in data:
        response = requests.request('POST', f'{API_URL}/bear', data=json.dumps(entry))
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
    response = requests.request('POST', f'{API_URL}/bear', data=json.dumps(data))

    assert response.status_code == expected_status_code
    # created entry can also be verified field by field


@pytest.mark.parametrize("data,expected_status_code", [
    ({'bear_name': 'foo','bear_age': 10}, 400),
    ({'bear_type': 'POLAR','bear_age': 10}, 400)
])
def test_create_bear_with_missing_fields(data, expected_status_code):
    response = requests.request('POST', f'{API_URL}/bear', data=json.dumps(data))

    assert response.status_code == expected_status_code


def test_read_all_bears_from_empty_db(clear_db):
    response = requests.request('GET', f'{API_URL}/bear')

    assert response.status_code == 200
    assert response.json() == []


def test_read_all_bears_from_filled_db(clear_db, fill_db):
    response = requests.request('GET', f'{API_URL}/bear')

    assert response.status_code == 200
    assert response.json() == fill_db


def test_get_bear_by_id(clear_db, fill_db):
    response = requests.request('GET', f'{API_URL}/bear/{id}')

    assert response.status_code == 200
    assert response.json() == []


def test_delete_all_bears_when_db_empty(clear_db):
    response = requests.request('DELETE', f'{API_URL}/bear')
    assert response.status_code == 200
