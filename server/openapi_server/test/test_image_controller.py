# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.image import Image  # noqa: E501
from openapi_server.test import BaseTestCase


class TestImageController(BaseTestCase):
    """ImageController integration test stubs"""

    def test_images_get(self):
        """Test case for images_get

        List all Image entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/images',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.json)

if __name__ == '__main__':
    unittest.main()
