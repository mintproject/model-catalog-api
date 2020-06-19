# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.point_based_grid import PointBasedGrid  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPointBasedGridController(BaseTestCase):
    """PointBasedGridController integration test stubs"""

    def test_pointbasedgrids_get(self):
        """Test case for pointbasedgrids_get

        List all instances of PointBasedGrid
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/pointbasedgrids',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pointbasedgrids_id_delete(self):
        """Test case for pointbasedgrids_id_delete

        Delete an existing PointBasedGrid
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/pointbasedgrids/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pointbasedgrids_id_get(self):
        """Test case for pointbasedgrids_id_get

        Get a single PointBasedGrid by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/pointbasedgrids/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pointbasedgrids_id_put(self):
        """Test case for pointbasedgrids_id_put

        Update an existing PointBasedGrid
        """
        point_based_grid = {
  "hasDimensionality" : [ 0, 0 ],
  "hasFormat" : [ "hasFormat", "hasFormat" ],
  "hasFileStructure" : [ "{}", "{}" ],
  "description" : [ "description", "description" ],
  "hasPresentation" : [ {
    "hasDefaultValue" : [ "", "" ],
    "hasStandardVariable" : [ {
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
    "hasMaximumAcceptedValue" : [ "", "" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "description" : [ "description", "description" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "", "" ],
    "id" : "id",
    "partOfDataset" : [ {
      "hasDimensionality" : [ 6, 6 ],
      "hasFormat" : [ "hasFormat", "hasFormat" ],
      "hasFileStructure" : [ "{}", "{}" ],
      "description" : [ "description", "description" ],
      "hasPresentation" : [ null, null ],
      "position" : [ 1, 1 ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasFixedResource" : [ {
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
      } ]
    }, {
      "hasDimensionality" : [ 6, 6 ],
      "hasFormat" : [ "hasFormat", "hasFormat" ],
      "hasFileStructure" : [ "{}", "{}" ],
      "description" : [ "description", "description" ],
      "hasPresentation" : [ null, null ],
      "position" : [ 1, 1 ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasFixedResource" : [ {
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
      } ]
    } ],
    "usesUnit" : [ {
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
  }, {
    "hasDefaultValue" : [ "", "" ],
    "hasStandardVariable" : [ {
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
    "hasMaximumAcceptedValue" : [ "", "" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "description" : [ "description", "description" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "", "" ],
    "id" : "id",
    "partOfDataset" : [ {
      "hasDimensionality" : [ 6, 6 ],
      "hasFormat" : [ "hasFormat", "hasFormat" ],
      "hasFileStructure" : [ "{}", "{}" ],
      "description" : [ "description", "description" ],
      "hasPresentation" : [ null, null ],
      "position" : [ 1, 1 ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasFixedResource" : [ {
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
      } ]
    }, {
      "hasDimensionality" : [ 6, 6 ],
      "hasFormat" : [ "hasFormat", "hasFormat" ],
      "hasFileStructure" : [ "{}", "{}" ],
      "description" : [ "description", "description" ],
      "hasPresentation" : [ null, null ],
      "position" : [ 1, 1 ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasFixedResource" : [ {
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
      } ]
    } ],
    "usesUnit" : [ {
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
  } ],
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ],
  "hasFixedResource" : [ {
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
  "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
  "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
  "hasShape" : [ "hasShape", "hasShape" ],
  "hasDimension" : [ "hasDimension", "hasDimension" ],
  "position" : [ 6, 6 ],
  "id" : "id"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/pointbasedgrids/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(point_based_grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pointbasedgrids_post(self):
        """Test case for pointbasedgrids_post

        Create one PointBasedGrid
        """
        point_based_grid = {
  "hasDimensionality" : [ 0, 0 ],
  "hasFormat" : [ "hasFormat", "hasFormat" ],
  "hasFileStructure" : [ "{}", "{}" ],
  "description" : [ "description", "description" ],
  "hasPresentation" : [ {
    "hasDefaultValue" : [ "", "" ],
    "hasStandardVariable" : [ {
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
    "hasMaximumAcceptedValue" : [ "", "" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "description" : [ "description", "description" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "", "" ],
    "id" : "id",
    "partOfDataset" : [ {
      "hasDimensionality" : [ 6, 6 ],
      "hasFormat" : [ "hasFormat", "hasFormat" ],
      "hasFileStructure" : [ "{}", "{}" ],
      "description" : [ "description", "description" ],
      "hasPresentation" : [ null, null ],
      "position" : [ 1, 1 ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasFixedResource" : [ {
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
      } ]
    }, {
      "hasDimensionality" : [ 6, 6 ],
      "hasFormat" : [ "hasFormat", "hasFormat" ],
      "hasFileStructure" : [ "{}", "{}" ],
      "description" : [ "description", "description" ],
      "hasPresentation" : [ null, null ],
      "position" : [ 1, 1 ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasFixedResource" : [ {
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
      } ]
    } ],
    "usesUnit" : [ {
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
  }, {
    "hasDefaultValue" : [ "", "" ],
    "hasStandardVariable" : [ {
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
    "hasMaximumAcceptedValue" : [ "", "" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "description" : [ "description", "description" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasLongName" : [ "hasLongName", "hasLongName" ],
    "hasShortName" : [ "hasShortName", "hasShortName" ],
    "hasMinimumAcceptedValue" : [ "", "" ],
    "id" : "id",
    "partOfDataset" : [ {
      "hasDimensionality" : [ 6, 6 ],
      "hasFormat" : [ "hasFormat", "hasFormat" ],
      "hasFileStructure" : [ "{}", "{}" ],
      "description" : [ "description", "description" ],
      "hasPresentation" : [ null, null ],
      "position" : [ 1, 1 ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasFixedResource" : [ {
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
      } ]
    }, {
      "hasDimensionality" : [ 6, 6 ],
      "hasFormat" : [ "hasFormat", "hasFormat" ],
      "hasFileStructure" : [ "{}", "{}" ],
      "description" : [ "description", "description" ],
      "hasPresentation" : [ null, null ],
      "position" : [ 1, 1 ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasFixedResource" : [ {
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
      } ]
    } ],
    "usesUnit" : [ {
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
  } ],
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ],
  "hasFixedResource" : [ {
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
  "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
  "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
  "hasShape" : [ "hasShape", "hasShape" ],
  "hasDimension" : [ "hasDimension", "hasDimension" ],
  "position" : [ 6, 6 ],
  "id" : "id"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/pointbasedgrids'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(point_based_grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
