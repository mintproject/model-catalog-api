import connexion
import six

from openapi_server.models.process import Process  # noqa: E501
from openapi_server import util


def processs_get(username=None):  # noqa: E501
    """List all Process entities

    Gets a list of all Process entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[Process]
    """
    return 'do some magic!'


def processs_id_delete(id):  # noqa: E501
    """Delete a Process

    Delete an existing Process # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def processs_id_get(id, username=None):  # noqa: E501
    """Get a Process

    Gets the details of a single instance of a Process # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Process
    """
    return 'do some magic!'


def processs_id_put(id, process=None):  # noqa: E501
    """Update a Process

    Updates an existing Process # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param process: An old Processto be updated
    :type process: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        process = Process.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def processs_post(process=None):  # noqa: E501
    """Create a Process

    Create a new instance of a Process # noqa: E501

    :param process: A new Processto be created
    :type process: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        process = Process.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
