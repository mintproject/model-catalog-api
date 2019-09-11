import connexion
import six

from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501
from openapi_server import util


def modelconfigurations_get(username=None):  # noqa: E501
    """List all ModelConfiguration entities

    Gets a list of all ModelConfiguration entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[ModelConfiguration]
    """
    return 'do some magic!'


def modelconfigurations_id_delete(id):  # noqa: E501
    """Delete a ModelConfiguration

    Delete an existing ModelConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def modelconfigurations_id_get(id, username=None):  # noqa: E501
    """Get a ModelConfiguration

    Gets the details of a single instance of a ModelConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: ModelConfiguration
    """
    return 'do some magic!'


def modelconfigurations_id_put(id, model_configuration=None):  # noqa: E501
    """Update a ModelConfiguration

    Updates an existing ModelConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param model_configuration: An old ModelConfigurationto be updated
    :type model_configuration: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def modelconfigurations_post(model_configuration=None):  # noqa: E501
    """Create a ModelConfiguration

    Create a new instance of a ModelConfiguration # noqa: E501

    :param model_configuration: A new ModelConfigurationto be created
    :type model_configuration: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
