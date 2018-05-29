from . import blueprint


@blueprint.api_route('/register', methods=['GET'])
def register():

    return 'hi from api'
