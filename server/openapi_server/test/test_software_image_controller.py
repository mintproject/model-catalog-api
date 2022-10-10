# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.software_image import SoftwareImage  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSoftwareImageController(BaseTestCase):
    """SoftwareImageController integration test stubs"""

    def test_softwareimages_get(self):
        """Test case for softwareimages_get

        List all instances of SoftwareImage
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/softwareimages',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareimages_id_delete(self):
        """Test case for softwareimages_id_delete

        Delete an existing SoftwareImage
        """
        query_string = [('user', 'user_example')]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/softwareimages/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareimages_id_get(self):
        """Test case for softwareimages_id_get

        Get a single SoftwareImage by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/softwareimages/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareimages_id_put(self):
        """Test case for softwareimages_id_put

        Update an existing SoftwareImage
        """
        software_image = {
  "value" : {
    "id" : "some_id"
  }
}
        query_string = [('user', 'user_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/softwareimages/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(software_image),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareimages_post(self):
        """Test case for softwareimages_post

        Create one SoftwareImage
        """
        software_image = {
  "value" : {
    "id" : "some_id"
  }
}
        query_string = [('user', 'user_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/softwareimages',
            method='POST',
            headers=headers,
            data=json.dumps(software_image),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
