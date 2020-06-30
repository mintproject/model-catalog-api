import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import DATATRANSFORMATION_TYPE_NAME, DATATRANSFORMATION_TYPE_URI

from openapi_server.models.data_transformation import DataTransformation  # noqa: E501
from openapi_server import util

def datatransformations_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of DataTransformation

    Gets a list of all instances of DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[DataTransformation]
    """


    return get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation)

def datatransformations_id_delete(id, user):  # noqa: E501
    """Delete an existing DataTransformation

    Delete an existing DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation) # noqa: E501

    :param id: The ID of the DataTransformation to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation)

def datatransformations_id_get(id, username=None):  # noqa: E501
    """Get a single DataTransformation by its id

    Gets the details of a given DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation) # noqa: E501

    :param id: The ID of the DataTransformation to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: DataTransformation
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation)

def datatransformations_id_put(id, user, data_transformation=None):  # noqa: E501
    """Update an existing DataTransformation

    Updates an existing DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation) # noqa: E501

    :param id: The ID of the DataTransformation to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param data_transformation: An old DataTransformationto be updated
    :type data_transformation: dict | bytes

    :rtype: DataTransformation
    """

    if connexion.request.is_json:
        data_transformation = DataTransformation.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=data_transformation,
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation)

def datatransformations_post(user, data_transformation=None):  # noqa: E501
    """Create one DataTransformation

    Create a new instance of DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation) # noqa: E501

    :param user: Username
    :type user: str
    :param data_transformation: Information about the DataTransformationto be created
    :type data_transformation: dict | bytes

    :rtype: DataTransformation
    """

    if connexion.request.is_json:
        data_transformation = DataTransformation.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=data_transformation,
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation)
