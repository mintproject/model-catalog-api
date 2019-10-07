import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SOFTWARE_TYPE_NAME, SOFTWARE_TYPE_URI

from openapi_server.models.software import Software  # noqa: E501
from openapi_server import util

def softwares_get(username=None, query_text=None):  # noqa: E501
    """List all Software entities

    Gets a list of all Software entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[Software]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)

def softwares_id_delete(id, user):  # noqa: E501
    """Delete a Software

    Delete an existing Software # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)

def softwares_id_get(id, username=None):  # noqa: E501
    """Get a Software

    Gets the details of a single instance of a Software # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Software
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)

def softwares_id_put(id, user, software=None):  # noqa: E501
    """Update a Software

    Updates an existing Software # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param software: An old Softwareto be updated
    :type software: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        software = Software.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=software,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)

def softwares_post(user, software=None):  # noqa: E501
    """Create a Software

    Create a new instance of a Software # noqa: E501

    :param user: Username
    :type user: str
    :param software: A new Softwareto be created
    :type software: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        software = Software.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=software,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)
