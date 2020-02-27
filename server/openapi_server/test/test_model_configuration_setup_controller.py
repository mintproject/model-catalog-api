# coding: utf-8

from __future__ import absolute_import

import logging
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModelConfigurationSetupController(BaseTestCase):
    """ModelConfigurationSetupController integration test stubs"""

    def test_modelconfigurationsetups_variable_get(self):
        """Test case for modelconfigurationsetups_get

        List all ModelConfigurationSetup entities
        """
        query_string = [('username', 'mint@isi.edu'),
                        ('label', 'crop')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.3.1/custom/modelconfigurationsetups/variable',
            method='GET',
            headers=headers,
            query_string=query_string)

        for item in response.json:
            self.assertIsInstance(ModelConfigurationSetup.from_dict(item), ModelConfigurationSetup)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



if __name__ == '__main__':
    unittest.main()
