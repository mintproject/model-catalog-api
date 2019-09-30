import connexion
import six

from openapi_server.models.empirical_model import EmpiricalModel  # noqa: E501
from openapi_server import util


def empiricalmodels_get(username=None):  # noqa: E501
    """List all EmpiricalModel entities

    Gets a list of all EmpiricalModel entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[EmpiricalModel]
    """
    return 'do some magic!'


def empiricalmodels_id_delete(id):  # noqa: E501
    """Delete a EmpiricalModel

    Delete an existing EmpiricalModel # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def empiricalmodels_id_get(id, username=None):  # noqa: E501
    """Get a EmpiricalModel

    Gets the details of a single instance of a EmpiricalModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: EmpiricalModel
    """
    return 'do some magic!'


def empiricalmodels_id_put(id, empirical_model=None):  # noqa: E501
    """Update a EmpiricalModel

    Updates an existing EmpiricalModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param empirical_model: An old EmpiricalModelto be updated
    :type empirical_model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        empirical_model = EmpiricalModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def empiricalmodels_post(empirical_model=None):  # noqa: E501
    """Create a EmpiricalModel

    Create a new instance of a EmpiricalModel # noqa: E501

    :param empirical_model: A new EmpiricalModelto be created
    :type empirical_model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        empirical_model = EmpiricalModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
