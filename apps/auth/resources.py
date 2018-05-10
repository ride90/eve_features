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
                'allowed': ['user', 'superuser', 'admin'],
                'required': True,
            }
        },
        # Disable endpoint caching.
        'cache_control': '',
        'cache_expires': 0,
    }
}
