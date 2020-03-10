# coding: utf-8

from __future__ import absolute_import

import logging
import unittest
from pathlib import Path

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase

INPUT_TESTS_DIRECTORY = Path('.') / 'openapi_server' / 'test' / 'input_tests'


USERNAME = "mosorio@isi.edu"
MINT_USERNAME = "mint@isi.edu"
PASSWORD = "Cs0WgIQPWJ"


class TestModelConfigurationController(BaseTestCase):
    """ModelConfigurationController integration test stubs"""
    def test_modelconfigurations_get(self):
        """Test case for modelconfigurations_get

        List all ModelConfiguration entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'agriculture')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/modelconfigurations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_id_get(self):
        """Test case for modelconfigurations_id_get
        Get a ModelConfiguration
        """
        query_string = [('username', MINT_USERNAME)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/modelconfigurations/{id}'.format(id="hand_v2"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def login(self):
        query_string = [('username', USERNAME),
                        ('password', PASSWORD)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/user/login',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        return response


if __name__ == '__main__':
    unittest.main()
