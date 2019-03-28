import connexion

from openapi_server.models.data_set import DataSet  # noqa: E501
from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501
from openapi_server.models.parameter import Parameter  # noqa: E501
from endpoint.utils import insert_query
from openapi_server.static import DEFAULT_ENDPOINT
from flask import json



def add_inputs_by_modelconfiguration(name, data_set):  # noqa: E501
    """Creates a new instance of a &#x60;Dataset&#x60; related as Input.

     # noqa: E501

    :param name:
    :type name: str
    :param data_set:
    :type data_set: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_set = [DataSet.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def add_model_configuration():  # noqa: E501
    """Create a model configuration

     # noqa: E501

    :param model_configuration:
    :type model_configuration: dict | bytes

    :rtype: None
    """
    endpoint = "http://ontosoft.isi.edu:3030/test/update"
    graph = "http://example/mosorio"

    if connexion.request.is_json:
        jsonld_str = json.dumps(connexion.request.get_json())
        #TODO: validate triples
        insert_query(DEFAULT_ENDPOINT, jsonld_str, graph)

    return 'do some magic!'


def add_parameters_by_modelconfiguration(name, parameter):  # noqa: E501
    """Create the inputs of a model configuration

    Creates a new instance of a &#x60;Dataset&#x60; and it related with the &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param name:
    :type name: str
    :param parameter:
    :type parameter: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        parameter = [Parameter.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_model_configuration(name):  # noqa: E501
    """Delete a ModelConfiguration

    Deletes an existing &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param name: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def get_inputs_by_modelconfiguration(name):  # noqa: E501
    """Get the inputs of a model configuration

     # noqa: E501

    :param name: The name of the resource
    :type name: str

    :rtype: List[ApiResponse]
    """
    return 'do some magic!'


def get_model_configuraton_by_uri(name):  # noqa: E501
    """Get modelconfiguration by uri

    Gets the details of a single instance of a &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param name: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type name: str

    :rtype: ModelConfiguration
    """
    return 'do some magic!'


def get_outputs_by_modelconfiguration(name):  # noqa: E501
    """Get the outputs of a model configuration

     # noqa: E501

    :param name: The name of the resource
    :type name: str

    :rtype: List[ApiResponse]
    """
    return 'do some magic!'


def get_parameters_by_modelconfiguration(name):  # noqa: E501
    """Get the parameters of a model configuration

     # noqa: E501

    :param name: The name of the resource
    :type name: str

    :rtype: List[ApiResponse]
    """
    return 'do some magic!'


def list_model_configurations():  # noqa: E501
    """List modelconfiguration

     # noqa: E501


    :rtype: List[ModelConfiguration]
    """
    return 'do some magic!'


def modelconfiguration_name_outputs_post(name, data_set):  # noqa: E501
    """Create the output of a model configuration

     # noqa: E501

    :param name:
    :type name: str
    :param data_set:
    :type data_set: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_set = [DataSet.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def update_model_configuration(name, model_configuration):  # noqa: E501
    """Update model configuration

     # noqa: E501

    :param name: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type name: str
    :param model_configuration:
    :type model_configuration: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
