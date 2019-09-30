import connexion
import six

from openapi_server.models.geo_shape import GeoShape  # noqa: E501
from openapi_server import util


def geoshapes_get(username=None):  # noqa: E501
    """List all GeoShape entities

    Gets a list of all GeoShape entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[GeoShape]
    """
    return 'do some magic!'


def geoshapes_id_delete(id):  # noqa: E501
    """Delete a GeoShape

    Delete an existing GeoShape # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def geoshapes_id_get(id, username=None):  # noqa: E501
    """Get a GeoShape

    Gets the details of a single instance of a GeoShape # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: GeoShape
    """
    return 'do some magic!'


def geoshapes_id_put(id, geo_shape=None):  # noqa: E501
    """Update a GeoShape

    Updates an existing GeoShape # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param geo_shape: An old GeoShapeto be updated
    :type geo_shape: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        geo_shape = GeoShape.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def geoshapes_post(geo_shape=None):  # noqa: E501
    """Create a GeoShape

    Create a new instance of a GeoShape # noqa: E501

    :param geo_shape: A new GeoShapeto be created
    :type geo_shape: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        geo_shape = GeoShape.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
