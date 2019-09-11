# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.causal_diagram import CausalDiagram  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCausalDiagramController(BaseTestCase):
    """CausalDiagramController integration test stubs"""

    def test_causaldiagrams_get(self):
        """Test case for causaldiagrams_get

        List all CausalDiagram entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/causaldiagrams',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_causaldiagrams_id_delete(self):
        """Test case for causaldiagrams_id_delete

        Delete a CausalDiagram
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/causaldiagrams/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_causaldiagrams_id_get(self):
        """Test case for causaldiagrams_id_get

        Get a CausalDiagram
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/causaldiagrams/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_causaldiagrams_id_put(self):
        """Test case for causaldiagrams_id_put

        Update a CausalDiagram
        """
        causal_diagram = {
  "hasPart" : [ "{}", "{}" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/causaldiagrams/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(causal_diagram),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_causaldiagrams_post(self):
        """Test case for causaldiagrams_post

        Create a CausalDiagram
        """
        causal_diagram = {
  "hasPart" : [ "{}", "{}" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/causaldiagrams'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(causal_diagram),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
