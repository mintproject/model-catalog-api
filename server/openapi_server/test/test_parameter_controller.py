# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.parameter import Parameter  # noqa: E501
from openapi_server.test import BaseTestCase


class TestParameterController(BaseTestCase):
    """ParameterController integration test stubs"""

    def test_parameters_get(self):
        """Test case for parameters_get

        List all Parameter entities
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/parameters',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parameters_id_delete(self):
        """Test case for parameters_id_delete

        Delete a Parameter
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/parameters/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parameters_id_get(self):
        """Test case for parameters_id_get

        Get a Parameter
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/parameters/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parameters_id_put(self):
        """Test case for parameters_id_put

        Update a Parameter
        """
        parameter = {
  "hasDefaultValue" : [ "{}", "{}" ],
  "hasMinimumAcceptedValue" : [ "{}", "{}" ],
  "hasMaximumAcceptedValue" : [ "{}", "{}" ],
  "adjustsVariable" : [ "{}", "{}" ],
  "hasDataType" : [ "hasDataType", "hasDataType" ],
  "hasFixedValue" : [ "{}", "{}" ],
  "hasPresentation" : [ {
    "hasDefaultValue" : [ "{}", "{}" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "{}", "{}" ],
    "hasStandardVariable" : [ {
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    }, {
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    } ],
    "hasMaximumAcceptedValue" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "partOfDataset" : [ null, null ],
    "type" : [ "type", "type" ],
    "usesUnit" : [ "{}", "{}" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ]
  }, {
    "hasDefaultValue" : [ "{}", "{}" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "{}", "{}" ],
    "hasStandardVariable" : [ {
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    }, {
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    } ],
    "hasMaximumAcceptedValue" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "partOfDataset" : [ null, null ],
    "type" : [ "type", "type" ],
    "usesUnit" : [ "{}", "{}" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ]
  } ],
  "position" : [ 0.8008281904610115, 0.8008281904610115 ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/parameters/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(parameter),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parameters_post(self):
        """Test case for parameters_post

        Create a Parameter
        """
        parameter = {
  "hasDefaultValue" : [ "{}", "{}" ],
  "hasMinimumAcceptedValue" : [ "{}", "{}" ],
  "hasMaximumAcceptedValue" : [ "{}", "{}" ],
  "adjustsVariable" : [ "{}", "{}" ],
  "hasDataType" : [ "hasDataType", "hasDataType" ],
  "hasFixedValue" : [ "{}", "{}" ],
  "hasPresentation" : [ {
    "hasDefaultValue" : [ "{}", "{}" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "{}", "{}" ],
    "hasStandardVariable" : [ {
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    }, {
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    } ],
    "hasMaximumAcceptedValue" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "partOfDataset" : [ null, null ],
    "type" : [ "type", "type" ],
    "usesUnit" : [ "{}", "{}" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ]
  }, {
    "hasDefaultValue" : [ "{}", "{}" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "{}", "{}" ],
    "hasStandardVariable" : [ {
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    }, {
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    } ],
    "hasMaximumAcceptedValue" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "partOfDataset" : [ null, null ],
    "type" : [ "type", "type" ],
    "usesUnit" : [ "{}", "{}" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ]
  } ],
  "position" : [ 0.8008281904610115, 0.8008281904610115 ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/parameters'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(parameter),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
