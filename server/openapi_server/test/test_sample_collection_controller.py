# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.sample_collection import SampleCollection  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSampleCollectionController(BaseTestCase):
    """SampleCollectionController integration test stubs"""

    def test_samplecollections_get(self):
        """Test case for samplecollections_get

        List all instances of SampleCollection
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/samplecollections',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_samplecollections_id_delete(self):
        """Test case for samplecollections_id_delete

        Delete an existing SampleCollection
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/samplecollections/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_samplecollections_id_get(self):
        """Test case for samplecollections_id_get

        Get a single SampleCollection by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/samplecollections/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_samplecollections_id_put(self):
        """Test case for samplecollections_id_put

        Update an existing SampleCollection
        """
        sample_collection = {
  "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
  "hasPart" : [ {
    "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ]
  }, {
    "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ]
  } ],
  "description" : [ "description", "description" ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ],
  "value" : [ "", "" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/samplecollections/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(sample_collection),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_samplecollections_post(self):
        """Test case for samplecollections_post

        Create one SampleCollection
        """
        sample_collection = {
  "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
  "hasPart" : [ {
    "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ]
  }, {
    "dataCatalogIdentifier" : [ "dataCatalogIdentifier", "dataCatalogIdentifier" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ]
  } ],
  "description" : [ "description", "description" ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ],
  "value" : [ "", "" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/samplecollections'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(sample_collection),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
