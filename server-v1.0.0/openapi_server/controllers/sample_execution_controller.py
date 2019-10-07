import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SAMPLEEXECUTION_TYPE_NAME, SAMPLEEXECUTION_TYPE_URI

from openapi_server.models.sample_execution import SampleExecution  # noqa: E501
from openapi_server import util

def sampleexecutions_get(username=None, query_text=None):  # noqa: E501
    """List all SampleExecution entities

    Gets a list of all SampleExecution entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[SampleExecution]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)

def sampleexecutions_id_delete(id, user):  # noqa: E501
    """Delete a SampleExecution

    Delete an existing SampleExecution # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)

def sampleexecutions_id_get(id, username=None):  # noqa: E501
    """Get a SampleExecution

    Gets the details of a single instance of a SampleExecution # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SampleExecution
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)

def sampleexecutions_id_put(id, user, sample_execution=None):  # noqa: E501
    """Update a SampleExecution

    Updates an existing SampleExecution # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param sample_execution: An old SampleExecutionto be updated
    :type sample_execution: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        sample_execution = SampleExecution.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=sample_execution,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)

def sampleexecutions_post(user, sample_execution=None):  # noqa: E501
    """Create a SampleExecution

    Create a new instance of a SampleExecution # noqa: E501

    :param user: Username
    :type user: str
    :param sample_execution: A new SampleExecutionto be created
    :type sample_execution: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        sample_execution = SampleExecution.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=sample_execution,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)
