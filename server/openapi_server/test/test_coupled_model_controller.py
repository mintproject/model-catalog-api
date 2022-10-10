# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.coupled_model import CoupledModel  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCoupledModelController(BaseTestCase):
    """CoupledModelController integration test stubs"""

    def test_coupledmodels_get(self):
        """Test case for coupledmodels_get

        List all instances of CoupledModel
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/coupledmodels',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_coupledmodels_id_delete(self):
        """Test case for coupledmodels_id_delete

        Delete an existing CoupledModel
        """
        query_string = [('user', 'user_example')]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.8.0/coupledmodels/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_coupledmodels_id_get(self):
        """Test case for coupledmodels_id_get

        Get a single CoupledModel by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/coupledmodels/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_coupledmodels_id_put(self):
        """Test case for coupledmodels_id_put

        Update an existing CoupledModel
        """
        coupled_model = {
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
            '/v1.8.0/coupledmodels/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(coupled_model),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_coupledmodels_post(self):
        """Test case for coupledmodels_post

        Create one CoupledModel
        """
        coupled_model = {
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
            '/v1.8.0/coupledmodels',
            method='POST',
            headers=headers,
            data=json.dumps(coupled_model),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
