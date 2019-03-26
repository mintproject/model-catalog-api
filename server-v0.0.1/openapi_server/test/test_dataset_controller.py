# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.data_set import DataSet  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDatasetController(BaseTestCase):
    """DatasetController integration test stubs"""

    def test_createdataset(self):
        """Test case for createdataset

        Create a dataset
        """
        data_set = DataSet()
        response = self.client.open(
            '/v0.0.1/datasets',
            method='POST',
            data=json.dumps(data_set),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getdatasets(self):
        """Test case for getdatasets

        List All datasets
        """
        response = self.client.open(
            '/v0.0.1/datasets',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
