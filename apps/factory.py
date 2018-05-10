import os

import eve
import flask


class BlogEve(eve.Eve):
    """
    Main Eve object.
    On initialization it will load Eve settings, then
    configure and enable the API endpoints.
    """
    pass


def _register_blueprints(app):
    """
    Register blueprints and eve domains
    :param app: app object
    :return:
    """
    from .auth import blueprint as auth_blueprint
    app.register_blueprint(auth_blueprint)

    with app.app_context():
        auth_blueprint.register_resources()


def get_app(config=None):
    abs_path = os.path.abspath(
        os.path.dirname(os.path.dirname(__file__))
    )

    app_config = flask.Config(abs_path)
    app_config.from_object('settings.base')

    if config:
        app_config.update(config)

    # create app
    app = BlogEve(settings=app_config)

    # register blue prints and resources
    _register_blueprints(app)

    return app
