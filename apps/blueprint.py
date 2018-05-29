from flask import Blueprint
from flask.blueprints import BlueprintSetupState
from flask.helpers import _endpoint_from_view_func

from settings.base import API_VERSION, URL_PREFIX


class CustomBlueprintSetupState(BlueprintSetupState):

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        """A helper method to register a rule (and optionally a view function)
        to the application.  The endpoint is automatically prefixed with the
        blueprint's name.
        """

        if self.url_prefix is not None and not options.get('no_prefix', False):
            if rule:
                rule = '/'.join((
                    self.url_prefix.rstrip('/'), rule.lstrip('/')))
            else:
                rule = self.url_prefix

        if 'no_prefix' in options:
            del options['no_prefix']

        options.setdefault('subdomain', self.subdomain)
        if endpoint is None:
            endpoint = _endpoint_from_view_func(view_func)
        defaults = self.url_defaults
        if 'defaults' in options:
            defaults = dict(defaults, **options.pop('defaults'))
        self.app.add_url_rule(rule, '%s.%s' % (self.blueprint.name, endpoint),
                              view_func, defaults=defaults, **options)


class CustomBlueprint(Blueprint):
    """
    Custom blueprint which helps to register Eve resources
    """

    def __init__(self, *args, eve_resources=None, **kwargs):
        super(CustomBlueprint, self).__init__(*args, **kwargs)
        self._eve_resources = eve_resources

    def register(self, app, options, first_registration=False):
        super(CustomBlueprint, self).register(app, options, first_registration=False)
        self._app = app
        self._register_eve_resources(app)

    def make_setup_state(self, app, options, first_registration=False):
        """Creates an instance of :meth:`~CustomBlueprintSetupState`
        object that is later passed to the register callback functions.
        Subclasses can override this to return a subclass of the setup state.
        """

        return CustomBlueprintSetupState(self, app, options, first_registration)

    def _register_eve_resources(self, app):
        if self._eve_resources:
            for resource_key in self._eve_resources:
                app.register_resource(
                    '/'.join((self.url_prefix.strip('/'), resource_key)) if self.url_prefix else resource_key,
                    self._eve_resources[resource_key]
                )

    def api_route(self, rule, **options):
        options.update({'no_prefix': True})

        if self.url_prefix:
            rule = '/{}'.format('/'.join(
                (URL_PREFIX, API_VERSION, self.url_prefix.strip('/'), rule.strip('/'))
            ))

        def decorator(f):
            endpoint = options.pop("endpoint", f.__name__)
            self.add_url_rule(rule, endpoint, f, **options)
            return f

        return decorator
