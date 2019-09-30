# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.icasa_variable import ICASAVariable  # noqa: E501
from openapi_server.test import BaseTestCase


class TestICASAVariableController(BaseTestCase):
    """ICASAVariableController integration test stubs"""

    def test_icasavariables_get(self):
        """Test case for icasavariables_get

        List all ICASAVariable entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/icasavariables',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_icasavariables_id_delete(self):
        """Test case for icasavariables_id_delete

        Delete a ICASAVariable
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/icasavariables/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_icasavariables_id_get(self):
        """Test case for icasavariables_id_get

        Get a ICASAVariable
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/icasavariables/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_icasavariables_id_put(self):
        """Test case for icasavariables_id_put

        Update a ICASAVariable
        """
        icasa_variable = {
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/icasavariables/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(icasa_variable),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_icasavariables_post(self):
        """Test case for icasavariables_post

        Create a ICASAVariable
        """
        icasa_variable = {
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/icasavariables'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(icasa_variable),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
