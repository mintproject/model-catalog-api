import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SOFTWARECONFIGURATION_TYPE_NAME, SOFTWARECONFIGURATION_TYPE_URI

from openapi_server.models.software_configuration import SoftwareConfiguration  # noqa: E501
from openapi_server import util

def softwareconfigurations_get(username=None):  # noqa: E501
    """List all SoftwareConfiguration entities

    Gets a list of all SoftwareConfiguration entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[SoftwareConfiguration]
    """


    return get_resource(
        username=username,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)

def softwareconfigurations_id_delete(id, user):  # noqa: E501
    """Delete a SoftwareConfiguration

    Delete an existing SoftwareConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)

def softwareconfigurations_id_get(id, username=None):  # noqa: E501
    """Get a SoftwareConfiguration

    Gets the details of a single instance of a SoftwareConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SoftwareConfiguration
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)

def softwareconfigurations_id_put(id, user, software_configuration=None):  # noqa: E501
    """Update a SoftwareConfiguration

    Updates an existing SoftwareConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param software_configuration: An old SoftwareConfigurationto be updated
    :type software_configuration: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        software_configuration = SoftwareConfiguration.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=software_configuration,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)

def softwareconfigurations_post(user, software_configuration=None):  # noqa: E501
    """Create a SoftwareConfiguration

    Create a new instance of a SoftwareConfiguration # noqa: E501

    :param user: Username
    :type user: str
    :param software_configuration: A new SoftwareConfigurationto be created
    :type software_configuration: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        software_configuration = SoftwareConfiguration.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=software_configuration,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)
