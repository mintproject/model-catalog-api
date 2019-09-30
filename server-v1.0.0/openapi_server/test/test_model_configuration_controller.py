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
        query_string = [('username', 'username_example')]
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
  "parameterAssignmentMethod" : [ "parameterAssignmentMethod", "parameterAssignmentMethod" ],
  "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
  "hasGrid" : [ {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : "label",
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
    "hasPresentation" : [ "{}", "{}" ],
    "label" : "label",
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  } ],
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
  "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
  "type" : [ "type", "type" ],
  "calibratedVariable" : [ "{}", "{}" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ],
  "hasSoftwareImage" : [ "{}", "{}" ],
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
  "hasModelResultTable" : [ "hasModelResultTable", "hasModelResultTable" ],
  "calibrationTargetVariable" : [ "{}", "{}" ],
  "id" : "id",
  "hasExpertTunedModel" : [ null, null ],
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
  "hasSampleExecution" : [ "{}", "{}" ],
  "hasSampleResult" : [ "{}", "{}" ],
  "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
  "adjustableParameter" : [ "{}", "{}" ],
  "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
  "label" : "label",
  "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
  "hasParameter" : [ "{}", "{}" ],
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
  "hasOutput" : [ "{}", "{}" ],
  "hasOutputTimeInterval" : [ {
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
  "parameterAssignmentMethod" : [ "parameterAssignmentMethod", "parameterAssignmentMethod" ],
  "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
  "hasGrid" : [ {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : "label",
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
    "hasPresentation" : [ "{}", "{}" ],
    "label" : "label",
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : "id"
  } ],
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
  "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
  "type" : [ "type", "type" ],
  "calibratedVariable" : [ "{}", "{}" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ],
  "hasSoftwareImage" : [ "{}", "{}" ],
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
  "hasModelResultTable" : [ "hasModelResultTable", "hasModelResultTable" ],
  "calibrationTargetVariable" : [ "{}", "{}" ],
  "id" : "id",
  "hasExpertTunedModel" : [ null, null ],
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
  "hasSampleExecution" : [ "{}", "{}" ],
  "hasSampleResult" : [ "{}", "{}" ],
  "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
  "adjustableParameter" : [ "{}", "{}" ],
  "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
  "label" : "label",
  "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
  "hasParameter" : [ "{}", "{}" ],
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
  "hasOutput" : [ "{}", "{}" ],
  "hasOutputTimeInterval" : [ {
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
