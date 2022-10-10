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

        List all instances of NumericalIndex
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/numericalindexs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_numericalindexs_id_delete(self):
        """Test case for numericalindexs_id_delete

        Delete an existing NumericalIndex
        """
        query_string = [('user', 'user_example')]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/numericalindexs/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_numericalindexs_id_get(self):
        """Test case for numericalindexs_id_get

        Get a single NumericalIndex by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/numericalindexs/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_numericalindexs_id_put(self):
        """Test case for numericalindexs_id_put

        Update an existing NumericalIndex
        """
        numerical_index = {
  "value" : {
    "id" : "some_id"
  }
}
        query_string = [('user', 'user_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/numericalindexs/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(numerical_index),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_numericalindexs_post(self):
        """Test case for numericalindexs_post

        Create one NumericalIndex
        """
        numerical_index = {
  "value" : {
    "id" : "some_id"
  }
}
        query_string = [('user', 'user_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/numericalindexs',
            method='POST',
            headers=headers,
            data=json.dumps(numerical_index),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
