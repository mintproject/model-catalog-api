# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_user_login_get(self):
        """Test case for user_login_get

        
        """
        query_string = [('username', 'username_example'),
                        ('password', 'password_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/user/login',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
