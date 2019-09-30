import connexion
import six

from openapi_server.models.grid import Grid  # noqa: E501
from openapi_server import util


def grids_get(username=None):  # noqa: E501
    """List all Grid entities

    Gets a list of all Grid entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[Grid]
    """
    return 'do some magic!'


def grids_id_delete(id):  # noqa: E501
    """Delete a Grid

    Delete an existing Grid # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def grids_id_get(id, username=None):  # noqa: E501
    """Get a Grid

    Gets the details of a single instance of a Grid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Grid
    """
    return 'do some magic!'


def grids_id_put(id, grid=None):  # noqa: E501
    """Update a Grid

    Updates an existing Grid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param grid: An old Gridto be updated
    :type grid: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        grid = Grid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def grids_post(grid=None):  # noqa: E501
    """Create a Grid

    Create a new instance of a Grid # noqa: E501

    :param grid: A new Gridto be created
    :type grid: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        grid = Grid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
