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
    Register blueprints.
    :param app: eve app object
    :return:
    """
    from .auth import blueprint as auth_blueprint
    from .blog import blueprint as blog_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(blog_blueprint)


def get_app(config=None):
    abs_path = os.path.abspath(
        os.path.dirname(os.path.dirname(__file__))
    )

    # flask config
    app_config = flask.Config(abs_path)
    app_config.from_object('settings.base')

    if config:
        app_config.update(config)

    # create eve blog app instance
    app = BlogEve(settings=app_config)

    # register blueprints with resources inside
    _register_blueprints(app)

    return app
