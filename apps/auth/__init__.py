from apps.blueprint import CustomBlueprint
from .resources import RESOURCES


blueprint = CustomBlueprint('auth', __name__, eve_resources=RESOURCES)
