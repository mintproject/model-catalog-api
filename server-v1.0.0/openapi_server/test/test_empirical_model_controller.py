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

        List all EmpiricalModel entities
        """
        query_string = [('username', 'username_example'),
                        ('query_text', 'query_text_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/empiricalmodels',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empiricalmodels_id_delete(self):
        """Test case for empiricalmodels_id_delete

        Delete a EmpiricalModel
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/empiricalmodels/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empiricalmodels_id_get(self):
        """Test case for empiricalmodels_id_get

        Get a EmpiricalModel
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/empiricalmodels/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empiricalmodels_id_put(self):
        """Test case for empiricalmodels_id_put

        Update a EmpiricalModel
        """
        empirical_model = {
  "keywords" : [ "keywords", "keywords" ],
  "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
  "hasGrid" : [ {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : "label",
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  }, {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : "label",
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  } ],
  "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
  "hasVersion" : [ "{}", "{}" ],
  "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
  "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
  "referencePublication" : [ "referencePublication", "referencePublication" ],
  "description" : [ "description", "description" ],
  "screenshot" : [ "{}", "{}" ],
  "type" : [ "type", "type" ],
  "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ],
  "dateCreated" : [ "dateCreated", "dateCreated" ],
  "contributor" : [ "{}", "{}" ],
  "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
  "logo" : [ "{}", "{}" ],
  "hasContactPerson" : [ "{}", "{}" ],
  "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
  "id" : "id",
  "hasSampleVisualization" : [ "{}", "{}" ],
  "identifier" : [ "identifier", "identifier" ],
  "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
  "website" : [ "website", "website" ],
  "citation" : [ "citation", "citation" ],
  "author" : [ "{}", "{}" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "shortDescription" : [ "shortDescription", "shortDescription" ],
  "label" : "label",
  "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
  "datePublished" : [ "datePublished", "datePublished" ],
  "license" : [ "license", "license" ],
  "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
  "hasSourceCode" : [ "{}", "{}" ],
  "hasExplanationDiagram" : [ "{}", "{}" ],
  "hasEquation" : [ {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "publisher" : [ "{}", "{}" ],
  "fundingSource" : [ "{}", "{}" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/empiricalmodels/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(empirical_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empiricalmodels_post(self):
        """Test case for empiricalmodels_post

        Create a EmpiricalModel
        """
        empirical_model = {
  "keywords" : [ "keywords", "keywords" ],
  "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
  "hasGrid" : [ {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : "label",
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  }, {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : "label",
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  } ],
  "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
  "hasVersion" : [ "{}", "{}" ],
  "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
  "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
  "referencePublication" : [ "referencePublication", "referencePublication" ],
  "description" : [ "description", "description" ],
  "screenshot" : [ "{}", "{}" ],
  "type" : [ "type", "type" ],
  "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ],
  "dateCreated" : [ "dateCreated", "dateCreated" ],
  "contributor" : [ "{}", "{}" ],
  "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
  "logo" : [ "{}", "{}" ],
  "hasContactPerson" : [ "{}", "{}" ],
  "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
  "id" : "id",
  "hasSampleVisualization" : [ "{}", "{}" ],
  "identifier" : [ "identifier", "identifier" ],
  "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
  "website" : [ "website", "website" ],
  "citation" : [ "citation", "citation" ],
  "author" : [ "{}", "{}" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "shortDescription" : [ "shortDescription", "shortDescription" ],
  "label" : "label",
  "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
  "datePublished" : [ "datePublished", "datePublished" ],
  "license" : [ "license", "license" ],
  "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
  "hasSourceCode" : [ "{}", "{}" ],
  "hasExplanationDiagram" : [ "{}", "{}" ],
  "hasEquation" : [ {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "publisher" : [ "{}", "{}" ],
  "fundingSource" : [ "{}", "{}" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/empiricalmodels'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(empirical_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
