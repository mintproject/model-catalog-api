import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import GRID_TYPE_NAME, GRID_TYPE_URI

from openapi_server.models.grid import Grid  # noqa: E501
from openapi_server import util

def grids_get(username=None, label=None):  # noqa: E501
    """List all Grid entities

    Gets a list of all Grid entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Grid]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)

def grids_id_delete(id, user):  # noqa: E501
    """Delete a Grid

    Delete an existing Grid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)

def grids_id_get(id, username=None):  # noqa: E501
    """Get a Grid

    Gets the details of a single instance of a Grid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Grid
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)

def grids_id_put(id, user, grid=None):  # noqa: E501
    """Update a Grid

    Updates an existing Grid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param grid: An old Gridto be updated
    :type grid: dict | bytes

    :rtype: Grid
    """

    if connexion.request.is_json:
        grid = Grid.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=grid,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)

def grids_post(user, grid=None):  # noqa: E501
    """Create a Grid

    Create a new instance of a Grid # noqa: E501

    :param user: Username
    :type user: str
    :param grid: A new Gridto be created
    :type grid: dict | bytes

    :rtype: Grid
    """

    if connexion.request.is_json:
        grid = Grid.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=grid,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)
