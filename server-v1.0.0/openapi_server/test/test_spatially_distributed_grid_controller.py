# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.spatially_distributed_grid import SpatiallyDistributedGrid  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSpatiallyDistributedGridController(BaseTestCase):
    """SpatiallyDistributedGridController integration test stubs"""

    def test_spatiallydistributedgrids_get(self):
        """Test case for spatiallydistributedgrids_get

        List all SpatiallyDistributedGrid entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/spatiallydistributedgrids',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spatiallydistributedgrids_id_delete(self):
        """Test case for spatiallydistributedgrids_id_delete

        Delete a SpatiallyDistributedGrid
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/spatiallydistributedgrids/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spatiallydistributedgrids_id_get(self):
        """Test case for spatiallydistributedgrids_id_get

        Get a SpatiallyDistributedGrid
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/spatiallydistributedgrids/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spatiallydistributedgrids_id_put(self):
        """Test case for spatiallydistributedgrids_id_put

        Update a SpatiallyDistributedGrid
        """
        spatially_distributed_grid = {
  "hasShape" : [ "hasShape", "hasShape" ],
  "hasDimension" : [ "hasDimension", "hasDimension" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ],
  "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
  "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/spatiallydistributedgrids/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(spatially_distributed_grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spatiallydistributedgrids_post(self):
        """Test case for spatiallydistributedgrids_post

        Create a SpatiallyDistributedGrid
        """
        spatially_distributed_grid = {
  "hasShape" : [ "hasShape", "hasShape" ],
  "hasDimension" : [ "hasDimension", "hasDimension" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ],
  "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
  "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/spatiallydistributedgrids'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(spatially_distributed_grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
