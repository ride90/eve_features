from apps.blueprint import CustomBlueprint
from .resources import RESOURCES


blueprint = CustomBlueprint('blog', __name__, eve_resources=RESOURCES)