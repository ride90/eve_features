from flask import Blueprint, current_app as app

from .resources import RESOURCES


blueprint = Blueprint('auth', __name__)


def register_resources():
    for resource_key in RESOURCES:
        app.register_resource(resource_key, RESOURCES[resource_key])

blueprint.register_resources = register_resources

