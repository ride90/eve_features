RESOURCES = {
    'accounts': {
        'schema': {
            'username': {
                'type': 'string',
                'required': True,
                'unique': True
            },
            'password': {
                'type': 'string',
                'required': True
            },
            'roles': {
                'type': 'list',
                'allowed': ['user', 'superuser'],
                'required': True,
            },
            'location': {
                'type': 'dict',
                'schema': {
                    'country': {'type': 'string'},
                    'city': {'type': 'string'},
                    'address': {'type': 'string'}
                },
            },
            'born': {
                'type': 'datetime',
            },
        },
        # Disable endpoint caching.
        'cache_control': '',
        'cache_expires': 0,
    }
}
