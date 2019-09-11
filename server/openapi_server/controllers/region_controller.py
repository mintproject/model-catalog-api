import connexion
import six

from openapi_server.models.region import Region  # noqa: E501
from openapi_server import util


def regions_get(username=None):  # noqa: E501
    """List all Region entities

    Gets a list of all Region entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[Region]
    """
    return 'do some magic!'


def regions_id_delete(id):  # noqa: E501
    """Delete a Region

    Delete an existing Region # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def regions_id_get(id, username=None):  # noqa: E501
    """Get a Region

    Gets the details of a single instance of a Region # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Region
    """
    return 'do some magic!'


def regions_id_put(id, region=None):  # noqa: E501
    """Update a Region

    Updates an existing Region # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param region: An old Regionto be updated
    :type region: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        region = Region.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def regions_post(region=None):  # noqa: E501
    """Create a Region

    Create a new instance of a Region # noqa: E501

    :param region: A new Regionto be created
    :type region: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        region = Region.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
