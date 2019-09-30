import connexion
import six

from openapi_server.models.spatial_resolution import SpatialResolution  # noqa: E501
from openapi_server import util


def spatialresolutions_get(username=None):  # noqa: E501
    """List all SpatialResolution entities

    Gets a list of all SpatialResolution entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[SpatialResolution]
    """
    return 'do some magic!'


def spatialresolutions_id_delete(id):  # noqa: E501
    """Delete a SpatialResolution

    Delete an existing SpatialResolution # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def spatialresolutions_id_get(id, username=None):  # noqa: E501
    """Get a SpatialResolution

    Gets the details of a single instance of a SpatialResolution # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SpatialResolution
    """
    return 'do some magic!'


def spatialresolutions_id_put(id, spatial_resolution=None):  # noqa: E501
    """Update a SpatialResolution

    Updates an existing SpatialResolution # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param spatial_resolution: An old SpatialResolutionto be updated
    :type spatial_resolution: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        spatial_resolution = SpatialResolution.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def spatialresolutions_post(spatial_resolution=None):  # noqa: E501
    """Create a SpatialResolution

    Create a new instance of a SpatialResolution # noqa: E501

    :param spatial_resolution: A new SpatialResolutionto be created
    :type spatial_resolution: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        spatial_resolution = SpatialResolution.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
