# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModelConfigurationSetupController(BaseTestCase):
    """ModelConfigurationSetupController integration test stubs"""

    def test_custom_modelconfigurationsetups_id_get(self):
        """Test case for custom_modelconfigurationsetups_id_get

        Get a ModelConfigurationSetup
        """
        query_string = [('username', 'username_example'),
                        ('custom_query_name', 'custom_modelconfigurationsetups')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/custom/modelconfigurationsetups/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_custom_modelconfigurationsetups_variable_get(self):
        """Test case for custom_modelconfigurationsetups_variable_get

        Get a list  Model
        """
        query_string = [('custom_query_name', 'custom_modelconfigurationsetups_variable'),
                        ('username', 'username_example'),
                        ('label', 'label_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/custom/modelconfigurationsetups/variable',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_get(self):
        """Test case for modelconfigurationsetups_get

        List all instances of ModelConfigurationSetup
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/modelconfigurationsetups',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_id_delete(self):
        """Test case for modelconfigurationsetups_id_delete

        Delete an existing ModelConfigurationSetup
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/modelconfigurationsetups/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_id_get(self):
        """Test case for modelconfigurationsetups_id_get

        Get a single ModelConfigurationSetup by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/modelconfigurationsetups/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_id_put(self):
        """Test case for modelconfigurationsetups_id_put

        Update an existing ModelConfigurationSetup
        """
        model_configuration_setup = {
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
            '/v1.5.0/modelconfigurationsetups/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(model_configuration_setup),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_post(self):
        """Test case for modelconfigurationsetups_post

        Create one ModelConfigurationSetup
        """
        model_configuration_setup = {
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
            '/v1.5.0/modelconfigurationsetups'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(model_configuration_setup),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
