# coding: utf-8

from __future__ import absolute_import

import logging
import unittest
from pathlib import Path

# Comparing the JSON objects (with nested levels ignoring the order)
from deepdiff import DeepDiff
import json

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase
from openapi_server.test.utils import read_json_file

from openapi_server.models.model_configuration import ModelConfiguration

INPUT_TESTS_DIRECTORY = Path('.') / 'openapi_server' / 'test' / 'input_tests'

class TestModelConfigurationController(BaseTestCase):
    logger = logging.getLogger("TestModelConfigurationController")
    input_test_directory = Path(__file__).parent / "input_tests"

    """ModelConfigurationController integration test stubs"""
    def test_datatransformationsetups_get(self):
        """Test case for datatransformationsetups_get

        List all ModelConfiguration entities
        """
        query_string = [('username', self.get_username)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.6.0/datatransformationsetups',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        #self.assertTrue(response.json)

    def test_datatransformationsetups_id_get(self):
        """Test case for datatransformationsetups_id_get
        Get a ModelConfiguration
        """
        query_string = [('username', self.get_username)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.6.0/datatransformationsetups/{id}'.format(id="hand_v2"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
