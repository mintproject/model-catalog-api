# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModelConfigurationController(BaseTestCase):
    """ModelConfigurationController integration test stubs"""

    def test_custom_modelconfigurations_id_get(self):
        """Test case for custom_modelconfigurations_id_get

        Get a ModelConfiguration
        """
        query_string = [('username', 'username_example'),
                        ('custom_query_name', 'custom_modelconfigurations')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/custom/modelconfigurations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_get(self):
        """Test case for modelconfigurations_get

        List all instances of ModelConfiguration
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/modelconfigurations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_id_delete(self):
        """Test case for modelconfigurations_id_delete

        Delete an existing ModelConfiguration
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/modelconfigurations/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_id_get(self):
        """Test case for modelconfigurations_id_get

        Get a single ModelConfiguration by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/modelconfigurations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_id_put(self):
        """Test case for modelconfigurations_id_put

        Update an existing ModelConfiguration
        """
        model_configuration = {
  "value" : {
    "id" : "some_id"
  }
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/modelconfigurations/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(model_configuration),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_post(self):
        """Test case for modelconfigurations_post

        Create one ModelConfiguration
        """
        model_configuration = {
  "value" : {
    "id" : "some_id"
  }
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/modelconfigurations'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(model_configuration),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
