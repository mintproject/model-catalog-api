import connexion

from openapi_server.models.model_version import ModelVersion  # noqa: E501
from endpoint.utils import insert_query, prepare_jsonld, get_all_resource, get_resource, delete_query
from openapi_server.static_vars import *


def create_model_version(user):  # noqa: E501
    """Create a ModelVersion

    Creates a new instance of a &#x60;ModelVersion&#x60;. # noqa: E501

    :param model_version: A new &#x60;ModelVersion&#x60; to be created.
    :type model_version: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        model_version = ModelVersion.from_dict(connexion.request.get_json())  # noqa: E501
        if model_version.type:
            model_version.type.append(MODELVERSION_TYPE)
        else:
            model_version.type = [MODELVERSION_TYPE]
        model_version_json = prepare_jsonld(model_version, user)
        return insert_query(model_version_json, user)

    return "Bad request", 400, {}


def delete_model_version(id, user):  # noqa: E501
    """Delete a ModelVersion

    Deletes an existing &#x60;ModelVersion&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelVersion&#x60;.
    :type id: str

    :rtype: None
    """
    try:
        return delete_query(id, user)
    except:
        return "Bad request", 400, {}

def get_model_version(id, username=None):  # noqa: E501
    """Get a ModelVersion

    Gets the details of a single instance of a &#x60;ModelVersion&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelVersion&#x60;.
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: ModelVersion
    """
    model_version = ModelVersion()
    try:
        response = get_resource(id, MODELVERSION_TYPE, username)
    except:
        return "Bad request", 400, {}

    if response:
        model_version = ModelVersion.from_dict(response[0])
    else:
        return "Not found", 404, {}
    return model_version


def get_model_versions(username=None):  # noqa: E501
    """List All ModelVersions

    Gets a list of all &#x60;ModelVersion&#x60; entities. # noqa: E501

    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[ModelVersion]
    """
    model_version = ModelVersion()
    try:
        response = get_all_resource(MODELVERSION_TYPE, username)
    except:
        return "Bad request", 400, {}

    model_versions = []
    for d in response:
        model_versions.append(ModelVersion.from_dict(d))
    return model_versions


def update_model_version(id, user):  # noqa: E501
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
        if model_version.type:
            model_version.type.append(MODELVERSION_TYPE)
        else:
            model_version.type = [MODELVERSION_TYPE]
        model_version_json = prepare_jsonld(model_version, user)
        delete_query(id, user);
        return insert_query(model_version_json, user)
    return "Bad request", 400, {}
