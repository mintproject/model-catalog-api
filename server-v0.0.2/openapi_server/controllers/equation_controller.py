import connexion
import six

from openapi_server.models.equation import Equation  # noqa: E501
from openapi_server import util


def equations_get(username=None):  # noqa: E501
    """List all Equation entities

    Gets a list of all Equation entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[Equation]
    """
    return 'do some magic!'


def equations_id_delete(id):  # noqa: E501
    """Delete a Equation

    Delete an existing Equation # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def equations_id_get(id, username=None):  # noqa: E501
    """Get a Equation

    Gets the details of a single instance of a Equation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Equation
    """
    return 'do some magic!'


def equations_id_put(id, equation=None):  # noqa: E501
    """Update a Equation

    Updates an existing Equation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param equation: An old Equationto be updated
    :type equation: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        equation = Equation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def equations_post(equation=None):  # noqa: E501
    """Create a Equation

    Create a new instance of a Equation # noqa: E501

    :param equation: A new Equationto be created
    :type equation: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        equation = Equation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
