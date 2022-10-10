# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.configuration_setup import ConfigurationSetup  # noqa: E501
from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: E501
from openapi_server.test import BaseTestCase


class TestConfigurationSetupController(BaseTestCase):
    """ConfigurationSetupController integration test stubs"""

    def test_configurationsetups_get(self):
        """Test case for configurationsetups_get

        List all instances of ConfigurationSetup
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/configurationsetups',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_configurationsetups_id_delete(self):
        """Test case for configurationsetups_id_delete

        Delete an existing ConfigurationSetup
        """
        query_string = [('user', 'user_example')]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/configurationsetups/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_configurationsetups_id_get(self):
        """Test case for configurationsetups_id_get

        Get a single ConfigurationSetup by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/configurationsetups/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_configurationsetups_id_put(self):
        """Test case for configurationsetups_id_put

        Update an existing ConfigurationSetup
        """
        configuration_setup = {
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
            '/v1.8.0/configurationsetups/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(configuration_setup),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_configurationsetups_post(self):
        """Test case for configurationsetups_post

        Create one ConfigurationSetup
        """
        configuration_setup = {
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
            '/v1.8.0/configurationsetups',
            method='POST',
            headers=headers,
            data=json.dumps(configuration_setup),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_custom_configurationsetups_id_get(self):
        """Test case for custom_configurationsetups_id_get

        Get a ModelConfigurationSetup
        """
        query_string = [('username', 'username_example'),
                        ('custom_query_name', 'custom_configurationsetups')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/custom/configurationsetups/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
