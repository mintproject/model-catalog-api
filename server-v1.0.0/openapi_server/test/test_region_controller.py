# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.region import Region  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRegionController(BaseTestCase):
    """RegionController integration test stubs"""

    def test_regions_get(self):
        """Test case for regions_get

        List all Region entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/regions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_regions_id_delete(self):
        """Test case for regions_id_delete

        Delete a Region
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/regions/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_regions_id_get(self):
        """Test case for regions_id_get

        Get a Region
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/regions/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_regions_id_put(self):
        """Test case for regions_id_put

        Update a Region
        """
        region = {
  "geo" : [ "{}", "{}" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/regions/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(region),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_regions_post(self):
        """Test case for regions_post

        Create a Region
        """
        region = {
  "geo" : [ "{}", "{}" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/regions'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(region),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
