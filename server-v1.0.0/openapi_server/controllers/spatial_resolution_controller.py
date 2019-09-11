import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SPATIALRESOLUTION_TYPE_NAME, SPATIALRESOLUTION_TYPE_URI

from openapi_server.models.spatial_resolution import SpatialResolution  # noqa: E501
from openapi_server import util

def spatialresolutions_get(username=None):  # noqa: E501
    """List all SpatialResolution entities

    Gets a list of all SpatialResolution entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[SpatialResolution]
    """


    return get_resource(
        username=username,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)

def spatialresolutions_id_delete(id, user):  # noqa: E501
    """Delete a SpatialResolution

    Delete an existing SpatialResolution # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)

def spatialresolutions_id_get(id, username=None):  # noqa: E501
    """Get a SpatialResolution

    Gets the details of a single instance of a SpatialResolution # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SpatialResolution
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)

def spatialresolutions_id_put(id, user, spatial_resolution=None):  # noqa: E501
    """Update a SpatialResolution

    Updates an existing SpatialResolution # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param spatial_resolution: An old SpatialResolutionto be updated
    :type spatial_resolution: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        spatial_resolution = SpatialResolution.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=spatial_resolution,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)

def spatialresolutions_post(user, spatial_resolution=None):  # noqa: E501
    """Create a SpatialResolution

    Create a new instance of a SpatialResolution # noqa: E501

    :param user: Username
    :type user: str
    :param spatial_resolution: A new SpatialResolutionto be created
    :type spatial_resolution: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        spatial_resolution = SpatialResolution.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=spatial_resolution,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)
