import connexion
import six

from openapi_server.models.geo_coordinates import GeoCoordinates  # noqa: E501
from openapi_server import util


def geocoordinatess_get(username=None):  # noqa: E501
    """List all GeoCoordinates entities

    Gets a list of all GeoCoordinates entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[GeoCoordinates]
    """
    return 'do some magic!'


def geocoordinatess_id_delete(id):  # noqa: E501
    """Delete a GeoCoordinates

    Delete an existing GeoCoordinates # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def geocoordinatess_id_get(id, username=None):  # noqa: E501
    """Get a GeoCoordinates

    Gets the details of a single instance of a GeoCoordinates # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: GeoCoordinates
    """
    return 'do some magic!'


def geocoordinatess_id_put(id, geo_coordinates=None):  # noqa: E501
    """Update a GeoCoordinates

    Updates an existing GeoCoordinates # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param geo_coordinates: An old GeoCoordinatesto be updated
    :type geo_coordinates: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        geo_coordinates = GeoCoordinates.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def geocoordinatess_post(geo_coordinates=None):  # noqa: E501
    """Create a GeoCoordinates

    Create a new instance of a GeoCoordinates # noqa: E501

    :param geo_coordinates: A new GeoCoordinatesto be created
    :type geo_coordinates: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        geo_coordinates = GeoCoordinates.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
