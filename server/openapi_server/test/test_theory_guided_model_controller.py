# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.theory_guided_model import TheoryGuidedModel  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTheoryGuidedModelController(BaseTestCase):
    """TheoryGuidedModelController integration test stubs"""

    def test_theory_guidedmodels_get(self):
        """Test case for theory_guidedmodels_get

        List all Theory-GuidedModel entities
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/theory-guidedmodels',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_theory_guidedmodels_id_delete(self):
        """Test case for theory_guidedmodels_id_delete

        Delete a Theory-GuidedModel
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/theory-guidedmodels/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_theory_guidedmodels_id_get(self):
        """Test case for theory_guidedmodels_id_get

        Get a Theory-GuidedModel
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/theory-guidedmodels/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_theory_guidedmodels_id_put(self):
        """Test case for theory_guidedmodels_id_put

        Update a Theory-GuidedModel
        """
        theory_guided_model = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/theory-guidedmodels/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(theory_guided_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_theory_guidedmodels_post(self):
        """Test case for theory_guidedmodels_post

        Create a Theory-GuidedModel
        """
        theory_guided_model = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/theory-guidedmodels'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(theory_guided_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
