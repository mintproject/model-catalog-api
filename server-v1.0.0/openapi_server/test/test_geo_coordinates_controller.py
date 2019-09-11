# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.geo_coordinates import GeoCoordinates  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGeoCoordinatesController(BaseTestCase):
    """GeoCoordinatesController integration test stubs"""

    def test_geocoordinatess_get(self):
        """Test case for geocoordinatess_get

        List all GeoCoordinates entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/geocoordinatess',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geocoordinatess_id_delete(self):
        """Test case for geocoordinatess_id_delete

        Delete a GeoCoordinates
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/geocoordinatess/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geocoordinatess_id_get(self):
        """Test case for geocoordinatess_id_get

        Get a GeoCoordinates
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/geocoordinatess/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geocoordinatess_id_put(self):
        """Test case for geocoordinatess_id_put

        Update a GeoCoordinates
        """
        geo_coordinates = {
  "elevation" : [ "elevation", "elevation" ],
  "latitude" : [ "latitude", "latitude" ],
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
            '/v1.0.0/geocoordinatess/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(geo_coordinates),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geocoordinatess_post(self):
        """Test case for geocoordinatess_post

        Create a GeoCoordinates
        """
        geo_coordinates = {
  "elevation" : [ "elevation", "elevation" ],
  "latitude" : [ "latitude", "latitude" ],
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
            '/v1.0.0/geocoordinatess'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(geo_coordinates),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
