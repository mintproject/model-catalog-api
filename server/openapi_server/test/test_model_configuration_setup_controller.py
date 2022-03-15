# coding: utf-8

from __future__ import absolute_import

import logging
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: E501
from openapi_server.test import BaseTestCase

MINT_USERNAME = "mint@isi.edu"

class TestModelConfigurationSetupController(BaseTestCase):
    """ModelConfigurationSetupController integration test stubs"""
    logger = logging.getLogger("TestModelConfigurationSetupController")

    def test_modelconfigurationsetups_get(self):
        """Test case for modelconfigurationsetups_get

        List all ModelConfigurationSetup entities
        """
        query_string = [('username', MINT_USERNAME)]

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/modelconfigurationsetups',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assertTrue(response.json)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        for _item in response.json:
            keys = _item.keys()
            for key in keys:
                self.check_key(key)

if __name__ == '__main__':
    unittest.main()
