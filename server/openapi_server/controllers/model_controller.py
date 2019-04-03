import connexion

from openapi_server.models.model import Model  # noqa: E501
from endpoint.utils import insert_query, prepare_jsonld
from openapi_server.static_vars import *

def createmodel(user):  # noqa: E501
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

    return "Bad request", 403, {}

def delete_model(model_id):  # noqa: E501
    """Delete a Model

    Deletes an existing &#x60;Model&#x60;. # noqa: E501

    :param model_id: A unique identifier for a &#x60;Model&#x60;.
    :type model_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_model(model_id):  # noqa: E501
    """Get a Model

    Gets the details of a single instance of a &#x60;Model&#x60;. # noqa: E501

    :param model_id: A unique identifier for a &#x60;Model&#x60;.
    :type model_id: str

    :rtype: Model
    """
    return 'do some magic!'


def getmodels():  # noqa: E501
    """List All models

    Gets a list of all &#x60;model&#x60; entities. # noqa: E501


    :rtype: List[Model]
    """
    return 'do some magic!'


def update_model(model_id, model):  # noqa: E501
    """Update a Model

    Updates an existing &#x60;Model&#x60;. # noqa: E501

    :param model_id: A unique identifier for a &#x60;Model&#x60;.
    :type model_id: str
    :param model: Updated &#x60;Model&#x60; information.
    :type model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model = Model.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
