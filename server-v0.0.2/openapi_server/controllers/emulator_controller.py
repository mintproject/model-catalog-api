import connexion
import six

from openapi_server.models.emulator import Emulator  # noqa: E501
from openapi_server import util


def emulators_get(username=None):  # noqa: E501
    """List all Emulator entities

    Gets a list of all Emulator entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[Emulator]
    """
    return 'do some magic!'


def emulators_id_delete(id):  # noqa: E501
    """Delete a Emulator

    Delete an existing Emulator # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def emulators_id_get(id, username=None):  # noqa: E501
    """Get a Emulator

    Gets the details of a single instance of a Emulator # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Emulator
    """
    return 'do some magic!'


def emulators_id_put(id, emulator=None):  # noqa: E501
    """Update a Emulator

    Updates an existing Emulator # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param emulator: An old Emulatorto be updated
    :type emulator: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        emulator = Emulator.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def emulators_post(emulator=None):  # noqa: E501
    """Create a Emulator

    Create a new instance of a Emulator # noqa: E501

    :param emulator: A new Emulatorto be created
    :type emulator: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        emulator = Emulator.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
