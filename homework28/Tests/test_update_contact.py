import requests
from jsonschema.validators import validate
from homework28.Data.payload_update_contact import CORRECT_PAYLOAD_UPDATE, INCORRECT_PAYLOAD_UPDATE_EMPTY_FIELD, \
    INCORRECT_PAYLOAD_UPDATE_EMPTY_FIELDS
from homework28.Data.schemas_validate import SCHEMA_CREATE_CONTACT, SCHEMA_ERROR_UPDATE_CONTACT
from homework28.Data.url_token_headers_auth import URL, AUTH


def test_update_contact_success(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.put(f'{URL}/contacts/{ID}', headers=AUTH, json=CORRECT_PAYLOAD_UPDATE)
    assert response.status_code == 200
    response_json = response.json()
    validate(instance=response_json, schema=SCHEMA_CREATE_CONTACT)


def test_update_contact_empty_field(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.put(f'{URL}/contacts/{ID}', headers=AUTH, json=INCORRECT_PAYLOAD_UPDATE_EMPTY_FIELD)
    assert response.status_code == 400
    response_json = response.json()
    validate(instance=response_json, schema=SCHEMA_ERROR_UPDATE_CONTACT)


def test_update_contact_all_empty_fields(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.put(f'{URL}/contacts/{ID}', headers=AUTH, json=INCORRECT_PAYLOAD_UPDATE_EMPTY_FIELDS)
    assert response.status_code == 400
    response_json = response.json()
    validate(instance=response_json, schema=SCHEMA_ERROR_UPDATE_CONTACT)
