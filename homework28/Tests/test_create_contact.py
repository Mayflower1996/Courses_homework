import requests
from jsonschema import validate
from homework28.Data.payload_create_contact import PayloadCreate as pc
from homework28.Data.schemas_validate import SchemasValidate as sv
from homework28.Data.url_token_headers_auth import UrlHeaders as uh


def test_create_contact_success_and_schema():
    response = requests.post(f'{uh.URL}/contacts', headers=uh.AUTH, json=pc.CORRECT_PAYLOAD)
    assert response.status_code == 201
    response_json = response.json()
    validate(instance=response_json, schema=sv.SCHEMA_CREATE_CONTACT)


def test_create_contact_missing_field():
    response = requests.post(f'{uh.URL}/contacts', headers=uh.AUTH, json=pc.INCORRECT_PAYLOAD_MISSING_FIELD)
    assert response.status_code == 400
    response_json = response.json()
    validate(instance=response_json, schema=sv.SCHEMA_ERROR_CREATE_CONTACT)


def test_create_contact_all_fields_empty():
    response = requests.post(f'{uh.URL}/contacts', headers=uh.AUTH, json=pc.INCORRECT_PAYLOAD_EMPTY_FIELDS)
    assert response.status_code == 400
    response_json = response.json()
    validate(instance=response_json, schema=sv.SCHEMA_ERROR_CREATE_CONTACT)
