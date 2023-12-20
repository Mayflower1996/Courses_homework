"""Module containing URL, headers, and authentication details."""

import requests
from homework28.Data.payload_login_pass import PayloadLogin as pl


class UrlHeaders:
    """Class containing URL, headers, and authentication details."""

    URL = 'https://thinking-tester-contact-list.herokuapp.com'
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request('POST', f'{URL}/users/login', headers=headers, json=pl.payload)
    response_json = response.json()
    TOKEN = response_json.get('token')
    HEADERS = headers
    AUTH = {
        'Authorization': f'Bearer {TOKEN}'
    }
