import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import PERSON_TYPE_NAME, PERSON_TYPE_URI

from openapi_server.models.person import Person  # noqa: E501
from openapi_server import util

def persons_get(username=None, label=None):  # noqa: E501
    """List all Person entities

    Gets a list of all Person entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Person]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)

def persons_id_delete(id, user):  # noqa: E501
    """Delete a Person

    Delete an existing Person # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)

def persons_id_get(id, username=None):  # noqa: E501
    """Get a Person

    Gets the details of a single instance of a Person # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Person
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)

def persons_id_put(id, user, person=None):  # noqa: E501
    """Update a Person

    Updates an existing Person # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param person: An old Personto be updated
    :type person: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=person,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)

def persons_post(user, person=None):  # noqa: E501
    """Create a Person

    Create a new instance of a Person # noqa: E501

    :param user: Username
    :type user: str
    :param person: A new Personto be created
    :type person: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=person,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)
