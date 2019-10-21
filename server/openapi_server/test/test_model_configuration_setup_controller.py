# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: E501
from openapi_server.test import BaseTestCase


class TestModelConfigurationSetupController(BaseTestCase):
    """ModelConfigurationSetupController integration test stubs"""

    def test_modelconfigurationsetups_get(self):
        """Test case for modelconfigurationsetups_get

        List all ModelConfigurationSetup entities
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/modelconfigurationsetups',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_id_delete(self):
        """Test case for modelconfigurationsetups_id_delete

        Delete a ModelConfigurationSetup
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/modelconfigurationsetups/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_id_get(self):
        """Test case for modelconfigurationsetups_id_get

        Get a ModelConfigurationSetup
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.2.0/modelconfigurationsetups/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_id_put(self):
        """Test case for modelconfigurationsetups_id_put

        Update a ModelConfigurationSetup
        """
        model_configuration_setup = {
  "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
  "keywords" : [ "keywords", "keywords" ],
  "hasGrid" : [ {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "description" : [ "description", "description" ],
    "hasPresentation" : [ "{}", "{}" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  }, {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "description" : [ "description", "description" ],
    "hasPresentation" : [ "{}", "{}" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  } ],
  "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
  "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
  "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
  "type" : [ "type", "type" ],
  "calibratedVariable" : [ "{}", "{}" ],
  "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
  "compatibleVisualizationSoftware" : [ "{}", "{}" ],
  "calibrationMethod" : [ "calibrationMethod", "calibrationMethod" ],
  "hasRegion" : [ {
    "geo" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "geo" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
  "hasContactPerson" : [ "{}", "{}" ],
  "logo" : [ "{}", "{}" ],
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
  "hasSetup" : [ "{}", "{}" ],
  "hasExplanationDiagram" : [ "{}", "{}" ],
  "hasExample" : [ "hasExample", "hasExample" ],
  "calibrationInterval" : [ "calibrationInterval", "calibrationInterval" ],
  "publisher" : [ "{}", "{}" ],
  "hasOutput" : [ "{}", "{}" ],
  "hasOutputTimeInterval" : [ {
    "intervalUnit" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "intervalValue" : [ 0.8008281904610115, 0.8008281904610115 ]
  }, {
    "intervalUnit" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "intervalValue" : [ 0.8008281904610115, 0.8008281904610115 ]
  } ],
  "parameterAssignmentMethod" : [ "parameterAssignmentMethod", "parameterAssignmentMethod" ],
  "hasFunding" : [ "{}", "{}" ],
  "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
  "hasProcess" : [ {
    "influences" : [ null, null ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "influences" : [ null, null ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "supportDetails" : [ "supportDetails", "supportDetails" ],
  "hasVersion" : [ "{}", "{}" ],
  "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
  "description" : [ "description", "description" ],
  "referencePublication" : [ "referencePublication", "referencePublication" ],
  "screenshot" : [ "{}", "{}" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ],
  "hadPrimarySource" : [ "{}", "{}" ],
  "hasSoftwareImage" : [ "{}", "{}" ],
  "dateCreated" : [ "dateCreated", "dateCreated" ],
  "contributor" : [ "{}", "{}" ],
  "hasModelResultTable" : [ "hasModelResultTable", "hasModelResultTable" ],
  "calibrationTargetVariable" : [ "{}", "{}" ],
  "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
  "hasSampleVisualization" : [ "{}", "{}" ],
  "hasCausalDiagram" : [ {
    "hasPart" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "hasPart" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
  "website" : [ "website", "website" ],
  "citation" : [ "citation", "citation" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "adjustableParameter" : [ "{}", "{}" ],
  "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
  "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
  "label" : [ "label", "label" ],
  "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
  "hasParameter" : [ "{}", "{}" ],
  "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
  "validUntil" : [ "validUntil", "validUntil" ],
  "hasEquation" : [ {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "hasInput" : [ "{}", "{}" ],
  "usefulForCalculatingIndex" : [ {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/modelconfigurationsetups/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(model_configuration_setup),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_post(self):
        """Test case for modelconfigurationsetups_post

        Create a ModelConfigurationSetup
        """
        model_configuration_setup = {
  "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
  "keywords" : [ "keywords", "keywords" ],
  "hasGrid" : [ {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "description" : [ "description", "description" ],
    "hasPresentation" : [ "{}", "{}" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  }, {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "description" : [ "description", "description" ],
    "hasPresentation" : [ "{}", "{}" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  } ],
  "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
  "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
  "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
  "type" : [ "type", "type" ],
  "calibratedVariable" : [ "{}", "{}" ],
  "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
  "compatibleVisualizationSoftware" : [ "{}", "{}" ],
  "calibrationMethod" : [ "calibrationMethod", "calibrationMethod" ],
  "hasRegion" : [ {
    "geo" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "geo" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
  "hasContactPerson" : [ "{}", "{}" ],
  "logo" : [ "{}", "{}" ],
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
  "hasSetup" : [ "{}", "{}" ],
  "hasExplanationDiagram" : [ "{}", "{}" ],
  "hasExample" : [ "hasExample", "hasExample" ],
  "calibrationInterval" : [ "calibrationInterval", "calibrationInterval" ],
  "publisher" : [ "{}", "{}" ],
  "hasOutput" : [ "{}", "{}" ],
  "hasOutputTimeInterval" : [ {
    "intervalUnit" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "intervalValue" : [ 0.8008281904610115, 0.8008281904610115 ]
  }, {
    "intervalUnit" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "intervalValue" : [ 0.8008281904610115, 0.8008281904610115 ]
  } ],
  "parameterAssignmentMethod" : [ "parameterAssignmentMethod", "parameterAssignmentMethod" ],
  "hasFunding" : [ "{}", "{}" ],
  "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
  "hasProcess" : [ {
    "influences" : [ null, null ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "influences" : [ null, null ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "supportDetails" : [ "supportDetails", "supportDetails" ],
  "hasVersion" : [ "{}", "{}" ],
  "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
  "description" : [ "description", "description" ],
  "referencePublication" : [ "referencePublication", "referencePublication" ],
  "screenshot" : [ "{}", "{}" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ],
  "hadPrimarySource" : [ "{}", "{}" ],
  "hasSoftwareImage" : [ "{}", "{}" ],
  "dateCreated" : [ "dateCreated", "dateCreated" ],
  "contributor" : [ "{}", "{}" ],
  "hasModelResultTable" : [ "hasModelResultTable", "hasModelResultTable" ],
  "calibrationTargetVariable" : [ "{}", "{}" ],
  "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
  "hasSampleVisualization" : [ "{}", "{}" ],
  "hasCausalDiagram" : [ {
    "hasPart" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "hasPart" : [ "{}", "{}" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
  "website" : [ "website", "website" ],
  "citation" : [ "citation", "citation" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "adjustableParameter" : [ "{}", "{}" ],
  "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
  "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
  "label" : [ "label", "label" ],
  "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
  "hasParameter" : [ "{}", "{}" ],
  "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
  "validUntil" : [ "validUntil", "validUntil" ],
  "hasEquation" : [ {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "hasInput" : [ "{}", "{}" ],
  "usefulForCalculatingIndex" : [ {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.2.0/modelconfigurationsetups'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(model_configuration_setup),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
