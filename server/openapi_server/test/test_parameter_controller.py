# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.parameter import Parameter  # noqa: E501
from openapi_server.test import BaseTestCase


class TestParameterController(BaseTestCase):
    """ParameterController integration test stubs"""

    def test_create_parameter(self):
        """Test case for create_parameter

        Create a Parameter
        """
        parameter = Parameter()
        response = self.client.open(
            '/v0.0.1/parameters',
            method='POST',
            data=json.dumps(parameter),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_parameters(self):
        """Test case for get_parameters

        List All Parameters
        """
        response = self.client.open(
            '/v0.0.1/parameters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
