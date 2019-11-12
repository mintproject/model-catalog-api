import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import NUMERICALINDEX_TYPE_NAME, NUMERICALINDEX_TYPE_URI

from openapi_server.models.numerical_index import NumericalIndex  # noqa: E501
from openapi_server import util

def numericalindexs_get(username=None, label=None):  # noqa: E501
    """List all NumericalIndex entities

    Gets a list of all NumericalIndex entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[NumericalIndex]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)

def numericalindexs_id_delete(id, user):  # noqa: E501
    """Delete a NumericalIndex

    Delete an existing NumericalIndex # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)

def numericalindexs_id_get(id, username=None):  # noqa: E501
    """Get a NumericalIndex

    Gets the details of a single instance of a NumericalIndex # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: NumericalIndex
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)

def numericalindexs_id_put(id, user, numerical_index=None):  # noqa: E501
    """Update a NumericalIndex

    Updates an existing NumericalIndex # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param numerical_index: An old NumericalIndexto be updated
    :type numerical_index: dict | bytes

    :rtype: NumericalIndex
    """

    if connexion.request.is_json:
        numerical_index = NumericalIndex.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=numerical_index,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)

def numericalindexs_post(user, numerical_index=None):  # noqa: E501
    """Create a NumericalIndex

    Create a new instance of a NumericalIndex # noqa: E501

    :param user: Username
    :type user: str
    :param numerical_index: A new NumericalIndexto be created
    :type numerical_index: dict | bytes

    :rtype: NumericalIndex
    """

    if connexion.request.is_json:
        numerical_index = NumericalIndex.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=numerical_index,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)
