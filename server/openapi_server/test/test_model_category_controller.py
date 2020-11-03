# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.model_category import ModelCategory  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModelCategoryController(BaseTestCase):
    """ModelCategoryController integration test stubs"""

    def test_modelcategorys_get(self):
        """Test case for modelcategorys_get

        List all instances of ModelCategory
        """
        query_string = [('username', 'mint@isi.edu')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.6.0/modelcategorys',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.json)

#    def test_modelcategorys_id_delete(self):
#        """Test case for modelcategorys_id_delete
#
#        Delete an existing ModelCategory
#        """
#        headers = { 
#            'Authorization': 'Bearer special-key',
#        }
#        response = self.client.open(
#            '/v1.6.0/modelcategorys/{id}'.format(id='id_example', user='user_example'),
#            method='DELETE',
#            headers=headers)
#        self.assert200(response,
#                       'Response body is : ' + response.data.decode('utf-8'))
#
#    def test_modelcategorys_id_get(self):
#        """Test case for modelcategorys_id_get
#
#        Get a single ModelCategory by its id
#        """
#        query_string = [('username', 'username_example')]
#        headers = { 
#            'Accept': 'application/json',
#        }
#        response = self.client.open(
#            '/v1.6.0/modelcategorys/{id}'.format(id='id_example'),
#            method='GET',
#            headers=headers,
#            query_string=query_string)
#        self.assert200(response,
#                       'Response body is : ' + response.data.decode('utf-8'))
#
#    def test_modelcategorys_id_put(self):
#        """Test case for modelcategorys_id_put
#
#        Update an existing ModelCategory
#        """
#        model_category = {
#  "value" : {
#    "id" : "some_id"
#  }
#}
#        headers = { 
#            'Accept': 'application/json',
#            'Content-Type': 'application/json',
#            'Authorization': 'Bearer special-key',
#        }
#        response = self.client.open(
#            '/v1.6.0/modelcategorys/{id}'.format(id='id_example', user='user_example'),
#            method='PUT',
#            headers=headers,
#            data=json.dumps(model_category),
#            content_type='application/json')
#        self.assert200(response,
#                       'Response body is : ' + response.data.decode('utf-8'))
#
#    def test_modelcategorys_post(self):
#        """Test case for modelcategorys_post
#
#        Create one ModelCategory
#        """
#        model_category = {
#  "value" : {
#    "id" : "some_id"
#  }
#}
#        headers = { 
#            'Accept': 'application/json',
#            'Content-Type': 'application/json',
#            'Authorization': 'Bearer special-key',
#        }
#        response = self.client.open(
#            '/v1.6.0/modelcategorys'.format(user='user_example'),
#            method='POST',
#            headers=headers,
#            data=json.dumps(model_category),
#            content_type='application/json')
#        self.assert200(response,
#                       'Response body is : ' + response.data.decode('utf-8'))
#

if __name__ == '__main__':
    unittest.main()
