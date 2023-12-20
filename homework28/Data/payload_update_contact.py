"""Data module containing payloads for updating contacts."""


CORRECT_PAYLOAD_UPDATE = {
    'firstName': 'Ivans',
    'lastName': 'Ivanovs',
    'birthdate': '1996-11-26',
    'email': 'example@example.com',
    'phone': '1234567891',
    'street1': 'Test3',
    'street2': 'Test4',
    'city': 'Minsks',
    'stateProvince': 'Minsks',
    'postalCode': '220060',
    'country': 'Belaruss'
}

INCORRECT_PAYLOAD_UPDATE_EMPTY_FIELD = {
    'firstName': '',
    'lastName': 'Ivanovs',
    'birthdate': '1996-11-26',
    'email': 'example@example.com',
    'phone': '1234567891',
    'street1': 'Test3',
    'street2': 'Test4',
    'city': 'Minsks',
    'stateProvince': 'Minsks',
    'postalCode': '220060',
    'country': 'Belaruss'
}

INCORRECT_PAYLOAD_UPDATE_EMPTY_FIELDS = {
    'firstName': '',
    'lastName': ''
}
