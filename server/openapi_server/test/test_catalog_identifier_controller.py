# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.catalog_identifier import CatalogIdentifier  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCatalogIdentifierController(BaseTestCase):
    """CatalogIdentifierController integration test stubs"""

    def test_catalogidentifiers_get(self):
        """Test case for catalogidentifiers_get

        List all instances of CatalogIdentifier
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.6.0/catalogidentifiers',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_catalogidentifiers_id_delete(self):
        """Test case for catalogidentifiers_id_delete

        Delete an existing CatalogIdentifier
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.6.0/catalogidentifiers/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_catalogidentifiers_id_get(self):
        """Test case for catalogidentifiers_id_get

        Get a single CatalogIdentifier by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.6.0/catalogidentifiers/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_catalogidentifiers_id_put(self):
        """Test case for catalogidentifiers_id_put

        Update an existing CatalogIdentifier
        """
        catalog_identifier = {
  "value" : {
    "id" : "some_id"
  }
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.6.0/catalogidentifiers/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(catalog_identifier),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_catalogidentifiers_post(self):
        """Test case for catalogidentifiers_post

        Create one CatalogIdentifier
        """
        catalog_identifier = {
  "value" : {
    "id" : "some_id"
  }
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.6.0/catalogidentifiers'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(catalog_identifier),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
