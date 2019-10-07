import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import ORGANIZATION_TYPE_NAME, ORGANIZATION_TYPE_URI

from openapi_server.models.organization import Organization  # noqa: E501
from openapi_server import util

def organizations_get(username=None, query_text=None):  # noqa: E501
    """List all Organization entities

    Gets a list of all Organization entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[Organization]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)

def organizations_id_delete(id, user):  # noqa: E501
    """Delete a Organization

    Delete an existing Organization # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)

def organizations_id_get(id, username=None):  # noqa: E501
    """Get a Organization

    Gets the details of a single instance of a Organization # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Organization
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)

def organizations_id_put(id, user, organization=None):  # noqa: E501
    """Update a Organization

    Updates an existing Organization # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param organization: An old Organizationto be updated
    :type organization: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        organization = Organization.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=organization,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)

def organizations_post(user, organization=None):  # noqa: E501
    """Create a Organization

    Create a new instance of a Organization # noqa: E501

    :param user: Username
    :type user: str
    :param organization: A new Organizationto be created
    :type organization: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        organization = Organization.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=organization,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)
