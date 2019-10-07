# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModelConfigurationController(BaseTestCase):
    """ModelConfigurationController integration test stubs"""

    def test_modelconfigurations_get(self):
        """Test case for modelconfigurations_get

        List all ModelConfiguration entities
        """
        query_string = [('username', 'username_example'),
                        ('query_text', 'query_text_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/modelconfigurations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_id_delete(self):
        """Test case for modelconfigurations_id_delete

        Delete a ModelConfiguration
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/modelconfigurations/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_id_get(self):
        """Test case for modelconfigurations_id_get

        Get a ModelConfiguration
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/modelconfigurations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_id_put(self):
        """Test case for modelconfigurations_id_put

        Update a ModelConfiguration
        """
        model_configuration = {
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
  "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
  "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
  "type" : [ "type", "type" ],
  "calibratedVariable" : [ "{}", "{}" ],
  "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
  "compatibleVisualizationSoftware" : [ "{}", "{}" ],
  "calibrationMethod" : [ "calibrationMethod", "calibrationMethod" ],
  "hasRegion" : [ {
    "geo" : [ "{}", "{}" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "geo" : [ "{}", "{}" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
  "logo" : [ "{}", "{}" ],
  "hasContactPerson" : [ "{}", "{}" ],
  "id" : "id",
  "identifier" : [ "identifier", "identifier" ],
  "hasSampleExecution" : [ "{}", "{}" ],
  "hasSampleResult" : [ "{}", "{}" ],
  "author" : [ "{}", "{}" ],
  "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
  "shortDescription" : [ "shortDescription", "shortDescription" ],
  "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
  "datePublished" : [ "datePublished", "datePublished" ],
  "license" : [ "license", "license" ],
  "hasSourceCode" : [ "{}", "{}" ],
  "hasExplanationDiagram" : [ "{}", "{}" ],
  "publisher" : [ "{}", "{}" ],
  "hasOutput" : [ "{}", "{}" ],
  "fundingSource" : [ "{}", "{}" ],
  "hasOutputTimeInterval" : [ {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "parameterAssignmentMethod" : [ "parameterAssignmentMethod", "parameterAssignmentMethod" ],
  "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
  "hasProcess" : [ {
    "influences" : [ null, null ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "influences" : [ null, null ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "hasVersion" : [ "{}", "{}" ],
  "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
  "referencePublication" : [ "referencePublication", "referencePublication" ],
  "description" : [ "description", "description" ],
  "screenshot" : [ "{}", "{}" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ],
  "hasSoftwareImage" : [ "{}", "{}" ],
  "dateCreated" : [ "dateCreated", "dateCreated" ],
  "contributor" : [ "{}", "{}" ],
  "hasModelResultTable" : [ "hasModelResultTable", "hasModelResultTable" ],
  "calibrationTargetVariable" : [ "{}", "{}" ],
  "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
  "hasExpertTunedModel" : [ null, null ],
  "hasSampleVisualization" : [ "{}", "{}" ],
  "hasCalibration" : [ null, null ],
  "hasCausalDiagram" : [ {
    "hasPart" : [ "{}", "{}" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "hasPart" : [ "{}", "{}" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
  "website" : [ "website", "website" ],
  "citation" : [ "citation", "citation" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "adjustableParameter" : [ "{}", "{}" ],
  "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
  "label" : "label",
  "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
  "hasParameter" : [ "{}", "{}" ],
  "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
  "hasEquation" : [ {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "hasInput" : [ "{}", "{}" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/modelconfigurations/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(model_configuration),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_post(self):
        """Test case for modelconfigurations_post

        Create a ModelConfiguration
        """
        model_configuration = {
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
  "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
  "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
  "type" : [ "type", "type" ],
  "calibratedVariable" : [ "{}", "{}" ],
  "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
  "compatibleVisualizationSoftware" : [ "{}", "{}" ],
  "calibrationMethod" : [ "calibrationMethod", "calibrationMethod" ],
  "hasRegion" : [ {
    "geo" : [ "{}", "{}" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "geo" : [ "{}", "{}" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
  "logo" : [ "{}", "{}" ],
  "hasContactPerson" : [ "{}", "{}" ],
  "id" : "id",
  "identifier" : [ "identifier", "identifier" ],
  "hasSampleExecution" : [ "{}", "{}" ],
  "hasSampleResult" : [ "{}", "{}" ],
  "author" : [ "{}", "{}" ],
  "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
  "shortDescription" : [ "shortDescription", "shortDescription" ],
  "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
  "datePublished" : [ "datePublished", "datePublished" ],
  "license" : [ "license", "license" ],
  "hasSourceCode" : [ "{}", "{}" ],
  "hasExplanationDiagram" : [ "{}", "{}" ],
  "publisher" : [ "{}", "{}" ],
  "hasOutput" : [ "{}", "{}" ],
  "fundingSource" : [ "{}", "{}" ],
  "hasOutputTimeInterval" : [ {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "parameterAssignmentMethod" : [ "parameterAssignmentMethod", "parameterAssignmentMethod" ],
  "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
  "hasProcess" : [ {
    "influences" : [ null, null ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "influences" : [ null, null ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "hasVersion" : [ "{}", "{}" ],
  "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
  "referencePublication" : [ "referencePublication", "referencePublication" ],
  "description" : [ "description", "description" ],
  "screenshot" : [ "{}", "{}" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ],
  "hasSoftwareImage" : [ "{}", "{}" ],
  "dateCreated" : [ "dateCreated", "dateCreated" ],
  "contributor" : [ "{}", "{}" ],
  "hasModelResultTable" : [ "hasModelResultTable", "hasModelResultTable" ],
  "calibrationTargetVariable" : [ "{}", "{}" ],
  "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
  "hasExpertTunedModel" : [ null, null ],
  "hasSampleVisualization" : [ "{}", "{}" ],
  "hasCalibration" : [ null, null ],
  "hasCausalDiagram" : [ {
    "hasPart" : [ "{}", "{}" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "hasPart" : [ "{}", "{}" ],
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
  "website" : [ "website", "website" ],
  "citation" : [ "citation", "citation" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "adjustableParameter" : [ "{}", "{}" ],
  "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
  "label" : "label",
  "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
  "hasParameter" : [ "{}", "{}" ],
  "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
  "hasEquation" : [ {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  }, {
    "id" : "id",
    "label" : "label",
    "type" : [ "type", "type" ]
  } ],
  "hasInput" : [ "{}", "{}" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/modelconfigurations'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(model_configuration),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
