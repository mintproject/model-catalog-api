# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.organization import Organization  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrganizationController(BaseTestCase):
    """OrganizationController integration test stubs"""

    def test_organizations_get(self):
        """Test case for organizations_get

        List all Organization entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/organizations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_organizations_id_delete(self):
        """Test case for organizations_id_delete

        Delete a Organization
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/organizations/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_organizations_id_get(self):
        """Test case for organizations_id_get

        Get a Organization
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/organizations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_organizations_id_put(self):
        """Test case for organizations_id_put

        Update a Organization
        """
        organization = {
  "identifier" : [ "identifier", "identifier" ],
  "website" : [ "website", "website" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/organizations/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(organization),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_organizations_post(self):
        """Test case for organizations_post

        Create a Organization
        """
        organization = {
  "identifier" : [ "identifier", "identifier" ],
  "website" : [ "website", "website" ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/organizations'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(organization),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
