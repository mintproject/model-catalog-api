# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.index import Index  # noqa: E501
from openapi_server.test import BaseTestCase


class TestIndexController(BaseTestCase):
    """IndexController integration test stubs"""

    def test_indexs_get(self):
        """Test case for indexs_get

        List all Index entities
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/indexs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_indexs_id_delete(self):
        """Test case for indexs_id_delete

        Delete a Index
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/indexs/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_indexs_id_get(self):
        """Test case for indexs_id_get

        Get a Index
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/indexs/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_indexs_id_put(self):
        """Test case for indexs_id_put

        Update a Index
        """
        index = {
  "description" : [ "description", "description" ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/indexs/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(index),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_indexs_post(self):
        """Test case for indexs_post

        Create a Index
        """
        index = {
  "description" : [ "description", "description" ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/indexs'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(index),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
