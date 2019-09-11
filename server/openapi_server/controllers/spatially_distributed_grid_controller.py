import connexion
import six

from openapi_server.models.spatially_distributed_grid import SpatiallyDistributedGrid  # noqa: E501
from openapi_server import util


def spatiallydistributedgrids_get(username=None):  # noqa: E501
    """List all SpatiallyDistributedGrid entities

    Gets a list of all SpatiallyDistributedGrid entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[SpatiallyDistributedGrid]
    """
    return 'do some magic!'


def spatiallydistributedgrids_id_delete(id):  # noqa: E501
    """Delete a SpatiallyDistributedGrid

    Delete an existing SpatiallyDistributedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def spatiallydistributedgrids_id_get(id, username=None):  # noqa: E501
    """Get a SpatiallyDistributedGrid

    Gets the details of a single instance of a SpatiallyDistributedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SpatiallyDistributedGrid
    """
    return 'do some magic!'


def spatiallydistributedgrids_id_put(id, spatially_distributed_grid=None):  # noqa: E501
    """Update a SpatiallyDistributedGrid

    Updates an existing SpatiallyDistributedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param spatially_distributed_grid: An old SpatiallyDistributedGridto be updated
    :type spatially_distributed_grid: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        spatially_distributed_grid = SpatiallyDistributedGrid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def spatiallydistributedgrids_post(spatially_distributed_grid=None):  # noqa: E501
    """Create a SpatiallyDistributedGrid

    Create a new instance of a SpatiallyDistributedGrid # noqa: E501

    :param spatially_distributed_grid: A new SpatiallyDistributedGridto be created
    :type spatially_distributed_grid: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        spatially_distributed_grid = SpatiallyDistributedGrid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
