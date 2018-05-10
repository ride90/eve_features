from flask import Blueprint


class CustomBlueprint(Blueprint):
    """
    Custom blueprint which helps to register Eve resources
    """

    def __init__(self, *args, eve_resources=None, **kwargs):
        super(CustomBlueprint, self).__init__(*args, **kwargs)
        self._eve_resources = eve_resources

    def register(self, app, options, first_registration=False):
        super(CustomBlueprint, self).register(app, options, first_registration=False)
        self._register_eve_resources(app)

    def _register_eve_resources(self, app):
        if self._eve_resources:
            for resource_key in self._eve_resources:
                app.register_resource(resource_key, self._eve_resources[resource_key])
