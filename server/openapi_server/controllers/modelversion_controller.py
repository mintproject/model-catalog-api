import connexion

from openapi_server.models.model_version import ModelVersion  # noqa: E501
from endpoint.utils import insert_query, prepare_jsonld, get_all_resource, get_resource
from openapi_server.static_vars import *


def create_model_version(user):  # noqa: E501
    """Create a ModelVersion

    Creates a new instance of a &#x60;ModelVersion&#x60;. # noqa: E501

    :param model_version: A new &#x60;ModelVersion&#x60; to be created.
    :type model_version: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        _ = ModelVersion.from_dict(connexion.request.get_json())  # noqa: E501
        model_version_json = prepare_jsonld(connexion.request.get_json(), user, MODELVERSION_TYPE)
        return insert_query(model_version_json, user)

    return "Bad request", 400, {}

#todo: implement
def delete_model_version(id):  # noqa: E501
    """Delete a ModelVersion

    Deletes an existing &#x60;ModelVersion&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelVersion&#x60;.
    :type id: str

    :rtype: None
    """
    "Not Implemented", 501, {}


def get_model_version(id, username=None):  # noqa: E501
    """Get a ModelVersion

    Gets the details of a single instance of a &#x60;ModelVersion&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelVersion&#x60;.
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: ModelVersion
    """
    response = get_resource(id, MODELVERSION_TYPE, username)
    try:
        return response.json()
    except:
        return "Bad request", 400, {}


def get_model_versions(username=None):  # noqa: E501
    """List All ModelVersions

    Gets a list of all &#x60;ModelVersion&#x60; entities. # noqa: E501

    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[ModelVersion]
    """
    response = get_all_resource(MODELVERSION_TYPE, username)
    try:
        return response.json()
    except:
        return "Bad request", 400, {}


def update_model_version(id, model_version):  # noqa: E501
    """Update a ModelVersion

    Updates an existing &#x60;ModelVersion&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelVersion&#x60;.
    :type id: str
    :param model_version: Updated &#x60;ModelVersion&#x60; information.
    :type model_version: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_version = ModelVersion.from_dict(connexion.request.get_json())  # noqa: E501
    "Not Implemented", 501, {}
