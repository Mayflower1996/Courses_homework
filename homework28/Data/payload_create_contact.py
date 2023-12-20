"""Data module containing payloads for creating contacts."""


class PayloadCreate:
    """Class containing payloads for creating contacts."""

    CORRECT_PAYLOAD = {
        'firstName': 'Ivan',
        'lastName': 'Ivanov',
        'birthdate': '1996-11-26',
        'email': 'example@example.com',
        'phone': '1234567890',
        'street1': 'Test1',
        'street2': 'Test2',
        'city': 'Minsk',
        'stateProvince': 'Minsk',
        'postalCode': '220069',
        'country': 'Belarus'
    }

    INCORRECT_PAYLOAD_MISSING_FIELD = {
        'firstName': 'Ivan',
        'birthdate': '1996-11-26',
        'email': 'example@example.com',
        'phone': '1234567890',
        'street1': 'Test1',
        'street2': 'Test2',
        'city': 'Minsk',
        'stateProvince': 'Minsk',
        'postalCode': '220069',
        'country': 'Belarus'
    }

    INCORRECT_PAYLOAD_EMPTY_FIELDS = {
        'firstName': '',
        'lastName': '',
        'birthdate': '',
        'email': '',
        'phone': '',
        'street1': '',
        'street2': '',
        'city': '',
        'stateProvince': '',
        'postalCode': '',
        'country': ''
    }
