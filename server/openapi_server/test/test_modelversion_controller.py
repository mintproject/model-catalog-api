# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.model_version import ModelVersion  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModelversionController(BaseTestCase):
    """ModelversionController integration test stubs"""

    def test_create_model_version(self):
        """Test case for create_model_version

        Create a ModelVersion
        """
        model_version = ModelVersion()
        response = self.client.open(
            '/v0.0.1/modelversions',
            method='POST',
            data=json.dumps(model_version),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_model_version(self):
        """Test case for delete_model_version

        Delete a ModelVersion
        """
        response = self.client.open(
            '/v0.0.1/modelversion/{modelVersionId}'.format(model_version_id='model_version_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_model_version(self):
        """Test case for get_model_version

        Get a ModelVersion
        """
        response = self.client.open(
            '/v0.0.1/modelversion/{modelVersionId}'.format(model_version_id='model_version_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_model_versions(self):
        """Test case for get_model_versions

        List All ModelVersions
        """
        response = self.client.open(
            '/v0.0.1/modelversions',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_model_version(self):
        """Test case for update_model_version

        Update a ModelVersion
        """
        model_version = ModelVersion()
        response = self.client.open(
            '/v0.0.1/modelversion/{modelVersionId}'.format(model_version_id='model_version_id_example'),
            method='PUT',
            data=json.dumps(model_version),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
