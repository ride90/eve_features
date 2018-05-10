RESOURCES = {
    'posts': {
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 3,
                'maxlength': 30,
                'required': True,
                'unique': False
            },
            'body': {
                'type': 'string',
                'required': True,
                'unique': True
            },
            'published': {
                'type': 'boolean',
                'default': False
            },
            'category': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'categories',
                    'field': '_id',
                    'embeddable': True
                },
                'required': True
            },
            'tags': {
                'type': 'list',
                'default': [],
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'tags',
                        'field': '_id',
                        'embeddable': True
                    }
                }

            }
        },
    },
    'categories': {
        'schema': {
            'name': {
                'type': 'string',
                'minlength': 2,
                'maxlength': 10,
                'required': True,
                'unique': True
            }
        },
        'item_title': 'category',
    },
    'tags': {
        'schema': {
            'name': {
                'type': 'string',
                'minlength': 2,
                'maxlength': 10,
                'required': True,
                'unique': True
            }
        }
    }
}
