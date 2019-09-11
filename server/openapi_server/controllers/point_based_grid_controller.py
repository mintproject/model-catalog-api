import connexion
import six

from openapi_server.models.point_based_grid import PointBasedGrid  # noqa: E501
from openapi_server import util


def pointbasedgrids_get(username=None):  # noqa: E501
    """List all PointBasedGrid entities

    Gets a list of all PointBasedGrid entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[PointBasedGrid]
    """
    return 'do some magic!'


def pointbasedgrids_id_delete(id):  # noqa: E501
    """Delete a PointBasedGrid

    Delete an existing PointBasedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def pointbasedgrids_id_get(id, username=None):  # noqa: E501
    """Get a PointBasedGrid

    Gets the details of a single instance of a PointBasedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: PointBasedGrid
    """
    return 'do some magic!'


def pointbasedgrids_id_put(id, point_based_grid=None):  # noqa: E501
    """Update a PointBasedGrid

    Updates an existing PointBasedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param point_based_grid: An old PointBasedGridto be updated
    :type point_based_grid: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        point_based_grid = PointBasedGrid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pointbasedgrids_post(point_based_grid=None):  # noqa: E501
    """Create a PointBasedGrid

    Create a new instance of a PointBasedGrid # noqa: E501

    :param point_based_grid: A new PointBasedGridto be created
    :type point_based_grid: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        point_based_grid = PointBasedGrid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
