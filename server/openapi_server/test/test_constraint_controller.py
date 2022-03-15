# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.constraint import Constraint  # noqa: E501
from openapi_server.test import BaseTestCase


class TestConstraintController(BaseTestCase):
    """ConstraintController integration test stubs"""

    def test_constraints_get(self):
        """Test case for constraints_get

        List all instances of Constraint
        """
        query_string = [('username', 'mint@isi.edu')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/constraints',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



if __name__ == '__main__':
    unittest.main()
