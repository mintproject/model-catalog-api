import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import INDEX_TYPE_NAME, INDEX_TYPE_URI

from openapi_server.models.index import Index  # noqa: E501
from openapi_server import util

def indexs_get(username=None, label=None):  # noqa: E501
    """List all Index entities

    Gets a list of all Index entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Index]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=INDEX_TYPE_URI,
        rdf_type_name=INDEX_TYPE_NAME, 
        kls=Index)

def indexs_id_delete(id, user):  # noqa: E501
    """Delete a Index

    Delete an existing Index # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=INDEX_TYPE_URI,
        rdf_type_name=INDEX_TYPE_NAME, 
        kls=Index)

def indexs_id_get(id, username=None):  # noqa: E501
    """Get a Index

    Gets the details of a single instance of a Index # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Index
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=INDEX_TYPE_URI,
        rdf_type_name=INDEX_TYPE_NAME, 
        kls=Index)

def indexs_id_put(id, user, index=None):  # noqa: E501
    """Update a Index

    Updates an existing Index # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param index: An old Indexto be updated
    :type index: dict | bytes

    :rtype: Index
    """

    if connexion.request.is_json:
        index = Index.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=index,
        rdf_type_uri=INDEX_TYPE_URI,
        rdf_type_name=INDEX_TYPE_NAME, 
        kls=Index)

def indexs_post(user, index=None):  # noqa: E501
    """Create a Index

    Create a new instance of a Index # noqa: E501

    :param user: Username
    :type user: str
    :param index: A new Indexto be created
    :type index: dict | bytes

    :rtype: Index
    """

    if connexion.request.is_json:
        index = Index.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=index,
        rdf_type_uri=INDEX_TYPE_URI,
        rdf_type_name=INDEX_TYPE_NAME, 
        kls=Index)
