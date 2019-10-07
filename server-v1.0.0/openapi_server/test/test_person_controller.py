# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.person import Person  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPersonController(BaseTestCase):
    """PersonController integration test stubs"""

    def test_persons_get(self):
        """Test case for persons_get

        List all Person entities
        """
        query_string = [('username', 'username_example'),
                        ('query_text', 'query_text_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/persons',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_id_delete(self):
        """Test case for persons_id_delete

        Delete a Person
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/persons/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_id_get(self):
        """Test case for persons_id_get

        Get a Person
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/persons/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_id_put(self):
        """Test case for persons_id_put

        Update a Person
        """
        person = {
  "identifier" : [ "identifier", "identifier" ],
  "website" : [ "website", "website" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ],
  "email" : [ "email", "email" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/persons/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(person),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_post(self):
        """Test case for persons_post

        Create a Person
        """
        person = {
  "identifier" : [ "identifier", "identifier" ],
  "website" : [ "website", "website" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ],
  "email" : [ "email", "email" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/persons'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(person),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
