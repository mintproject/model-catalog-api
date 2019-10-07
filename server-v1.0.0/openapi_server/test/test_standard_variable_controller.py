# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.standard_variable import StandardVariable  # noqa: E501
from openapi_server.test import BaseTestCase


class TestStandardVariableController(BaseTestCase):
    """StandardVariableController integration test stubs"""

    def test_standardvariables_get(self):
        """Test case for standardvariables_get

        List all StandardVariable entities
        """
        query_string = [('username', 'username_example'),
                        ('query_text', 'query_text_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/standardvariables',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_standardvariables_id_delete(self):
        """Test case for standardvariables_id_delete

        Delete a StandardVariable
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/standardvariables/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_standardvariables_id_get(self):
        """Test case for standardvariables_id_get

        Get a StandardVariable
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/standardvariables/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_standardvariables_id_put(self):
        """Test case for standardvariables_id_put

        Update a StandardVariable
        """
        standard_variable = {
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/standardvariables/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(standard_variable),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_standardvariables_post(self):
        """Test case for standardvariables_post

        Create a StandardVariable
        """
        standard_variable = {
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/standardvariables'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(standard_variable),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
