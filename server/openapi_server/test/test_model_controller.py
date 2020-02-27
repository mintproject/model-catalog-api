# coding: utf-8

from __future__ import absolute_import

import logging
import unittest

from flask import json
from six import BytesIO

from openapi_server.models import Model
from openapi_server.test import BaseTestCase


class TestModel(BaseTestCase):
    """Model integration test stubs"""

    def test_model_variable_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', 'mint@isi.edu'),
                        ('label', 'crop')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.3.1/custom/models/variable',
            method='GET',
            headers=headers,
            query_string=query_string)

        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



if __name__ == '__main__':
    unittest.main()
