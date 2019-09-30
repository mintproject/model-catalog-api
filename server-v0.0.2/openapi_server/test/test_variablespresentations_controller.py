# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.variable_presentation import VariablePresentation  # noqa: E501
from openapi_server.test import BaseTestCase


class TestVariablespresentationsController(BaseTestCase):
    """VariablespresentationsController integration test stubs"""

    def test_datasetspecification_id_variablepresentations_get(self):
        """Test case for datasetspecification_id_variablepresentations_get

        List variable presentations related with a datasetspecification
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.2/datasetspecification/{id}/variablepresentations'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
