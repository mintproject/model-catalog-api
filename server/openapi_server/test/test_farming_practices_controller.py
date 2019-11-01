# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.farming_practices import FarmingPractices  # noqa: E501
from openapi_server.test import BaseTestCase


class TestFarmingPracticesController(BaseTestCase):
    """FarmingPracticesController integration test stubs"""

    def test_farmingpracticess_get(self):
        """Test case for farmingpracticess_get

        List all FarmingPractices entities
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/farmingpracticess',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_farmingpracticess_id_delete(self):
        """Test case for farmingpracticess_id_delete

        Delete a FarmingPractices
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/farmingpracticess/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_farmingpracticess_id_get(self):
        """Test case for farmingpracticess_id_get

        Get a FarmingPractices
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/farmingpracticess/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_farmingpracticess_id_put(self):
        """Test case for farmingpracticess_id_put

        Update a FarmingPractices
        """
        farming_practices = {
  "description" : [ "description", "description" ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/farmingpracticess/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(farming_practices),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_farmingpracticess_post(self):
        """Test case for farmingpracticess_post

        Create a FarmingPractices
        """
        farming_practices = {
  "description" : [ "description", "description" ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/farmingpracticess'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(farming_practices),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
