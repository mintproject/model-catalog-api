import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import VISUALIZATION_TYPE_NAME, VISUALIZATION_TYPE_URI

from openapi_server.models.visualization import Visualization  # noqa: E501
from openapi_server import util

def visualizations_get(username=None):  # noqa: E501
    """List all Visualization entities

    Gets a list of all Visualization entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[Visualization]
    """


    return get_resource(
        username=username,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)

def visualizations_id_delete(id, user):  # noqa: E501
    """Delete a Visualization

    Delete an existing Visualization # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)

def visualizations_id_get(id, username=None):  # noqa: E501
    """Get a Visualization

    Gets the details of a single instance of a Visualization # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Visualization
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)

def visualizations_id_put(id, user, visualization=None):  # noqa: E501
    """Update a Visualization

    Updates an existing Visualization # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param visualization: An old Visualizationto be updated
    :type visualization: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        visualization = Visualization.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=visualization,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)

def visualizations_post(user, visualization=None):  # noqa: E501
    """Create a Visualization

    Create a new instance of a Visualization # noqa: E501

    :param user: Username
    :type user: str
    :param visualization: A new Visualizationto be created
    :type visualization: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        visualization = Visualization.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=visualization,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)
