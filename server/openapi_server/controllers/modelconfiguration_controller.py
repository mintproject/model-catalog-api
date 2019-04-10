import connexion
from flask import json

from openapi_server.models.data_set import DataSet  # noqa: E501

from openapi_server.models.parameter import Parameter  # noqa: E501


from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501

from endpoint.utils import insert_query, prepare_jsonld, get_all_resource, get_resource, get_all_resources_related
from openapi_server.static_vars import *

#todo: implement
def create_inputs_by_modelconfiguration(id, data_set):  # noqa: E501
    """Creates a new instance of a &#x60;Dataset&#x60; related as Input.

     # noqa: E501

    :param id:
    :type id: str
    :param data_set:
    :type data_set: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_set = [DataSet.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return "Not Implemented", 501, {}


def create_model_configuration(user):  # noqa: E501
    """Create a model configuration

     # noqa: E501

    :param model_configuration:
    :type model_configuration: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        _ = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
        model_configuration_json = prepare_jsonld(connexion.request.get_json(), user, MODELCONFIGURATION_TYPE)
        return insert_query(model_configuration_json, user)
    return "Bad request", 400, {}


#todo: implement
def create_parameters_by_modelconfiguration(id, parameter):  # noqa: E501
    """Create the inputs of a model configuration

    Creates a new instance of a &#x60;Dataset&#x60; and it related with the &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param id:
    :type id: str
    :param parameter:
    :type parameter: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        parameter = [Parameter.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return "Not Implemented", 501, {}

#todo: implement
def delete_model_configuration(id):  # noqa: E501
    """Delete a ModelConfiguration

    Deletes an existing &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type id: str

    :rtype: None
    """
    return "Not Implemented", 501, {}

#todo: implement
def get_inputs_by_modelconfiguration(id, username=None):  # noqa: E501
    """Get the inputs of a model configuration

     # noqa: E501

    :param id: The name of the resource
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[ApiResponse]
    """
    try:
        return get_all_resources_related(id, "mc:hasInput", username)
    except:
        return "Bad request", 400, {}


def get_model_configurations(username=None):  # noqa: E501
    """List modelconfiguration

     # noqa: E501

    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[ModelConfiguration]
    """
    try:
        return get_all_resource(DATASETSPECIFICATION_TYPE, username)
    except:
        return "Bad request", 400, {}

def get_model_configuration(id, username=None):
    # noqa: E501
    """Get modelconfiguration

    Gets the details of a single instance of a &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: ModelConfiguration
    """
    try:
        return get_resource(id, MODELCONFIGURATION_TYPE, username)
    except:
        return "Bad request", 400, {}


def get_outputs_by_modelconfiguration(id, username=None):  # noqa: E501
    """Get the outputs of a model configuration

     # noqa: E501

    :param id: The name of the resource
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[ApiResponse]
    """
    try:
        return get_all_resources_related(id, "mc:hasOutput", username)
    except:
        return "Bad request", 400, {}

def get_parameters_by_modelconfiguration(id, username=None):  # noqa: E501
    """Get the parameters of a model configuration

     # noqa: E501

    :param id: The name of the resource
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[ApiResponse]
    """
    try:
        return get_all_resources_related(id, "mc:hasParameter", username)
    except:
        return "Bad request", 400, {}

#todo: implement
def modelconfiguration_id_outputs_post(id, data_set):  # noqa: E501
    """Create the output of a model configuration

     # noqa: E501

    :param id:
    :type id: str
    :param data_set:
    :type data_set: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_set = [DataSet.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return "Not Implemented", 501, {}

#todo: implement
def update_model_configuration(id, model_configuration):  # noqa: E501
    """Update model configuration

     # noqa: E501

    :param id: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type id: str
    :param model_configuration:
    :type model_configuration: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
    return "Not Implemented", 501, {}
