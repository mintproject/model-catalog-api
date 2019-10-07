import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import EMULATOR_TYPE_NAME, EMULATOR_TYPE_URI

from openapi_server.models.emulator import Emulator  # noqa: E501
from openapi_server import util

def emulators_get(username=None, query_text=None):  # noqa: E501
    """List all Emulator entities

    Gets a list of all Emulator entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[Emulator]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)

def emulators_id_delete(id, user):  # noqa: E501
    """Delete a Emulator

    Delete an existing Emulator # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)

def emulators_id_get(id, username=None):  # noqa: E501
    """Get a Emulator

    Gets the details of a single instance of a Emulator # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Emulator
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)

def emulators_id_put(id, user, emulator=None):  # noqa: E501
    """Update a Emulator

    Updates an existing Emulator # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param emulator: An old Emulatorto be updated
    :type emulator: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        emulator = Emulator.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=emulator,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)

def emulators_post(user, emulator=None):  # noqa: E501
    """Create a Emulator

    Create a new instance of a Emulator # noqa: E501

    :param user: Username
    :type user: str
    :param emulator: A new Emulatorto be created
    :type emulator: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        emulator = Emulator.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=emulator,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)
