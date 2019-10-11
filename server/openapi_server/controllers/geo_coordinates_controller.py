import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import GEOCOORDINATES_TYPE_NAME, GEOCOORDINATES_TYPE_URI

from openapi_server.models.geo_coordinates import GeoCoordinates  # noqa: E501
from openapi_server import util

def geocoordinatess_get(username=None, label=None):  # noqa: E501
    """List all GeoCoordinates entities

    Gets a list of all GeoCoordinates entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[GeoCoordinates]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)

def geocoordinatess_id_delete(id, user):  # noqa: E501
    """Delete a GeoCoordinates

    Delete an existing GeoCoordinates # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)

def geocoordinatess_id_get(id, username=None):  # noqa: E501
    """Get a GeoCoordinates

    Gets the details of a single instance of a GeoCoordinates # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: GeoCoordinates
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)

def geocoordinatess_id_put(id, user, geo_coordinates=None):  # noqa: E501
    """Update a GeoCoordinates

    Updates an existing GeoCoordinates # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param geo_coordinates: An old GeoCoordinatesto be updated
    :type geo_coordinates: dict | bytes

    :rtype: GeoCoordinates
    """

    if connexion.request.is_json:
        geo_coordinates = GeoCoordinates.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=geo_coordinates,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)

def geocoordinatess_post(user, geo_coordinates=None):  # noqa: E501
    """Create a GeoCoordinates

    Create a new instance of a GeoCoordinates # noqa: E501

    :param user: Username
    :type user: str
    :param geo_coordinates: A new GeoCoordinatesto be created
    :type geo_coordinates: dict | bytes

    :rtype: GeoCoordinates
    """

    if connexion.request.is_json:
        geo_coordinates = GeoCoordinates.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=geo_coordinates,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)
