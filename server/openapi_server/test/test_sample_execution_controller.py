# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.sample_execution import SampleExecution  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSampleExecutionController(BaseTestCase):
    """SampleExecutionController integration test stubs"""

    def test_sampleexecutions_get(self):
        """Test case for sampleexecutions_get

        List all SampleExecution entities
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/sampleexecutions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sampleexecutions_id_delete(self):
        """Test case for sampleexecutions_id_delete

        Delete a SampleExecution
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/sampleexecutions/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sampleexecutions_id_get(self):
        """Test case for sampleexecutions_id_get

        Get a SampleExecution
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/sampleexecutions/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sampleexecutions_id_put(self):
        """Test case for sampleexecutions_id_put

        Update a SampleExecution
        """
        sample_execution = {
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ],
  "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/sampleexecutions/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(sample_execution),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sampleexecutions_post(self):
        """Test case for sampleexecutions_post

        Create a SampleExecution
        """
        sample_execution = {
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ],
  "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/sampleexecutions'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(sample_execution),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
