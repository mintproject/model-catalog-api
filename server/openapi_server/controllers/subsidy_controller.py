import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SUBSIDY_TYPE_NAME, SUBSIDY_TYPE_URI

from openapi_server.models.subsidy import Subsidy  # noqa: E501
from openapi_server import util

def subsidys_get(username=None, label=None):  # noqa: E501
    """List all Subsidy entities

    Gets a list of all Subsidy entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Subsidy]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)

def subsidys_id_delete(id, user):  # noqa: E501
    """Delete a Subsidy

    Delete an existing Subsidy # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)

def subsidys_id_get(id, username=None):  # noqa: E501
    """Get a Subsidy

    Gets the details of a single instance of a Subsidy # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Subsidy
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)

def subsidys_id_put(id, user, subsidy=None):  # noqa: E501
    """Update a Subsidy

    Updates an existing Subsidy # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param subsidy: An old Subsidyto be updated
    :type subsidy: dict | bytes

    :rtype: Subsidy
    """

    if connexion.request.is_json:
        subsidy = Subsidy.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=subsidy,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)

def subsidys_post(user, subsidy=None):  # noqa: E501
    """Create a Subsidy

    Create a new instance of a Subsidy # noqa: E501

    :param user: Username
    :type user: str
    :param subsidy: A new Subsidyto be created
    :type subsidy: dict | bytes

    :rtype: Subsidy
    """

    if connexion.request.is_json:
        subsidy = Subsidy.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=subsidy,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)
