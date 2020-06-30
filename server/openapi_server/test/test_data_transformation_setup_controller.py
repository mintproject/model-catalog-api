# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.data_transformation_setup import DataTransformationSetup  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDataTransformationSetupController(BaseTestCase):
    """DataTransformationSetupController integration test stubs"""

    def test_datatransformationsetups_get(self):
        """Test case for datatransformationsetups_get

        List all instances of DataTransformationSetup
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/datatransformationsetups',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datatransformationsetups_id_delete(self):
        """Test case for datatransformationsetups_id_delete

        Delete an existing DataTransformationSetup
        """
        query_string = [('user', 'user_example')]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/datatransformationsetups/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datatransformationsetups_id_get(self):
        """Test case for datatransformationsetups_id_get

        Get a single DataTransformationSetup by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/datatransformationsetups/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datatransformationsetups_id_put(self):
        """Test case for datatransformationsetups_id_put

        Update an existing DataTransformationSetup
        """
        data_transformation_setup = {
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
            '/v1.5.0/datatransformationsetups/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(data_transformation_setup),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datatransformationsetups_post(self):
        """Test case for datatransformationsetups_post

        Create one DataTransformationSetup
        """
        data_transformation_setup = {
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
            '/v1.5.0/datatransformationsetups',
            method='POST',
            headers=headers,
            data=json.dumps(data_transformation_setup),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
