import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SAMPLECOLLECTION_TYPE_NAME, SAMPLECOLLECTION_TYPE_URI

from openapi_server.models.sample_collection import SampleCollection  # noqa: E501
from openapi_server import util

def samplecollections_get(username=None, label=None):  # noqa: E501
    """List all SampleCollection entities

    Gets a list of all SampleCollection entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[SampleCollection]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)

def samplecollections_id_delete(id, user):  # noqa: E501
    """Delete a SampleCollection

    Delete an existing SampleCollection # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)

def samplecollections_id_get(id, username=None):  # noqa: E501
    """Get a SampleCollection

    Gets the details of a single instance of a SampleCollection # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SampleCollection
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)

def samplecollections_id_put(id, user, sample_collection=None):  # noqa: E501
    """Update a SampleCollection

    Updates an existing SampleCollection # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param sample_collection: An old SampleCollectionto be updated
    :type sample_collection: dict | bytes

    :rtype: SampleCollection
    """

    if connexion.request.is_json:
        sample_collection = SampleCollection.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=sample_collection,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)

def samplecollections_post(user, sample_collection=None):  # noqa: E501
    """Create a SampleCollection

    Create a new instance of a SampleCollection # noqa: E501

    :param user: Username
    :type user: str
    :param sample_collection: A new SampleCollectionto be created
    :type sample_collection: dict | bytes

    :rtype: SampleCollection
    """

    if connexion.request.is_json:
        sample_collection = SampleCollection.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=sample_collection,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)
