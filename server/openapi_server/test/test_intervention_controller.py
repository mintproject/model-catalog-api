# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.intervention import Intervention  # noqa: E501
from openapi_server.test import BaseTestCase


class TestInterventionController(BaseTestCase):
    """InterventionController integration test stubs"""

    def test_interventions_get(self):
        """Test case for interventions_get

        List all Intervention entities
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/interventions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_interventions_id_delete(self):
        """Test case for interventions_id_delete

        Delete a Intervention
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/interventions/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_interventions_id_get(self):
        """Test case for interventions_id_get

        Get a Intervention
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/interventions/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_interventions_id_put(self):
        """Test case for interventions_id_put

        Update a Intervention
        """
        intervention = {
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
            '/v1.2.0/interventions/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(intervention),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_interventions_post(self):
        """Test case for interventions_post

        Create a Intervention
        """
        intervention = {
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
            '/v1.2.0/interventions'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(intervention),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
