# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.dataset_specification import DatasetSpecification  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDatasetSpecificationController(BaseTestCase):
    """DatasetSpecificationController integration test stubs"""

    def test_custom_configuration_id_inputs_get(self):
        """Test case for custom_configuration_id_inputs_get

        Gets all inputs of a configuration
        """
        query_string = [('username', 'username_example'),
                        ('custom_query_name', 'search_datasetspecification_by_configurationid')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/custom/configuration/{id}/inputs'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_custom_datasetspecifications_get(self):
        """Test case for custom_datasetspecifications_get

        Gets all inputs of a configuration
        """
        query_string = [('username', 'username_example'),
                        ('configurationid', 'configurationid_example'),
                        ('custom_query_name', 'custom_allinputs')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/custom/datasetspecifications',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datasetspecifications_get(self):
        """Test case for datasetspecifications_get

        List all instances of DatasetSpecification
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/datasetspecifications',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datasetspecifications_id_delete(self):
        """Test case for datasetspecifications_id_delete

        Delete an existing DatasetSpecification
        """
        query_string = [('user', 'user_example')]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/datasetspecifications/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datasetspecifications_id_get(self):
        """Test case for datasetspecifications_id_get

        Get a single DatasetSpecification by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/datasetspecifications/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datasetspecifications_id_put(self):
        """Test case for datasetspecifications_id_put

        Update an existing DatasetSpecification
        """
        dataset_specification = {
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
            '/v1.8.0/datasetspecifications/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(dataset_specification),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datasetspecifications_post(self):
        """Test case for datasetspecifications_post

        Create one DatasetSpecification
        """
        dataset_specification = {
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
            '/v1.8.0/datasetspecifications',
            method='POST',
            headers=headers,
            data=json.dumps(dataset_specification),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
