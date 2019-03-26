# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.data_set import DataSet  # noqa: E501
from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501
from openapi_server.models.parameter import Parameter  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModelconfigurationController(BaseTestCase):
    """ModelconfigurationController integration test stubs"""

    def test_add_inputs_by_modelconfiguration(self):
        """Test case for add_inputs_by_modelconfiguration

        Creates a new instance of a `Dataset` related as Input.
        """
        data_set = None
        response = self.client.open(
            '/v0.0.1/modelconfiguration/{name}/inputs'.format(name='name_example'),
            method='POST',
            data=json.dumps(data_set),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_model_configuration(self):
        """Test case for add_model_configuration

        Create a model configuration
        """
        model_configuration = ModelConfiguration()
        response = self.client.open(
            '/v0.0.1/modelconfigurations',
            method='POST',
            data=json.dumps(model_configuration),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_parameters_by_modelconfiguration(self):
        """Test case for add_parameters_by_modelconfiguration

        Create the inputs of a model configuration
        """
        parameter = None
        response = self.client.open(
            '/v0.0.1/modelconfiguration/{name}/parameters'.format(name='name_example'),
            method='POST',
            data=json.dumps(parameter),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_model_configuration(self):
        """Test case for delete_model_configuration

        Delete a ModelConfiguration
        """
        response = self.client.open(
            '/v0.0.1/modelconfiguration/{name}'.format(name='name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_inputs_by_modelconfiguration(self):
        """Test case for get_inputs_by_modelconfiguration

        Get the inputs of a model configuration
        """
        response = self.client.open(
            '/v0.0.1/modelconfiguration/{name}/inputs'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_model_configuraton_by_uri(self):
        """Test case for get_model_configuraton_by_uri

        Get modelconfiguration by uri
        """
        response = self.client.open(
            '/v0.0.1/modelconfiguration/{name}'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_outputs_by_modelconfiguration(self):
        """Test case for get_outputs_by_modelconfiguration

        Get the outputs of a model configuration
        """
        response = self.client.open(
            '/v0.0.1/modelconfiguration/{name}/outputs'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_parameters_by_modelconfiguration(self):
        """Test case for get_parameters_by_modelconfiguration

        Get the parameters of a model configuration
        """
        response = self.client.open(
            '/v0.0.1/modelconfiguration/{name}/parameters'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_model_configurations(self):
        """Test case for list_model_configurations

        List modelconfiguration
        """
        response = self.client.open(
            '/v0.0.1/modelconfigurations',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfiguration_name_outputs_post(self):
        """Test case for modelconfiguration_name_outputs_post

        Create the output of a model configuration
        """
        data_set = None
        response = self.client.open(
            '/v0.0.1/modelconfiguration/{name}/outputs'.format(name='name_example'),
            method='POST',
            data=json.dumps(data_set),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_model_configuration(self):
        """Test case for update_model_configuration

        Update model configuration
        """
        model_configuration = ModelConfiguration()
        response = self.client.open(
            '/v0.0.1/modelconfiguration/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(model_configuration),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
