# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.point_based_grid import PointBasedGrid  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPointBasedGridController(BaseTestCase):
    """PointBasedGridController integration test stubs"""

    def test_pointbasedgrids_get(self):
        """Test case for pointbasedgrids_get

        List all PointBasedGrid entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/pointbasedgrids',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pointbasedgrids_id_delete(self):
        """Test case for pointbasedgrids_id_delete

        Delete a PointBasedGrid
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/pointbasedgrids/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pointbasedgrids_id_get(self):
        """Test case for pointbasedgrids_id_get

        Get a PointBasedGrid
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/pointbasedgrids/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pointbasedgrids_id_put(self):
        """Test case for pointbasedgrids_id_put

        Update a PointBasedGrid
        """
        point_based_grid = {
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
            '/v1.0.0/pointbasedgrids/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(point_based_grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pointbasedgrids_post(self):
        """Test case for pointbasedgrids_post

        Create a PointBasedGrid
        """
        point_based_grid = {
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
            '/v1.0.0/pointbasedgrids'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(point_based_grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
