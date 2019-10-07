# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.grid import Grid  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGridController(BaseTestCase):
    """GridController integration test stubs"""

    def test_grids_get(self):
        """Test case for grids_get

        List all Grid entities
        """
        query_string = [('username', 'username_example'),
                        ('query_text', 'query_text_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/grids',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_grids_id_delete(self):
        """Test case for grids_id_delete

        Delete a Grid
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/grids/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_grids_id_get(self):
        """Test case for grids_id_get

        Get a Grid
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/grids/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_grids_id_put(self):
        """Test case for grids_id_put

        Update a Grid
        """
        grid = {
  "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
  "hasFormat" : [ "hasFormat", "hasFormat" ],
  "hasFileStructure" : "{}",
  "hasPresentation" : [ "{}", "{}" ],
  "label" : "label",
  "type" : [ "type", "type" ],
  "hasFixedResource" : [ "{}", "{}" ],
  "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
  "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
  "hasShape" : [ "hasShape", "hasShape" ],
  "hasDimension" : [ "hasDimension", "hasDimension" ],
  "position" : [ 6.027456183070403, 6.027456183070403 ],
  "id" : "id"
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/grids/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_grids_post(self):
        """Test case for grids_post

        Create a Grid
        """
        grid = {
  "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
  "hasFormat" : [ "hasFormat", "hasFormat" ],
  "hasFileStructure" : "{}",
  "hasPresentation" : [ "{}", "{}" ],
  "label" : "label",
  "type" : [ "type", "type" ],
  "hasFixedResource" : [ "{}", "{}" ],
  "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
  "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
  "hasShape" : [ "hasShape", "hasShape" ],
  "hasDimension" : [ "hasDimension", "hasDimension" ],
  "position" : [ 6.027456183070403, 6.027456183070403 ],
  "id" : "id"
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/grids'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
