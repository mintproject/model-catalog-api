import connexion
import six

from openapi_server.models.causal_diagram import CausalDiagram  # noqa: E501
from openapi_server import util


def causaldiagrams_get(username=None):  # noqa: E501
    """List all CausalDiagram entities

    Gets a list of all CausalDiagram entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[CausalDiagram]
    """
    return 'do some magic!'


def causaldiagrams_id_delete(id):  # noqa: E501
    """Delete a CausalDiagram

    Delete an existing CausalDiagram # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def causaldiagrams_id_get(id, username=None):  # noqa: E501
    """Get a CausalDiagram

    Gets the details of a single instance of a CausalDiagram # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: CausalDiagram
    """
    return 'do some magic!'


def causaldiagrams_id_put(id, causal_diagram=None):  # noqa: E501
    """Update a CausalDiagram

    Updates an existing CausalDiagram # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param causal_diagram: An old CausalDiagramto be updated
    :type causal_diagram: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        causal_diagram = CausalDiagram.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def causaldiagrams_post(causal_diagram=None):  # noqa: E501
    """Create a CausalDiagram

    Create a new instance of a CausalDiagram # noqa: E501

    :param causal_diagram: A new CausalDiagramto be created
    :type causal_diagram: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        causal_diagram = CausalDiagram.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
