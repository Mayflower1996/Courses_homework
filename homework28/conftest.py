import requests
import pytest
from Data.payload_create_contact import CORRECT_PAYLOAD
from Data.url_token_headers_auth import URL, AUTH


@pytest.fixture(scope='module')
def create_contact_and_get_id():
    url = f'{URL}/contacts'
    response = requests.post(url, headers=AUTH, json=CORRECT_PAYLOAD)
    ID = response.json().get('_id')
    return ID
