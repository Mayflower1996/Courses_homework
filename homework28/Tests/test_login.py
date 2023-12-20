import requests
from jsonschema import validate
from homework28.Data.schemas_validate import SchemasValidate as sv
from homework28.Data.url_token_headers_auth import UrlHeaders as uh
from homework28.Data.payload_login_pass import PayloadLogin as pl


def test_successful_login_and_schema():
    response = requests.post(f'{uh.URL}/users/login', headers=uh.HEADERS, json=pl.payload)
    assert response.status_code == 200
    response_json = response.json()
    validate(instance=response_json, schema=sv.SCHEMA_LOGIN)


def test_incorrect_login():
    response = requests.post(f'{uh.URL}/users/login', headers=uh.HEADERS, json=pl.invalid_payload)
    assert response.status_code == 401
    assert response.text == ''


def test_empty_input():
    response = requests.post(f'{uh.URL}/users/login', headers=uh.HEADERS, json=pl.empty_payload)
    assert response.status_code == 401
    assert response.text == ''
