# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.process import Process  # noqa: E501
from openapi_server.test import BaseTestCase


class TestProcessController(BaseTestCase):
    """ProcessController integration test stubs"""

    def test_processs_get(self):
        """Test case for processs_get

        List all Process entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/processs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_processs_id_delete(self):
        """Test case for processs_id_delete

        Delete a Process
        """
        headers = { 
        }
        response = self.client.open(
            '/v1.0.0/processs/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_processs_id_get(self):
        """Test case for processs_id_get

        Get a Process
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/processs/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_processs_id_put(self):
        """Test case for processs_id_put

        Update a Process
        """
        process = {
  "influences" : [ null, null ],
  "id" : [ "id", "id" ],
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/processs/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(process),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_processs_post(self):
        """Test case for processs_post

        Create a Process
        """
        process = {
  "influences" : [ null, null ],
  "id" : [ "id", "id" ],
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/processs',
            method='POST',
            headers=headers,
            data=json.dumps(process),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
