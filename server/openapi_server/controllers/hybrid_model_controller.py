import connexion
import six

from openapi_server.models.hybrid_model import HybridModel  # noqa: E501
from openapi_server import util


def hybridmodels_get(username=None):  # noqa: E501
    """List all HybridModel entities

    Gets a list of all HybridModel entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[HybridModel]
    """
    return 'do some magic!'


def hybridmodels_id_delete(id):  # noqa: E501
    """Delete a HybridModel

    Delete an existing HybridModel # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def hybridmodels_id_get(id, username=None):  # noqa: E501
    """Get a HybridModel

    Gets the details of a single instance of a HybridModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: HybridModel
    """
    return 'do some magic!'


def hybridmodels_id_put(id, hybrid_model=None):  # noqa: E501
    """Update a HybridModel

    Updates an existing HybridModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param hybrid_model: An old HybridModelto be updated
    :type hybrid_model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        hybrid_model = HybridModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def hybridmodels_post(hybrid_model=None):  # noqa: E501
    """Create a HybridModel

    Create a new instance of a HybridModel # noqa: E501

    :param hybrid_model: A new HybridModelto be created
    :type hybrid_model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        hybrid_model = HybridModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
