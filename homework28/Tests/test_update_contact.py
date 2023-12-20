import requests
from jsonschema.validators import validate
from homework28.Data.payload_update_contact import PayloadUpdate as pu
from homework28.Data.schemas_validate import SchemasValidate as sv
from homework28.Data.url_token_headers_auth import UrlHeaders as uh


def test_update_contact_success(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.put(f'{uh.URL}/contacts/{ID}', headers=uh.AUTH, json=pu.CORRECT_PAYLOAD_UPDATE)
    assert response.status_code == 200
    response_json = response.json()
    validate(instance=response_json, schema=sv.SCHEMA_CREATE_CONTACT)


def test_update_contact_empty_field(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.put(f'{uh.URL}/contacts/{ID}', headers=uh.AUTH, json=pu.INCORRECT_PAYLOAD_UPDATE_EMPTY_FIELD)
    assert response.status_code == 400
    response_json = response.json()
    validate(instance=response_json, schema=sv.SCHEMA_ERROR_UPDATE_CONTACT)


def test_update_contact_all_empty_fields(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.put(f'{uh.URL}/contacts/{ID}', headers=uh.AUTH, json=pu.INCORRECT_PAYLOAD_UPDATE_EMPTY_FIELDS)
    assert response.status_code == 400
    response_json = response.json()
    validate(instance=response_json, schema=sv.SCHEMA_ERROR_UPDATE_CONTACT)
