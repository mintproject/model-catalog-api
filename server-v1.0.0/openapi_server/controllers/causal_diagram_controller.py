import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import CAUSALDIAGRAM_TYPE_NAME, CAUSALDIAGRAM_TYPE_URI

from openapi_server.models.causal_diagram import CausalDiagram  # noqa: E501
from openapi_server import util

def causaldiagrams_get(username=None, query_text=None):  # noqa: E501
    """List all CausalDiagram entities

    Gets a list of all CausalDiagram entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[CausalDiagram]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)

def causaldiagrams_id_delete(id, user):  # noqa: E501
    """Delete a CausalDiagram

    Delete an existing CausalDiagram # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)

def causaldiagrams_id_get(id, username=None):  # noqa: E501
    """Get a CausalDiagram

    Gets the details of a single instance of a CausalDiagram # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: CausalDiagram
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)

def causaldiagrams_id_put(id, user, causal_diagram=None):  # noqa: E501
    """Update a CausalDiagram

    Updates an existing CausalDiagram # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param causal_diagram: An old CausalDiagramto be updated
    :type causal_diagram: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        causal_diagram = CausalDiagram.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=causal_diagram,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)

def causaldiagrams_post(user, causal_diagram=None):  # noqa: E501
    """Create a CausalDiagram

    Create a new instance of a CausalDiagram # noqa: E501

    :param user: Username
    :type user: str
    :param causal_diagram: A new CausalDiagramto be created
    :type causal_diagram: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        causal_diagram = CausalDiagram.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=causal_diagram,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)
