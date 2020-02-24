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
PASSWORD = "Cs0WgIQPWJ"


class TestModelConfigurationController(BaseTestCase):
    """ModelConfigurationController integration test stubs"""
    def test_modelconfigurations_get(self):
        """Test case for modelconfigurations_get

        List all ModelConfiguration entities
        """
        query_string = [('username', USERNAME),
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

    def test_modelconfigurations_post(self):
        """Test case for modelconfigurations_post

        Create a ModelConfiguration
        """

        path = INPUT_TESTS_DIRECTORY / 'model_configuration_without_id.json'
        with open(path) as json_file:
            data = json.load(json_file)

        login_response = self.login()

        token = login_response.json['access_token']
        headers = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer {}".format(token)
        }

        response = self.client.open(
            '/v1.4.0/modelconfigurations'.format(user=USERNAME),
            method='POST',
            headers=headers,
            data=json.dumps(data),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)

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
