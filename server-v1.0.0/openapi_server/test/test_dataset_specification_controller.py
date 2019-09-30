# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.dataset_specification import DatasetSpecification  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDatasetSpecificationController(BaseTestCase):
    """DatasetSpecificationController integration test stubs"""

    def test_datasetspecifications_get(self):
        """Test case for datasetspecifications_get

        List all DatasetSpecification entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/datasetspecifications',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datasetspecifications_id_delete(self):
        """Test case for datasetspecifications_id_delete

        Delete a DatasetSpecification
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/datasetspecifications/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datasetspecifications_id_get(self):
        """Test case for datasetspecifications_id_get

        Get a DatasetSpecification
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/datasetspecifications/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datasetspecifications_id_put(self):
        """Test case for datasetspecifications_id_put

        Update a DatasetSpecification
        """
        dataset_specification = {
  "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
  "hasFormat" : [ "hasFormat", "hasFormat" ],
  "hasFileStructure" : "{}",
  "hasPresentation" : [ {
    "hasDefaultValue" : [ "{}", "{}" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "{}", "{}" ],
    "hasStandardVariable" : [ {
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ],
    "hasMaximumAcceptedValue" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "id" : "id",
    "label" : "label",
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
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ],
    "hasMaximumAcceptedValue" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "id" : "id",
    "label" : "label",
    "partOfDataset" : [ null, null ],
    "type" : [ "type", "type" ],
    "usesUnit" : [ "{}", "{}" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ]
  } ],
  "position" : [ 6.027456183070403, 6.027456183070403 ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ],
  "hasFixedResource" : [ {
    "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/datasetspecifications/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(dataset_specification),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_datasetspecifications_post(self):
        """Test case for datasetspecifications_post

        Create a DatasetSpecification
        """
        dataset_specification = {
  "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
  "hasFormat" : [ "hasFormat", "hasFormat" ],
  "hasFileStructure" : "{}",
  "hasPresentation" : [ {
    "hasDefaultValue" : [ "{}", "{}" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "{}", "{}" ],
    "hasStandardVariable" : [ {
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ],
    "hasMaximumAcceptedValue" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "id" : "id",
    "label" : "label",
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
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ],
    "hasMaximumAcceptedValue" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "id" : "id",
    "label" : "label",
    "partOfDataset" : [ null, null ],
    "type" : [ "type", "type" ],
    "usesUnit" : [ "{}", "{}" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ]
  } ],
  "position" : [ 6.027456183070403, 6.027456183070403 ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ],
  "hasFixedResource" : [ {
    "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/datasetspecifications'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(dataset_specification),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
