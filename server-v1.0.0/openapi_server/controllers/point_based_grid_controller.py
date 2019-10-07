import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import POINTBASEDGRID_TYPE_NAME, POINTBASEDGRID_TYPE_URI

from openapi_server.models.point_based_grid import PointBasedGrid  # noqa: E501
from openapi_server import util

def pointbasedgrids_get(username=None, query_text=None):  # noqa: E501
    """List all PointBasedGrid entities

    Gets a list of all PointBasedGrid entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[PointBasedGrid]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)

def pointbasedgrids_id_delete(id, user):  # noqa: E501
    """Delete a PointBasedGrid

    Delete an existing PointBasedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)

def pointbasedgrids_id_get(id, username=None):  # noqa: E501
    """Get a PointBasedGrid

    Gets the details of a single instance of a PointBasedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: PointBasedGrid
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)

def pointbasedgrids_id_put(id, user, point_based_grid=None):  # noqa: E501
    """Update a PointBasedGrid

    Updates an existing PointBasedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param point_based_grid: An old PointBasedGridto be updated
    :type point_based_grid: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        point_based_grid = PointBasedGrid.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=point_based_grid,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)

def pointbasedgrids_post(user, point_based_grid=None):  # noqa: E501
    """Create a PointBasedGrid

    Create a new instance of a PointBasedGrid # noqa: E501

    :param user: Username
    :type user: str
    :param point_based_grid: A new PointBasedGridto be created
    :type point_based_grid: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        point_based_grid = PointBasedGrid.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=point_based_grid,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)
