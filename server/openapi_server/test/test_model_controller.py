# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.model import Model  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModelController(BaseTestCase):
    """ModelController integration test stubs"""

    def test_createmodel(self):
        """Test case for createmodel

        Create a model
        """
        model = Model()
        response = self.client.open(
            '/v0.0.1/models',
            method='POST',
            data=json.dumps(model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_model(self):
        """Test case for delete_model

        Delete a Model
        """
        response = self.client.open(
            '/v0.0.1/model/{modelId}'.format(model_id='model_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_model(self):
        """Test case for get_model

        Get a Model
        """
        response = self.client.open(
            '/v0.0.1/model/{modelId}'.format(model_id='model_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getmodels(self):
        """Test case for getmodels

        List All models
        """
        response = self.client.open(
            '/v0.0.1/models',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_model(self):
        """Test case for update_model

        Update a Model
        """
        model = Model()
        response = self.client.open(
            '/v0.0.1/model/{modelId}'.format(model_id='model_id_example'),
            method='PUT',
            data=json.dumps(model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
