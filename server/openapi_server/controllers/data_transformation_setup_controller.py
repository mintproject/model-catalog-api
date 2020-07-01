import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DATATRANSFORMATIONSETUP_TYPE_NAME, DATATRANSFORMATIONSETUP_TYPE_URI

from openapi_server.models.data_transformation_setup import DataTransformationSetup  # noqa: E501
from openapi_server import util

def datatransformationsetups_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of DataTransformationSetup

    Gets a list of all instances of DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[DataTransformationSetup]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME, 
        kls=DataTransformationSetup)

def datatransformationsetups_id_delete(id, user):  # noqa: E501
    """Delete an existing DataTransformationSetup

    Delete an existing DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup) # noqa: E501

    :param id: The ID of the DataTransformationSetup to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME, 
        kls=DataTransformationSetup)

def datatransformationsetups_id_get(id, username=None):  # noqa: E501
    """Get a single DataTransformationSetup by its id

    Gets the details of a given DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup) # noqa: E501

    :param id: The ID of the DataTransformationSetup to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: DataTransformationSetup
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME, 
        kls=DataTransformationSetup)

def datatransformationsetups_id_put(id, user, data_transformation_setup=None):  # noqa: E501
    """Update an existing DataTransformationSetup

    Updates an existing DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup) # noqa: E501

    :param id: The ID of the DataTransformationSetup to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param data_transformation_setup: An old DataTransformationSetupto be updated
    :type data_transformation_setup: dict | bytes

    :rtype: DataTransformationSetup
    """

    if connexion.request.is_json:
        data_transformation_setup = DataTransformationSetup.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=data_transformation_setup,
        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME, 
        kls=DataTransformationSetup)

def datatransformationsetups_post(user, data_transformation_setup=None):  # noqa: E501
    """Create one DataTransformationSetup

    Create a new instance of DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup) # noqa: E501

    :param user: Username
    :type user: str
    :param data_transformation_setup: Information about the DataTransformationSetupto be created
    :type data_transformation_setup: dict | bytes

    :rtype: DataTransformationSetup
    """

    if connexion.request.is_json:
        data_transformation_setup = DataTransformationSetup.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=data_transformation_setup,
        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME, 
        kls=DataTransformationSetup)
