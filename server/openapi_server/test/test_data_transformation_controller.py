# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.data_transformation import DataTransformation  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDataTransformationController(BaseTestCase):
    """DataTransformationController integration test stubs"""

    def test_datatransformations_get(self):
        """Test case for datatransformations_get

        List all instances of DataTransformation
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/datatransformations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datatransformations_id_delete(self):
        """Test case for datatransformations_id_delete

        Delete an existing DataTransformation
        """
        query_string = [('user', 'user_example')]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/datatransformations/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datatransformations_id_get(self):
        """Test case for datatransformations_id_get

        Get a single DataTransformation by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/datatransformations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datatransformations_id_put(self):
        """Test case for datatransformations_id_put

        Update an existing DataTransformation
        """
        data_transformation = {
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
            '/v1.5.0/datatransformations/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(data_transformation),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datatransformations_post(self):
        """Test case for datatransformations_post

        Create one DataTransformation
        """
        data_transformation = {
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
            '/v1.5.0/datatransformations',
            method='POST',
            headers=headers,
            data=json.dumps(data_transformation),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
