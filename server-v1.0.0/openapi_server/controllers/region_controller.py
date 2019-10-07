import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import REGION_TYPE_NAME, REGION_TYPE_URI

from openapi_server.models.region import Region  # noqa: E501
from openapi_server import util

def regions_get(username=None, query_text=None):  # noqa: E501
    """List all Region entities

    Gets a list of all Region entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[Region]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)

def regions_id_delete(id, user):  # noqa: E501
    """Delete a Region

    Delete an existing Region # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)

def regions_id_get(id, username=None):  # noqa: E501
    """Get a Region

    Gets the details of a single instance of a Region # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Region
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)

def regions_id_put(id, user, region=None):  # noqa: E501
    """Update a Region

    Updates an existing Region # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param region: An old Regionto be updated
    :type region: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        region = Region.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=region,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)

def regions_post(user, region=None):  # noqa: E501
    """Create a Region

    Create a new instance of a Region # noqa: E501

    :param user: Username
    :type user: str
    :param region: A new Regionto be created
    :type region: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        region = Region.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=region,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)
