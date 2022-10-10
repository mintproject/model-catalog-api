# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.variable_presentation import VariablePresentation  # noqa: E501
from openapi_server.test import BaseTestCase


class TestVariablePresentationController(BaseTestCase):
    """VariablePresentationController integration test stubs"""

    def test_variablepresentations_get(self):
        """Test case for variablepresentations_get

        List all instances of VariablePresentation
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/variablepresentations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variablepresentations_id_delete(self):
        """Test case for variablepresentations_id_delete

        Delete an existing VariablePresentation
        """
        query_string = [('user', 'user_example')]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/variablepresentations/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variablepresentations_id_get(self):
        """Test case for variablepresentations_id_get

        Get a single VariablePresentation by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/variablepresentations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variablepresentations_id_put(self):
        """Test case for variablepresentations_id_put

        Update an existing VariablePresentation
        """
        variable_presentation = {
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
            '/v1.8.0/variablepresentations/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(variable_presentation),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variablepresentations_post(self):
        """Test case for variablepresentations_post

        Create one VariablePresentation
        """
        variable_presentation = {
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
            '/v1.8.0/variablepresentations',
            method='POST',
            headers=headers,
            data=json.dumps(variable_presentation),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
