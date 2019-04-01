import connexion

from openapi_server.models.data_set import DataSet  # noqa: E501

from openapi_server.models.parameter import Parameter  # noqa: E501


from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501
import openapi_server.controllers.dataset_controller as DataSetController
import openapi_server.controllers.cag_controller as CagController
import openapi_server.controllers.process_controller as ProcessController
import openapi_server.controllers.time_interval_controller as TimeIntervalController
import openapi_server.controllers.parameter_controller as ParameterController
import openapi_server.static_vars as StaticVars


def add_inputs_by_modelconfiguration(id, data_set):  # noqa: E501
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
    return 'do some magic!'


def add_model_configuration():  # noqa: E501
    """Create a model configuration

     # noqa: E501

    :param model_configuration:
    :type model_configuration: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
        prepare_jsonld(connexion.request.get_json())
    return 'do some magic!'


def add_parameters_by_modelconfiguration(id, parameter):  # noqa: E501
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
    return 'do some magic!'


def delete_model_configuration(id):  # noqa: E501
    """Delete a ModelConfiguration

    Deletes an existing &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_inputs_by_modelconfiguration(id):  # noqa: E501
    """Get the inputs of a model configuration

     # noqa: E501

    :param id: The name of the resource
    :type id: str

    :rtype: List[ApiResponse]
    """
    return 'do some magic!'


def get_model_configuraton_by_uri(id):  # noqa: E501
    """Get modelconfiguration by uri

    Gets the details of a single instance of a &#x60;ModelConfiguration&#x60;. # noqa: E501

    :param id: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type id: str

    :rtype: ModelConfiguration
    """
    return 'do some magic!'


def get_outputs_by_modelconfiguration(id):  # noqa: E501
    """Get the outputs of a model configuration

     # noqa: E501

    :param id: The name of the resource
    :type id: str

    :rtype: List[ApiResponse]
    """
    return 'do some magic!'


def get_parameters_by_modelconfiguration(id):  # noqa: E501
    """Get the parameters of a model configuration

     # noqa: E501

    :param id: The name of the resource
    :type id: str

    :rtype: List[ApiResponse]
    """
    return 'do some magic!'


def list_model_configurations():  # noqa: E501
    """List modelconfiguration

     # noqa: E501


    :rtype: List[ModelConfiguration]
    """
    return 'do some magic!'


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
    return 'do some magic!'


def update_model_configuration(id, name, model_configuration):  # noqa: E501
    """Update model configuration

     # noqa: E501

    :param id: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type id: str
    :param name: A unique identifier for a &#x60;ModelConfiguration&#x60;.
    :type name: str
    :param model_configuration:
    :type model_configuration: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def obtain_uri(id):
    #todo: magic
    return StaticVars.DEFAULT_MINT_INSTANCE + 'id'


def prepare_jsonld(modelconfig):

    modelconfig['@context'] = StaticVars.MINT_CONTEXT
    modelconfig['@uri'] = obtain_uri(modelconfig['id'])
    modelconfig['@type'] = StaticVars.MODELCONFIGURATION_TYPE

    if 'inputs' in modelconfig:
        for item in modelconfig['inputs']:
            DataSetController.obtain_uri(item['id'])

    if 'outputs' in modelconfig:
        for item in modelconfig['outputs']:
            DataSetController.obtain_uri(item['id'])

    if 'process' in modelconfig:
        for process in modelconfig['process']:
            ProcessController.obtain_uri(process['id'])

    if 'cag' in modelconfig:
        for cag in modelconfig['cag']:
            CagController.obtain_uri(cag['id'])

    if 'interval_time' in modelconfig:
        for interval_time in modelconfig['interval_time']:
            TimeIntervalController.obtain_uri(interval_time['id'])

    if 'parameters' in modelconfig:
        for parameter in modelconfig['parameters']:
            ParameterController.obtain_uri(parameter['id'])

