import connexion
from flask import json

from openapi_server.models.dataset_specification import DatasetSpecification  # noqa: E501

from openapi_server.models.parameter import Parameter  # noqa: E501

from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501

from endpoint.utils import insert_query, prepare_jsonld, get_all_resource, get_resource, get_all_resources_related, delete_query
from openapi_server.static_vars import *


#todo: implement create_inputs_by_modelconfiguration
def create_inputs_by_modelconfiguration(id, dataset_specification):  # noqa: E501
    """Creates a new instance of a &#x60;DatasetSpecification&#x60; related as Input.

     # noqa: E501

    :param id:
    :type id: str
    :param dataset_specification:
    :type dataset_specification: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dataset_specification = [DatasetSpecification.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return "Not Implemented", 501, {}


def create_model_configuration(user):  # noqa: E501
    """Create a model configuration

     # noqa: E501

    :param model_configuration:
    :type model_configuration: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
        if model_configuration.type:
            model_configuration.type.append(MODELCONFIGURATION_TYPE)
        else:
            model_configuration.type = [MODELCONFIGURATION_TYPE]
        model_configuration_json = prepare_jsonld(model_configuration, user)
        return insert_query(model_configuration_json, user)

    return "Bad request", 400, {}

#todo: implement create_parameters_by_modelconfiguration
def create_parameters_by_modelconfiguration(id, parameter):  # noqa: E501
    """Create the inputs of a model configuration

    Creates a new instance of a &#x60;DatasetSpecification&#x60; and it related with the &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param id:
    :type id: str
    :param parameter:
    :type parameter: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        parameter = [Parameter.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return "Not Implemented", 501, {}


def delete_model_configuration(id, user):  # noqa: E501
    """Delete a ModelConfiguration

    Deletes an existing &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type id: str

    :rtype: None
    """
    try:
        return delete_query(id, user)
    except:
        return "Bad request", 400, {}


def get_inputs_by_modelconfiguration(id, username=None):  # noqa: E501
    """Get the inputs of a model configuration

     # noqa: E501

    :param id: The name of the resource
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[DatasetSpecification]
    """
    try:
        response = get_all_resources_related(id, HAS_INPUT, DATASETSPECIFICATION_TYPE, username)
    except:
        return "Bad request", 400, {}
    data_sets = []
    for d in response:
        data_sets.append(DatasetSpecification.from_dict(d))

    return data_sets

def get_model_configurations(username=None):  # noqa: E501
    """List modelconfiguration

     # noqa: E501

    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[ModelConfiguration]
    """

    model_configuration = ModelConfiguration()
    try:
        response = get_all_resource(MODELCONFIGURATION_TYPE, username)
    except:
        return "Bad request", 400, {}

    model_configurations = []
    for d in response:
        m = ModelConfiguration.from_dict(d)
        model_configurations.append(m)
    return model_configurations



def get_model_configuration(id, username=None):  # noqa: E501
    """Get modelconfiguration

    Gets the details of a single instance of a &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: ModelConfiguration
    """
    model_configuration = ModelConfiguration()
    try:
        response = get_resource(id, MODELCONFIGURATION_TYPE, username)
    except:
        return "Bad request", 400, {}
    if response:
        model_configuration = ModelConfiguration.from_dict(response[0])
    else:
        return "Not found", 404, {}
    return model_configuration



def get_outputs_by_modelconfiguration(id, username=None):  # noqa: E501
    """Get the outputs of a model configuration

     # noqa: E501

    :param id: The name of the resource
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[DatasetSpecification]
    """
    try:
        response = get_all_resources_related(id, HAS_OUTPUT, DATASETSPECIFICATION_TYPE, username)
    except:
        return "Bad request", 400, {}
    data_sets = []
    for d in response:
        data_sets.append(DatasetSpecification.from_dict(d))

    return data_sets



def get_parameters_by_modelconfiguration(id, username=None):  # noqa: E501
    """Get the parameters of a model configuration

     # noqa: E501

    :param id: The name of the resource
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[Parameter]
    """
    try:
        response = get_all_resources_related(id, HAS_PARAMETER, PARAMETER_TYPE, username)
    except:
        return "Bad request", 400, {}
    parameters = []
    for d in response:
        parameters.append(Parameter.from_dict(d))
    return parameters


#todo: implement create_outputs_by_modelconfiguration
def create_outputs_by_modelconfiguration(id, dataset_specification):  # noqa: E501
    """Create the output of a model configuration

     # noqa: E501

    :param id:
    :type id: str
    :param dataset_specification:
    :type dataset_specification: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dataset_specification = [DatasetSpecification.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


#todo: implement update_model_configuration
def update_model_configuration(id, user):  # noqa: E501
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
        if model_configuration.type:
            model_configuration.type.append(MODELCONFIGURATION_TYPE)
        else:
            model_configuration.type = [MODELCONFIGURATION_TYPE]
        model_configuration_json = prepare_jsonld(model_configuration, user)
        delete_query(id, user);
        return insert_query(model_configuration_json, user)
    return "Bad request", 400, {}
