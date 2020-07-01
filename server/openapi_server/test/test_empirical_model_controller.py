# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.empirical_model import EmpiricalModel  # noqa: E501
from openapi_server.test import BaseTestCase


class TestEmpiricalModelController(BaseTestCase):
    """EmpiricalModelController integration test stubs"""

    def test_empiricalmodels_get(self):
        """Test case for empiricalmodels_get

        List all instances of EmpiricalModel
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/empiricalmodels',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empiricalmodels_id_delete(self):
        """Test case for empiricalmodels_id_delete

        Delete an existing EmpiricalModel
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/empiricalmodels/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empiricalmodels_id_get(self):
        """Test case for empiricalmodels_id_get

        Get a single EmpiricalModel by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/empiricalmodels/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empiricalmodels_id_put(self):
        """Test case for empiricalmodels_id_put

        Update an existing EmpiricalModel
        """
        empirical_model = {
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
            '/v1.5.0/empiricalmodels/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(empirical_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empiricalmodels_post(self):
        """Test case for empiricalmodels_post

        Create one EmpiricalModel
        """
        empirical_model = {
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
            '/v1.5.0/empiricalmodels'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(empirical_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
