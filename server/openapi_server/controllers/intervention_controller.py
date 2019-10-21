import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import INTERVENTION_TYPE_NAME, INTERVENTION_TYPE_URI

from openapi_server.models.intervention import Intervention  # noqa: E501
from openapi_server import util

def interventions_get(username=None, label=None):  # noqa: E501
    """List all Intervention entities

    Gets a list of all Intervention entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Intervention]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)

def interventions_id_delete(id, user):  # noqa: E501
    """Delete a Intervention

    Delete an existing Intervention # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)

def interventions_id_get(id, username=None):  # noqa: E501
    """Get a Intervention

    Gets the details of a single instance of a Intervention # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Intervention
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)

def interventions_id_put(id, user, intervention=None):  # noqa: E501
    """Update a Intervention

    Updates an existing Intervention # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param intervention: An old Interventionto be updated
    :type intervention: dict | bytes

    :rtype: Intervention
    """

    if connexion.request.is_json:
        intervention = Intervention.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=intervention,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)

def interventions_post(user, intervention=None):  # noqa: E501
    """Create a Intervention

    Create a new instance of a Intervention # noqa: E501

    :param user: Username
    :type user: str
    :param intervention: A new Interventionto be created
    :type intervention: dict | bytes

    :rtype: Intervention
    """

    if connexion.request.is_json:
        intervention = Intervention.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=intervention,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)
