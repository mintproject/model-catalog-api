import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import PROCESS_TYPE_NAME, PROCESS_TYPE_URI

from openapi_server.models.process import Process  # noqa: E501
from openapi_server import util

def processs_get(username=None, label=None):  # noqa: E501
    """List all Process entities

    Gets a list of all Process entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Process]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)

def processs_id_delete(id, user):  # noqa: E501
    """Delete a Process

    Delete an existing Process # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)

def processs_id_get(id, username=None):  # noqa: E501
    """Get a Process

    Gets the details of a single instance of a Process # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Process
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)

def processs_id_put(id, user, process=None):  # noqa: E501
    """Update a Process

    Updates an existing Process # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param process: An old Processto be updated
    :type process: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        process = Process.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=process,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)

def processs_post(user, process=None):  # noqa: E501
    """Create a Process

    Create a new instance of a Process # noqa: E501

    :param user: Username
    :type user: str
    :param process: A new Processto be created
    :type process: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        process = Process.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=process,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)
