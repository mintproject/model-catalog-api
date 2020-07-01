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

        List all instances of SampleExecution
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/sampleexecutions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sampleexecutions_id_delete(self):
        """Test case for sampleexecutions_id_delete

        Delete an existing SampleExecution
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/sampleexecutions/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sampleexecutions_id_get(self):
        """Test case for sampleexecutions_id_get

        Get a single SampleExecution by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/sampleexecutions/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sampleexecutions_id_put(self):
        """Test case for sampleexecutions_id_put

        Update an existing SampleExecution
        """
        sample_execution = {
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
            '/v1.5.0/sampleexecutions/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(sample_execution),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sampleexecutions_post(self):
        """Test case for sampleexecutions_post

        Create one SampleExecution
        """
        sample_execution = {
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
            '/v1.5.0/sampleexecutions'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(sample_execution),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
