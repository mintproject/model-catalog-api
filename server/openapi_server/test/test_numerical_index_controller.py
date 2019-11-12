# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.numerical_index import NumericalIndex  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNumericalIndexController(BaseTestCase):
    """NumericalIndexController integration test stubs"""

    def test_numericalindexs_get(self):
        """Test case for numericalindexs_get

        List all NumericalIndex entities
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/numericalindexs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_numericalindexs_id_delete(self):
        """Test case for numericalindexs_id_delete

        Delete a NumericalIndex
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/numericalindexs/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_numericalindexs_id_get(self):
        """Test case for numericalindexs_id_get

        Get a NumericalIndex
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/numericalindexs/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_numericalindexs_id_put(self):
        """Test case for numericalindexs_id_put

        Update a NumericalIndex
        """
        numerical_index = {
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
            '/v1.2.0/numericalindexs/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(numerical_index),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_numericalindexs_post(self):
        """Test case for numericalindexs_post

        Create a NumericalIndex
        """
        numerical_index = {
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
            '/v1.2.0/numericalindexs'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(numerical_index),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
