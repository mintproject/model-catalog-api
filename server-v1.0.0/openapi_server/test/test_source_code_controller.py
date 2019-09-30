# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.source_code import SourceCode  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSourceCodeController(BaseTestCase):
    """SourceCodeController integration test stubs"""

    def test_sourcecodes_get(self):
        """Test case for sourcecodes_get

        List all SourceCode entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/sourcecodes',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sourcecodes_id_delete(self):
        """Test case for sourcecodes_id_delete

        Delete a SourceCode
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/sourcecodes/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sourcecodes_id_get(self):
        """Test case for sourcecodes_id_get

        Get a SourceCode
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/sourcecodes/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sourcecodes_id_put(self):
        """Test case for sourcecodes_id_put

        Update a SourceCode
        """
        source_code = {
  "license" : [ "license", "license" ],
  "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
  "codeRepository" : [ "codeRepository", "codeRepository" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/sourcecodes/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(source_code),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sourcecodes_post(self):
        """Test case for sourcecodes_post

        Create a SourceCode
        """
        source_code = {
  "license" : [ "license", "license" ],
  "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
  "codeRepository" : [ "codeRepository", "codeRepository" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/sourcecodes'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(source_code),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
