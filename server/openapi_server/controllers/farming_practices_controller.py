import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import FARMINGPRACTICES_TYPE_NAME, FARMINGPRACTICES_TYPE_URI

from openapi_server.models.farming_practices import FarmingPractices  # noqa: E501
from openapi_server import util

def farmingpracticess_get(username=None, label=None):  # noqa: E501
    """List all FarmingPractices entities

    Gets a list of all FarmingPractices entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[FarmingPractices]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)

def farmingpracticess_id_delete(id, user):  # noqa: E501
    """Delete a FarmingPractices

    Delete an existing FarmingPractices # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)

def farmingpracticess_id_get(id, username=None):  # noqa: E501
    """Get a FarmingPractices

    Gets the details of a single instance of a FarmingPractices # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: FarmingPractices
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)

def farmingpracticess_id_put(id, user, farming_practices=None):  # noqa: E501
    """Update a FarmingPractices

    Updates an existing FarmingPractices # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param farming_practices: An old FarmingPracticesto be updated
    :type farming_practices: dict | bytes

    :rtype: FarmingPractices
    """

    if connexion.request.is_json:
        farming_practices = FarmingPractices.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=farming_practices,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)

def farmingpracticess_post(user, farming_practices=None):  # noqa: E501
    """Create a FarmingPractices

    Create a new instance of a FarmingPractices # noqa: E501

    :param user: Username
    :type user: str
    :param farming_practices: A new FarmingPracticesto be created
    :type farming_practices: dict | bytes

    :rtype: FarmingPractices
    """

    if connexion.request.is_json:
        farming_practices = FarmingPractices.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=farming_practices,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)
