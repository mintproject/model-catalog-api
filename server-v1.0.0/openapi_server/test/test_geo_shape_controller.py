# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.geo_shape import GeoShape  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGeoShapeController(BaseTestCase):
    """GeoShapeController integration test stubs"""

    def test_geoshapes_get(self):
        """Test case for geoshapes_get

        List all GeoShape entities
        """
        query_string = [('username', 'username_example'),
                        ('query_text', 'query_text_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/geoshapes',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geoshapes_id_delete(self):
        """Test case for geoshapes_id_delete

        Delete a GeoShape
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/geoshapes/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geoshapes_id_get(self):
        """Test case for geoshapes_id_get

        Get a GeoShape
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/geoshapes/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geoshapes_id_put(self):
        """Test case for geoshapes_id_put

        Update a GeoShape
        """
        geo_shape = {
  "elevation" : [ "elevation", "elevation" ],
  "latitude" : [ "latitude", "latitude" ],
  "box" : [ "box", "box" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ],
  "longitude" : [ "longitude", "longitude" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/geoshapes/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(geo_shape),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geoshapes_post(self):
        """Test case for geoshapes_post

        Create a GeoShape
        """
        geo_shape = {
  "elevation" : [ "elevation", "elevation" ],
  "latitude" : [ "latitude", "latitude" ],
  "box" : [ "box", "box" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ],
  "longitude" : [ "longitude", "longitude" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/geoshapes'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(geo_shape),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
