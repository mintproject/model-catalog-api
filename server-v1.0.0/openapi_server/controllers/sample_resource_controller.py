import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SAMPLERESOURCE_TYPE_NAME, SAMPLERESOURCE_TYPE_URI

from openapi_server.models.sample_resource import SampleResource  # noqa: E501
from openapi_server import util

def sampleresources_get(username=None, query_text=None):  # noqa: E501
    """List all SampleResource entities

    Gets a list of all SampleResource entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[SampleResource]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)

def sampleresources_id_delete(id, user):  # noqa: E501
    """Delete a SampleResource

    Delete an existing SampleResource # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)

def sampleresources_id_get(id, username=None):  # noqa: E501
    """Get a SampleResource

    Gets the details of a single instance of a SampleResource # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SampleResource
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)

def sampleresources_id_put(id, user, sample_resource=None):  # noqa: E501
    """Update a SampleResource

    Updates an existing SampleResource # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param sample_resource: An old SampleResourceto be updated
    :type sample_resource: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        sample_resource = SampleResource.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=sample_resource,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)

def sampleresources_post(user, sample_resource=None):  # noqa: E501
    """Create a SampleResource

    Create a new instance of a SampleResource # noqa: E501

    :param user: Username
    :type user: str
    :param sample_resource: A new SampleResourceto be created
    :type sample_resource: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        sample_resource = SampleResource.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=sample_resource,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)
