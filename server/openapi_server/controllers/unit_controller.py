import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import UNIT_TYPE_NAME, UNIT_TYPE_URI

from openapi_server.models.unit import Unit  # noqa: E501
from openapi_server import util

def units_get(username=None, label=None):  # noqa: E501
    """List all Unit entities

    Gets a list of all Unit entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Unit]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)

def units_id_delete(id, user):  # noqa: E501
    """Delete a Unit

    Delete an existing Unit # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)

def units_id_get(id, username=None):  # noqa: E501
    """Get a Unit

    Gets the details of a single instance of a Unit # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Unit
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)

def units_id_put(id, user, unit=None):  # noqa: E501
    """Update a Unit

    Updates an existing Unit # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param unit: An old Unitto be updated
    :type unit: dict | bytes

    :rtype: Unit
    """

    if connexion.request.is_json:
        unit = Unit.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=unit,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)

def units_post(user, unit=None):  # noqa: E501
    """Create a Unit

    Create a new instance of a Unit # noqa: E501

    :param user: Username
    :type user: str
    :param unit: A new Unitto be created
    :type unit: dict | bytes

    :rtype: Unit
    """

    if connexion.request.is_json:
        unit = Unit.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=unit,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)
