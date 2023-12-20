"""Data module containing login payload information."""


class PayloadLogin:
    """Class containing different payloads related to log in functionality."""

    payload = {
      'email': 'jjgraffity@gmail.com',
      'password': 'Vania1996123qwe'
    }

    invalid_payload = {
            'email': 'nonexistent@example.com',
            'password': 'invalidPassword123'
    }

    empty_payload = {
            'email': '',
            'password': ''
    }
