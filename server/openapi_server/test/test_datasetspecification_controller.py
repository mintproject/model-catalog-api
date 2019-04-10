# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.dataset_specification import DatasetSpecification  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDatasetspecificationController(BaseTestCase):
    """DatasetspecificationController integration test stubs"""

    def test_create_data_set(self):
        """Test case for create_data_set

        Create a datasetspecification
        """
        dataset_specification = DatasetSpecification()
        response = self.client.open(
            '/v0.0.2/datasetspecifications',
            method='POST',
            data=json.dumps(dataset_specification),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_data_sets(self):
        """Test case for get_data_sets

        List All datasetspecifications
        """
        query_string = [('username', 'username_example')]
        response = self.client.open(
            '/v0.0.2/datasetspecifications',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
