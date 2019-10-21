import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import CONFIGURATIONSETUP_TYPE_NAME, CONFIGURATIONSETUP_TYPE_URI

from openapi_server.models.configuration_setup import ConfigurationSetup  # noqa: E501
from openapi_server import util

def configurationsetups_get(username=None, label=None):  # noqa: E501
    """List all ConfigurationSetup entities

    Gets a list of all ConfigurationSetup entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[ConfigurationSetup]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)

def configurationsetups_id_delete(id, user):  # noqa: E501
    """Delete a ConfigurationSetup

    Delete an existing ConfigurationSetup # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)

def configurationsetups_id_get(id, username=None):  # noqa: E501
    """Get a ConfigurationSetup

    Gets the details of a single instance of a ConfigurationSetup # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: ConfigurationSetup
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)

def configurationsetups_id_put(id, user, configuration_setup=None):  # noqa: E501
    """Update a ConfigurationSetup

    Updates an existing ConfigurationSetup # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param configuration_setup: An old ConfigurationSetupto be updated
    :type configuration_setup: dict | bytes

    :rtype: ConfigurationSetup
    """

    if connexion.request.is_json:
        configuration_setup = ConfigurationSetup.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=configuration_setup,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)

def configurationsetups_post(user, configuration_setup=None):  # noqa: E501
    """Create a ConfigurationSetup

    Create a new instance of a ConfigurationSetup # noqa: E501

    :param user: Username
    :type user: str
    :param configuration_setup: A new ConfigurationSetupto be created
    :type configuration_setup: dict | bytes

    :rtype: ConfigurationSetup
    """

    if connexion.request.is_json:
        configuration_setup = ConfigurationSetup.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=configuration_setup,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)
