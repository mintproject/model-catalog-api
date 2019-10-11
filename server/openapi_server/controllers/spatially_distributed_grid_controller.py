import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, SPATIALLYDISTRIBUTEDGRID_TYPE_URI

from openapi_server.models.spatially_distributed_grid import SpatiallyDistributedGrid  # noqa: E501
from openapi_server import util

def spatiallydistributedgrids_get(username=None, label=None):  # noqa: E501
    """List all SpatiallyDistributedGrid entities

    Gets a list of all SpatiallyDistributedGrid entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[SpatiallyDistributedGrid]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)

def spatiallydistributedgrids_id_delete(id, user):  # noqa: E501
    """Delete a SpatiallyDistributedGrid

    Delete an existing SpatiallyDistributedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)

def spatiallydistributedgrids_id_get(id, username=None):  # noqa: E501
    """Get a SpatiallyDistributedGrid

    Gets the details of a single instance of a SpatiallyDistributedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SpatiallyDistributedGrid
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)

def spatiallydistributedgrids_id_put(id, user, spatially_distributed_grid=None):  # noqa: E501
    """Update a SpatiallyDistributedGrid

    Updates an existing SpatiallyDistributedGrid # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param spatially_distributed_grid: An old SpatiallyDistributedGridto be updated
    :type spatially_distributed_grid: dict | bytes

    :rtype: SpatiallyDistributedGrid
    """

    if connexion.request.is_json:
        spatially_distributed_grid = SpatiallyDistributedGrid.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=spatially_distributed_grid,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)

def spatiallydistributedgrids_post(user, spatially_distributed_grid=None):  # noqa: E501
    """Create a SpatiallyDistributedGrid

    Create a new instance of a SpatiallyDistributedGrid # noqa: E501

    :param user: Username
    :type user: str
    :param spatially_distributed_grid: A new SpatiallyDistributedGridto be created
    :type spatially_distributed_grid: dict | bytes

    :rtype: SpatiallyDistributedGrid
    """

    if connexion.request.is_json:
        spatially_distributed_grid = SpatiallyDistributedGrid.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=spatially_distributed_grid,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)
