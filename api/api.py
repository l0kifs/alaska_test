import json
from typing import Type

import requests
from requests import Response

from config.config import Config


class API(object):
    def __init__(self, config: Type[Config]):
        self._config = config
    
    def add_bear(self, data: dict) -> Response:
        response = requests.request('POST', f'{self._config.API_URL}/bear', data=json.dumps(data))
        return response

    # Here we are using dataclass model as input (also dataclass can be used as output).
    # It's useful for structuration of payload data.
    # This structure is inconvenient in current case because of the "missing field" scenarios.
    # But it can still be implemented for more complex framework.
    # def add_bear(self, data: Bear) -> Response:
    #     response = requests.request('POST', f'{self._config.API_URL}/bear', data=json.dumps(asdict(data)))
    #     return response

    def read_bear(self, bear_id: str) -> Response:
        response = requests.request('GET', f'{self._config.API_URL}/bear/{bear_id}')
        return response

    def read_all_bears(self) -> Response:
        response = requests.request('GET', f'{self._config.API_URL}/bear')
        return response

    def delete_all_bears(self) -> Response:
        response = requests.request('DELETE', f'{self._config.API_URL}/bear')
        return response
