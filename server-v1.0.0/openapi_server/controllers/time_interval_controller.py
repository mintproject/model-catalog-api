import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import TIMEINTERVAL_TYPE_NAME, TIMEINTERVAL_TYPE_URI

from openapi_server.models.time_interval import TimeInterval  # noqa: E501
from openapi_server import util

def timeintervals_get(username=None):  # noqa: E501
    """List all TimeInterval entities

    Gets a list of all TimeInterval entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[TimeInterval]
    """


    return get_resource(
        username=username,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)

def timeintervals_id_delete(id, user):  # noqa: E501
    """Delete a TimeInterval

    Delete an existing TimeInterval # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)

def timeintervals_id_get(id, username=None):  # noqa: E501
    """Get a TimeInterval

    Gets the details of a single instance of a TimeInterval # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: TimeInterval
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)

def timeintervals_id_put(id, user, time_interval=None):  # noqa: E501
    """Update a TimeInterval

    Updates an existing TimeInterval # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param time_interval: An old TimeIntervalto be updated
    :type time_interval: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        time_interval = TimeInterval.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=time_interval,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)

def timeintervals_post(user, time_interval=None):  # noqa: E501
    """Create a TimeInterval

    Create a new instance of a TimeInterval # noqa: E501

    :param user: Username
    :type user: str
    :param time_interval: A new TimeIntervalto be created
    :type time_interval: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        time_interval = TimeInterval.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=time_interval,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)
