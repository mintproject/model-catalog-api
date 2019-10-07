import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import GEOSHAPE_TYPE_NAME, GEOSHAPE_TYPE_URI

from openapi_server.models.geo_shape import GeoShape  # noqa: E501
from openapi_server import util

def geoshapes_get(username=None, query_text=None):  # noqa: E501
    """List all GeoShape entities

    Gets a list of all GeoShape entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[GeoShape]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)

def geoshapes_id_delete(id, user):  # noqa: E501
    """Delete a GeoShape

    Delete an existing GeoShape # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)

def geoshapes_id_get(id, username=None):  # noqa: E501
    """Get a GeoShape

    Gets the details of a single instance of a GeoShape # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: GeoShape
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)

def geoshapes_id_put(id, user, geo_shape=None):  # noqa: E501
    """Update a GeoShape

    Updates an existing GeoShape # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param geo_shape: An old GeoShapeto be updated
    :type geo_shape: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        geo_shape = GeoShape.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=geo_shape,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)

def geoshapes_post(user, geo_shape=None):  # noqa: E501
    """Create a GeoShape

    Create a new instance of a GeoShape # noqa: E501

    :param user: Username
    :type user: str
    :param geo_shape: A new GeoShapeto be created
    :type geo_shape: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        geo_shape = GeoShape.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=geo_shape,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)
