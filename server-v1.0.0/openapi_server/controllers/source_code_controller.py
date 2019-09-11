import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SOURCECODE_TYPE_NAME, SOURCECODE_TYPE_URI

from openapi_server.models.source_code import SourceCode  # noqa: E501
from openapi_server import util

def sourcecodes_get(username=None):  # noqa: E501
    """List all SourceCode entities

    Gets a list of all SourceCode entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[SourceCode]
    """


    return get_resource(
        username=username,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)

def sourcecodes_id_delete(id, user):  # noqa: E501
    """Delete a SourceCode

    Delete an existing SourceCode # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)

def sourcecodes_id_get(id, username=None):  # noqa: E501
    """Get a SourceCode

    Gets the details of a single instance of a SourceCode # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SourceCode
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)

def sourcecodes_id_put(id, user, source_code=None):  # noqa: E501
    """Update a SourceCode

    Updates an existing SourceCode # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param source_code: An old SourceCodeto be updated
    :type source_code: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        source_code = SourceCode.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=source_code,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)

def sourcecodes_post(user, source_code=None):  # noqa: E501
    """Create a SourceCode

    Create a new instance of a SourceCode # noqa: E501

    :param user: Username
    :type user: str
    :param source_code: A new SourceCodeto be created
    :type source_code: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        source_code = SourceCode.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=source_code,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)
