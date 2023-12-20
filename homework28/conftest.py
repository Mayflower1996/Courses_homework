"""Fixture for contact creation and ID retrieval."""


import requests
import pytest
from Data.payload_create_contact import PayloadCreate as pc
from Data.url_token_headers_auth import UrlHeaders as uh


@pytest.fixture(scope='module')
def create_contact_and_get_id():
    """Create a contact and retrieve its ID."""
    url = f'{uh.URL}/contacts'
    response = requests.post(url, headers=uh.AUTH, json=pc.CORRECT_PAYLOAD)
    ID = response.json().get('_id')
    return ID
