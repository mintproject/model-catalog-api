import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import MODELCONFIGURATION_TYPE_NAME, MODELCONFIGURATION_TYPE_URI

from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501
from openapi_server import util

def custom_modelconfigurations_id_get(id, username=None, custom_query_name=None):  # noqa: E501
    """Get a ModelConfiguration

    Gets the details of a single instance of a ModelConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str
    :param custom_query_name: Name of the custom query
    :type custom_query_name: str

    :rtype: ModelConfiguration
    """


    return get_resource(id=id,
        username=username,
        custom_query_name=custom_query_name,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_get(username=None, label=None):  # noqa: E501
    """List all ModelConfiguration entities

    Gets a list of all ModelConfiguration entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[ModelConfiguration]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_id_delete(id, user):  # noqa: E501
    """Delete a ModelConfiguration

    Delete an existing ModelConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_id_get(id, username=None):  # noqa: E501
    """Get a ModelConfiguration

    Gets the details of a single instance of a ModelConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: ModelConfiguration
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_id_put(id, user, model_configuration=None):  # noqa: E501
    """Update a ModelConfiguration

    Updates an existing ModelConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param model_configuration: An old ModelConfigurationto be updated
    :type model_configuration: dict | bytes

    :rtype: ModelConfiguration
    """

    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=model_configuration,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_post(user, model_configuration=None):  # noqa: E501
    """Create a ModelConfiguration

    Create a new instance of a ModelConfiguration # noqa: E501

    :param user: Username
    :type user: str
    :param model_configuration: A new ModelConfigurationto be created
    :type model_configuration: dict | bytes

    :rtype: ModelConfiguration
    """

    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=model_configuration,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)
