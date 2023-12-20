SCHEMA_CREATE_CONTACT = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string'},
        'firstName': {'type': 'string'},
        'lastName': {'type': 'string'},
        'birthdate': {'type': 'string'},
        'email': {'type': 'string'},
        'phone': {'type': 'string'},
        'street1': {'type': 'string'},
        'street2': {'type': 'string'},
        'city': {'type': 'string'},
        'stateProvince': {'type': 'string'},
        'postalCode': {'type': 'string'},
        'country': {'type': 'string'}
    }
}

SCHEMA_LOGIN = {
    'type': 'object',
    'properties': {
        'user': {
            'type': 'object',
            'properties': {
                '_id': {'type': 'string'},
                'firstName': {'type': 'string'},
                'lastName': {'type': 'string'},
                'email': {'type': 'string'},
                '__v': {'type': 'integer'}
            },
            'required': ['_id', 'firstName', 'lastName', 'email', '__v']
        },
        'token': {'type': 'string'}
    },
    'required': ['user', 'token']
}

SCHEMA_ERROR_CREATE_CONTACT = {
    'type': 'object',
    'properties': {
        'errors': {
            'type': 'object',
            'properties': {
                'lastName': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'},
                        'message': {'type': 'string'},
                        'properties': {
                            'type': 'object',
                            'properties': {
                                'message': {'type': 'string'},
                                'path': {'type': 'string'},
                                'type': {'type': 'string'},
                                'value': {'type': ['string', 'null']}
                            },
                            'required': ['message', 'path', 'type']
                        },
                        'kind': {'type': 'string'},
                        'path': {'type': 'string'}
                    },
                    'required': ['name', 'message', 'properties', 'kind', 'path']
                }
            },
            'required': ['lastName']
        },
        '_message': {'type': 'string'},
        'message': {'type': 'string'}
    },
    'required': ['errors', '_message', 'message']
}

SCHEMA_ERROR_UPDATE_CONTACT = {
    'type': 'object',
    'properties': {
        '_message': {'type': 'string'},
        'errors': {
            'type': 'object',
            'properties': {
                'lastName': {
                    'type': 'object',
                    'properties': {
                        'kind': {'type': 'string'},
                        'message': {'type': 'string'},
                        'name': {'type': 'string'},
                        'path': {'type': 'string'},
                        'properties': {
                            'type': 'object',
                            'properties': {
                                'message': {'type': 'string'},
                                'type': {'type': 'string'},
                                'path': {'type': 'string'},
                                'value': {'type': 'string'}
                            },
                            'required': ['message', 'type', 'path', 'value'],
                            'additionalProperties': False
                        }
                    },
                    'required': ['kind', 'message', 'name', 'path', 'properties']
                },
                'firstName': {
                    'type': 'object',
                    'properties': {
                        'kind': {'type': 'string'},
                        'message': {'type': 'string'},
                        'name': {'type': 'string'},
                        'path': {'type': 'string'},
                        'properties': {
                            'type': 'object',
                            'properties': {
                                'message': {'type': 'string'},
                                'type': {'type': 'string'},
                                'path': {'type': 'string'},
                                'value': {'type': 'string'}
                            },
                            'required': ['message', 'type', 'path', 'value'],
                            'additionalProperties': False
                        }
                    },
                    'required': ['kind', 'message', 'name', 'path', 'properties']
                }
            },
            'required': ['lastName', 'firstName'],
            'additionalProperties': False
        },
        'message': {'type': 'string'}
    },
    'required': ['_message', 'errors', 'message'],
    'additionalProperties': False
}
