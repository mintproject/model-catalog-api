# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.software_image import SoftwareImage  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSoftwareImageController(BaseTestCase):
    """SoftwareImageController integration test stubs"""

    def test_softwareimages_get(self):
        """Test case for softwareimages_get

        List all instances of SoftwareImage
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/softwareimages',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareimages_id_delete(self):
        """Test case for softwareimages_id_delete

        Delete an existing SoftwareImage
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/softwareimages/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareimages_id_get(self):
        """Test case for softwareimages_id_get

        Get a single SoftwareImage by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/softwareimages/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareimages_id_put(self):
        """Test case for softwareimages_id_put

        Update an existing SoftwareImage
        """
        software_image = {
  "hasFunding" : [ {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "fundingSource" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    } ],
    "fundingGrant" : [ "fundingGrant", "fundingGrant" ]
  }, {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "fundingSource" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    } ],
    "fundingGrant" : [ "fundingGrant", "fundingGrant" ]
  } ],
  "keywords" : [ "keywords", "keywords" ],
  "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
  "supportDetails" : [ "supportDetails", "supportDetails" ],
  "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
  "hasVersion" : [ null, null ],
  "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
  "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
  "description" : [ "description", "description" ],
  "referencePublication" : [ "referencePublication", "referencePublication" ],
  "screenshot" : [ {
    "hasDimensionality" : [ 0, 0 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
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
    "position" : [ 5, 5 ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ],
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
    "hasDimensionality" : [ 0, 0 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
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
    "position" : [ 5, 5 ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ],
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
  "type" : [ "type", "type" ],
  "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
  "hadPrimarySource" : [ "{}", "{}" ],
  "dateCreated" : [ "dateCreated", "dateCreated" ],
  "contributor" : [ {
    "identifier" : [ "identifier", "identifier" ],
    "website" : [ "website", "website" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "email" : [ "email", "email" ]
  }, {
    "identifier" : [ "identifier", "identifier" ],
    "website" : [ "website", "website" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "email" : [ "email", "email" ]
  } ],
  "compatibleVisualizationSoftware" : [ null, null ],
  "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
  "logo" : [ {
    "hasDimensionality" : [ 0, 0 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
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
    "position" : [ 5, 5 ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ],
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
    "hasDimensionality" : [ 0, 0 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
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
    "position" : [ 5, 5 ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ],
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
  "hasContactPerson" : [ "{}", "{}" ],
  "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
  "id" : "id",
  "hasSampleVisualization" : [ {
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
    "wasDerivedFromSoftware" : [ null, null ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ]
  }, {
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
    "wasDerivedFromSoftware" : [ null, null ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ]
  } ],
  "identifier" : [ "identifier", "identifier" ],
  "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
  "website" : [ "website", "website" ],
  "citation" : [ "citation", "citation" ],
  "author" : [ "{}", "{}" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
  "shortDescription" : [ "shortDescription", "shortDescription" ],
  "label" : [ "label", "label" ],
  "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
  "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
  "datePublished" : [ "datePublished", "datePublished" ],
  "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
  "license" : [ "license", "license" ],
  "hasSourceCode" : [ {
    "license" : [ "license", "license" ],
    "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
    "description" : [ "description", "description" ],
    "codeRepository" : [ "codeRepository", "codeRepository" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "license" : [ "license", "license" ],
    "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
    "description" : [ "description", "description" ],
    "codeRepository" : [ "codeRepository", "codeRepository" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "hasExample" : [ "hasExample", "hasExample" ],
  "publisher" : [ "{}", "{}" ],
  "usefulForCalculatingIndex" : [ {
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
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
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
            '/v1.5.0/softwareimages/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(software_image),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareimages_post(self):
        """Test case for softwareimages_post

        Create one SoftwareImage
        """
        software_image = {
  "hasFunding" : [ {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "fundingSource" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    } ],
    "fundingGrant" : [ "fundingGrant", "fundingGrant" ]
  }, {
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "fundingSource" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ]
    } ],
    "fundingGrant" : [ "fundingGrant", "fundingGrant" ]
  } ],
  "keywords" : [ "keywords", "keywords" ],
  "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
  "supportDetails" : [ "supportDetails", "supportDetails" ],
  "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
  "hasVersion" : [ null, null ],
  "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
  "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
  "description" : [ "description", "description" ],
  "referencePublication" : [ "referencePublication", "referencePublication" ],
  "screenshot" : [ {
    "hasDimensionality" : [ 0, 0 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
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
    "position" : [ 5, 5 ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ],
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
    "hasDimensionality" : [ 0, 0 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
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
    "position" : [ 5, 5 ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ],
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
  "type" : [ "type", "type" ],
  "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
  "hadPrimarySource" : [ "{}", "{}" ],
  "dateCreated" : [ "dateCreated", "dateCreated" ],
  "contributor" : [ {
    "identifier" : [ "identifier", "identifier" ],
    "website" : [ "website", "website" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "email" : [ "email", "email" ]
  }, {
    "identifier" : [ "identifier", "identifier" ],
    "website" : [ "website", "website" ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "email" : [ "email", "email" ]
  } ],
  "compatibleVisualizationSoftware" : [ null, null ],
  "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
  "logo" : [ {
    "hasDimensionality" : [ 0, 0 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
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
    "position" : [ 5, 5 ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ],
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
    "hasDimensionality" : [ 0, 0 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
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
    "position" : [ 5, 5 ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ],
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
  "hasContactPerson" : [ "{}", "{}" ],
  "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
  "id" : "id",
  "hasSampleVisualization" : [ {
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
    "wasDerivedFromSoftware" : [ null, null ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ]
  }, {
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hadPrimarySource" : [ "{}", "{}" ],
    "wasDerivedFromSoftware" : [ null, null ],
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "value" : [ "", "" ]
  } ],
  "identifier" : [ "identifier", "identifier" ],
  "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
  "website" : [ "website", "website" ],
  "citation" : [ "citation", "citation" ],
  "author" : [ "{}", "{}" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
  "shortDescription" : [ "shortDescription", "shortDescription" ],
  "label" : [ "label", "label" ],
  "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
  "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
  "datePublished" : [ "datePublished", "datePublished" ],
  "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
  "license" : [ "license", "license" ],
  "hasSourceCode" : [ {
    "license" : [ "license", "license" ],
    "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
    "description" : [ "description", "description" ],
    "codeRepository" : [ "codeRepository", "codeRepository" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "license" : [ "license", "license" ],
    "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
    "description" : [ "description", "description" ],
    "codeRepository" : [ "codeRepository", "codeRepository" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "hasExample" : [ "hasExample", "hasExample" ],
  "publisher" : [ "{}", "{}" ],
  "usefulForCalculatingIndex" : [ {
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
    "description" : [ "description", "description" ],
    "id" : "id",
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
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
            '/v1.5.0/softwareimages'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(software_image),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
