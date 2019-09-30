import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SOFTWAREVERSION_TYPE_NAME, SOFTWAREVERSION_TYPE_URI

from openapi_server.models.software_version import SoftwareVersion  # noqa: E501
from openapi_server import util

def softwareversions_get(username=None):  # noqa: E501
    """List all SoftwareVersion entities

    Gets a list of all SoftwareVersion entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[SoftwareVersion]
    """


    return get_resource(
        username=username,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)

def softwareversions_id_delete(id, user):  # noqa: E501
    """Delete a SoftwareVersion

    Delete an existing SoftwareVersion # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)

def softwareversions_id_get(id, username=None):  # noqa: E501
    """Get a SoftwareVersion

    Gets the details of a single instance of a SoftwareVersion # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SoftwareVersion
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)

def softwareversions_id_put(id, user, software_version=None):  # noqa: E501
    """Update a SoftwareVersion

    Updates an existing SoftwareVersion # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param software_version: An old SoftwareVersionto be updated
    :type software_version: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        software_version = SoftwareVersion.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=software_version,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)

def softwareversions_post(user, software_version=None):  # noqa: E501
    """Create a SoftwareVersion

    Create a new instance of a SoftwareVersion # noqa: E501

    :param user: Username
    :type user: str
    :param software_version: A new SoftwareVersionto be created
    :type software_version: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        software_version = SoftwareVersion.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=software_version,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)
