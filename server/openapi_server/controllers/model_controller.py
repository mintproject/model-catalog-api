import connexion

from openapi_server.models.model import Model  # noqa: E501
from endpoint.utils import insert_query, prepare_jsonld, get_all_resource, get_resource
from openapi_server.static_vars import *


def create_model(user):  # noqa: E501
    """Create a model

    Creates a new instance of a &#x60;model&#x60;. # noqa: E501

    :param model: A new &#x60;model&#x60; to be created.
    :type model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        _ = Model.from_dict(connexion.request.get_json())  # noqa: E501
        model_json = prepare_jsonld(connexion.request.get_json(), user, MODEL_TYPE)
        return insert_query(model_json, user)

    return "Bad request", 400, {}


#todo: implement
def delete_model(id):  # noqa: E501
    """Delete a Model

    Deletes an existing &#x60;Model&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;Model&#x60;.
    :type id: str

    :rtype: None
    """
    return "Not Implemented", 501, {}


def get_model(id, username=None):  # noqa: E501
    """Get a Model

    Gets the details of a single instance of a &#x60;Model&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;Model&#x60;.
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: Model
    """
    try:
        return get_resource(id, MODEL_TYPE, username)
    except:
        return "Bad request", 400, {}

def get_models(username=None):  # noqa: E501
    """List All models

    Gets a list of all &#x60;model&#x60; entities. # noqa: E501

    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[Model]
    """
    try:
        return get_all_resource(MODEL_TYPE, username)
    except:
        return "Bad request", 400, {}

#todo: implement
def update_model(id, model):  # noqa: E501
    """Update a Model

    Updates an existing &#x60;Model&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;Model&#x60;.
    :type id: str
    :param model: Updated &#x60;Model&#x60; information.
    :type model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model = Model.from_dict(connexion.request.get_json())  # noqa: E501
    return "Not Implemented", 501, {}
