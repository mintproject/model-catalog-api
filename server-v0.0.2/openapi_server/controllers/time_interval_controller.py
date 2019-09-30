import connexion
import six

from openapi_server.models.time_interval import TimeInterval  # noqa: E501
from openapi_server import util


def timeintervals_get(username=None):  # noqa: E501
    """List all TimeInterval entities

    Gets a list of all TimeInterval entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[TimeInterval]
    """
    return 'do some magic!'


def timeintervals_id_delete(id):  # noqa: E501
    """Delete a TimeInterval

    Delete an existing TimeInterval # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def timeintervals_id_get(id, username=None):  # noqa: E501
    """Get a TimeInterval

    Gets the details of a single instance of a TimeInterval # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: TimeInterval
    """
    return 'do some magic!'


def timeintervals_id_put(id, time_interval=None):  # noqa: E501
    """Update a TimeInterval

    Updates an existing TimeInterval # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param time_interval: An old TimeIntervalto be updated
    :type time_interval: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        time_interval = TimeInterval.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def timeintervals_post(time_interval=None):  # noqa: E501
    """Create a TimeInterval

    Create a new instance of a TimeInterval # noqa: E501

    :param time_interval: A new TimeIntervalto be created
    :type time_interval: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        time_interval = TimeInterval.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
