import requests
from jsonschema import validate
from homework28.Data.schemas_validate import SCHEMA_LOGIN
from homework28.Data.url_token_headers_auth import URL, HEADERS
from homework28.Data.payload_login_pass import payload, empty_payload, invalid_payload


def test_successful_login_and_schema():
    response = requests.post(f"{URL}/users/login", headers=HEADERS, json=payload)
    assert response.status_code == 200
    response_json = response.json()
    validate(instance=response_json, schema=SCHEMA_LOGIN)


def test_incorrect_login():
    response = requests.post(f"{URL}/users/login", headers=HEADERS, json=invalid_payload)
    assert response.status_code == 401
    assert response.text == ''


def test_empty_input():
    response = requests.post(f"{URL}/users/login", headers=HEADERS, json=empty_payload)
    assert response.status_code == 401
    assert response.text == ''
