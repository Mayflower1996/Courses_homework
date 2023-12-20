import requests
from jsonschema import validate
from homework28.Data.payload_create_contact import INCORRECT_PAYLOAD_EMPTY_FIELDS, CORRECT_PAYLOAD, \
    INCORRECT_PAYLOAD_MISSING_FIELD
from homework28.Data.schemas_validate import SCHEMA_CREATE_CONTACT, SCHEMA_ERROR_CREATE_CONTACT
from homework28.Data.url_token_headers_auth import URL, AUTH


def test_create_contact_success_and_schema():
    response = requests.post(f"{URL}/contacts", headers=AUTH, json=CORRECT_PAYLOAD)
    assert response.status_code == 201
    response_json = response.json()
    validate(instance=response_json, schema=SCHEMA_CREATE_CONTACT)


def test_create_contact_missing_field():
    response = requests.post(f"{URL}/contacts", headers=AUTH, json=INCORRECT_PAYLOAD_MISSING_FIELD)
    assert response.status_code == 400
    response_json = response.json()
    validate(instance=response_json, schema=SCHEMA_ERROR_CREATE_CONTACT)


def test_create_contact_all_fields_empty():
    response = requests.post(f"{URL}/contacts", headers=AUTH, json=INCORRECT_PAYLOAD_EMPTY_FIELDS)
    assert response.status_code == 400
    response_json = response.json()
    validate(instance=response_json, schema=SCHEMA_ERROR_CREATE_CONTACT)
