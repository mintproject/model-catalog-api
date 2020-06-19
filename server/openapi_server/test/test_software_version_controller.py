# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.software_version import SoftwareVersion  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSoftwareVersionController(BaseTestCase):
    """SoftwareVersionController integration test stubs"""

    def test_softwareversions_get(self):
        """Test case for softwareversions_get

        List all instances of SoftwareVersion
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/softwareversions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareversions_id_delete(self):
        """Test case for softwareversions_id_delete

        Delete an existing SoftwareVersion
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/softwareversions/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareversions_id_get(self):
        """Test case for softwareversions_id_get

        Get a single SoftwareVersion by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/softwareversions/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareversions_id_put(self):
        """Test case for softwareversions_id_put

        Update an existing SoftwareVersion
        """
        software_version = {
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
  "tag" : [ "tag", "tag" ],
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
  "hasConfiguration" : [ {
    "keywords" : [ "keywords", "keywords" ],
    "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
    "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
    "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
    "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
    "type" : [ "type", "type" ],
    "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
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
    "tag" : [ "tag", "tag" ],
    "id" : "id",
    "identifier" : [ "identifier", "identifier" ],
    "hasSampleExecution" : [ {
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
    }, {
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
    } ],
    "hasSampleResult" : [ {
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
    "author" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "shortDescription" : [ "shortDescription", "shortDescription" ],
    "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
    "datePublished" : [ "datePublished", "datePublished" ],
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
    "hasSetup" : [ null, null ],
    "hasExample" : [ "hasExample", "hasExample" ],
    "publisher" : [ "{}", "{}" ],
    "hasOutput" : [ {
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
    "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
    "supportDetails" : [ "supportDetails", "supportDetails" ],
    "hasVersion" : [ null, null ],
    "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
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
    "hadPrimarySource" : [ "{}", "{}" ],
    "hasSoftwareImage" : [ {
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
    }, {
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
    } ],
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
    "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
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
    "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
    "website" : [ "website", "website" ],
    "citation" : [ "citation", "citation" ],
    "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
    "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
    "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
    "label" : [ "label", "label" ],
    "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
    "hasParameter" : [ {
      "hasDefaultValue" : [ "", "" ],
      "hasMaximumAcceptedValue" : [ "", "" ],
      "description" : [ "description", "description" ],
      "hasDataType" : [ "hasDataType", "hasDataType" ],
      "hasFixedValue" : [ "", "" ],
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
      "recommendedIncrement" : [ 5.637376656633329, 5.637376656633329 ],
      "type" : [ "type", "type" ],
      "hasMinimumAcceptedValue" : [ "", "" ],
      "hasAcceptedValues" : [ "hasAcceptedValues", "hasAcceptedValues" ],
      "adjustsVariable" : [ {
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
      "relevantForIntervention" : [ {
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
      "position" : [ 2, 2 ],
      "id" : "id",
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
      } ],
      "hasStepSize" : [ 7.061401241503109, 7.061401241503109 ]
    }, {
      "hasDefaultValue" : [ "", "" ],
      "hasMaximumAcceptedValue" : [ "", "" ],
      "description" : [ "description", "description" ],
      "hasDataType" : [ "hasDataType", "hasDataType" ],
      "hasFixedValue" : [ "", "" ],
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
      "recommendedIncrement" : [ 5.637376656633329, 5.637376656633329 ],
      "type" : [ "type", "type" ],
      "hasMinimumAcceptedValue" : [ "", "" ],
      "hasAcceptedValues" : [ "hasAcceptedValues", "hasAcceptedValues" ],
      "adjustsVariable" : [ {
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
      "relevantForIntervention" : [ {
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
      "position" : [ 2, 2 ],
      "id" : "id",
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
      } ],
      "hasStepSize" : [ 7.061401241503109, 7.061401241503109 ]
    } ],
    "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
    "hasInput" : [ {
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
  }, {
    "keywords" : [ "keywords", "keywords" ],
    "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
    "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
    "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
    "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
    "type" : [ "type", "type" ],
    "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
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
    "tag" : [ "tag", "tag" ],
    "id" : "id",
    "identifier" : [ "identifier", "identifier" ],
    "hasSampleExecution" : [ {
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
    }, {
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
    } ],
    "hasSampleResult" : [ {
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
    "author" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "shortDescription" : [ "shortDescription", "shortDescription" ],
    "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
    "datePublished" : [ "datePublished", "datePublished" ],
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
    "hasSetup" : [ null, null ],
    "hasExample" : [ "hasExample", "hasExample" ],
    "publisher" : [ "{}", "{}" ],
    "hasOutput" : [ {
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
    "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
    "supportDetails" : [ "supportDetails", "supportDetails" ],
    "hasVersion" : [ null, null ],
    "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
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
    "hadPrimarySource" : [ "{}", "{}" ],
    "hasSoftwareImage" : [ {
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
    }, {
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
    } ],
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
    "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
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
    "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
    "website" : [ "website", "website" ],
    "citation" : [ "citation", "citation" ],
    "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
    "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
    "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
    "label" : [ "label", "label" ],
    "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
    "hasParameter" : [ {
      "hasDefaultValue" : [ "", "" ],
      "hasMaximumAcceptedValue" : [ "", "" ],
      "description" : [ "description", "description" ],
      "hasDataType" : [ "hasDataType", "hasDataType" ],
      "hasFixedValue" : [ "", "" ],
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
      "recommendedIncrement" : [ 5.637376656633329, 5.637376656633329 ],
      "type" : [ "type", "type" ],
      "hasMinimumAcceptedValue" : [ "", "" ],
      "hasAcceptedValues" : [ "hasAcceptedValues", "hasAcceptedValues" ],
      "adjustsVariable" : [ {
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
      "relevantForIntervention" : [ {
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
      "position" : [ 2, 2 ],
      "id" : "id",
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
      } ],
      "hasStepSize" : [ 7.061401241503109, 7.061401241503109 ]
    }, {
      "hasDefaultValue" : [ "", "" ],
      "hasMaximumAcceptedValue" : [ "", "" ],
      "description" : [ "description", "description" ],
      "hasDataType" : [ "hasDataType", "hasDataType" ],
      "hasFixedValue" : [ "", "" ],
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
      "recommendedIncrement" : [ 5.637376656633329, 5.637376656633329 ],
      "type" : [ "type", "type" ],
      "hasMinimumAcceptedValue" : [ "", "" ],
      "hasAcceptedValues" : [ "hasAcceptedValues", "hasAcceptedValues" ],
      "adjustsVariable" : [ {
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
      "relevantForIntervention" : [ {
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
      "position" : [ 2, 2 ],
      "id" : "id",
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
      } ],
      "hasStepSize" : [ 7.061401241503109, 7.061401241503109 ]
    } ],
    "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
    "hasInput" : [ {
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
  } ],
  "author" : [ "{}", "{}" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
  "shortDescription" : [ "shortDescription", "shortDescription" ],
  "label" : [ "label", "label" ],
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
  } ],
  "hasVersionId" : [ "hasVersionId", "hasVersionId" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/softwareversions/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(software_version),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_softwareversions_post(self):
        """Test case for softwareversions_post

        Create one SoftwareVersion
        """
        software_version = {
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
  "tag" : [ "tag", "tag" ],
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
  "hasConfiguration" : [ {
    "keywords" : [ "keywords", "keywords" ],
    "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
    "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
    "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
    "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
    "type" : [ "type", "type" ],
    "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
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
    "tag" : [ "tag", "tag" ],
    "id" : "id",
    "identifier" : [ "identifier", "identifier" ],
    "hasSampleExecution" : [ {
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
    }, {
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
    } ],
    "hasSampleResult" : [ {
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
    "author" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "shortDescription" : [ "shortDescription", "shortDescription" ],
    "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
    "datePublished" : [ "datePublished", "datePublished" ],
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
    "hasSetup" : [ null, null ],
    "hasExample" : [ "hasExample", "hasExample" ],
    "publisher" : [ "{}", "{}" ],
    "hasOutput" : [ {
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
    "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
    "supportDetails" : [ "supportDetails", "supportDetails" ],
    "hasVersion" : [ null, null ],
    "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
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
    "hadPrimarySource" : [ "{}", "{}" ],
    "hasSoftwareImage" : [ {
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
    }, {
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
    } ],
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
    "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
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
    "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
    "website" : [ "website", "website" ],
    "citation" : [ "citation", "citation" ],
    "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
    "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
    "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
    "label" : [ "label", "label" ],
    "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
    "hasParameter" : [ {
      "hasDefaultValue" : [ "", "" ],
      "hasMaximumAcceptedValue" : [ "", "" ],
      "description" : [ "description", "description" ],
      "hasDataType" : [ "hasDataType", "hasDataType" ],
      "hasFixedValue" : [ "", "" ],
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
      "recommendedIncrement" : [ 5.637376656633329, 5.637376656633329 ],
      "type" : [ "type", "type" ],
      "hasMinimumAcceptedValue" : [ "", "" ],
      "hasAcceptedValues" : [ "hasAcceptedValues", "hasAcceptedValues" ],
      "adjustsVariable" : [ {
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
      "relevantForIntervention" : [ {
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
      "position" : [ 2, 2 ],
      "id" : "id",
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
      } ],
      "hasStepSize" : [ 7.061401241503109, 7.061401241503109 ]
    }, {
      "hasDefaultValue" : [ "", "" ],
      "hasMaximumAcceptedValue" : [ "", "" ],
      "description" : [ "description", "description" ],
      "hasDataType" : [ "hasDataType", "hasDataType" ],
      "hasFixedValue" : [ "", "" ],
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
      "recommendedIncrement" : [ 5.637376656633329, 5.637376656633329 ],
      "type" : [ "type", "type" ],
      "hasMinimumAcceptedValue" : [ "", "" ],
      "hasAcceptedValues" : [ "hasAcceptedValues", "hasAcceptedValues" ],
      "adjustsVariable" : [ {
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
      "relevantForIntervention" : [ {
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
      "position" : [ 2, 2 ],
      "id" : "id",
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
      } ],
      "hasStepSize" : [ 7.061401241503109, 7.061401241503109 ]
    } ],
    "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
    "hasInput" : [ {
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
  }, {
    "keywords" : [ "keywords", "keywords" ],
    "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
    "hasImplementationScriptLocation" : [ "hasImplementationScriptLocation", "hasImplementationScriptLocation" ],
    "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
    "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
    "type" : [ "type", "type" ],
    "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
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
    "tag" : [ "tag", "tag" ],
    "id" : "id",
    "identifier" : [ "identifier", "identifier" ],
    "hasSampleExecution" : [ {
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
    }, {
      "description" : [ "description", "description" ],
      "id" : "id",
      "label" : [ "label", "label" ],
      "type" : [ "type", "type" ],
      "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ]
    } ],
    "hasSampleResult" : [ {
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
    "author" : [ "{}", "{}" ],
    "hasConstraint" : [ "hasConstraint", "hasConstraint" ],
    "shortDescription" : [ "shortDescription", "shortDescription" ],
    "hasExecutionCommand" : [ "hasExecutionCommand", "hasExecutionCommand" ],
    "datePublished" : [ "datePublished", "datePublished" ],
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
    "hasSetup" : [ null, null ],
    "hasExample" : [ "hasExample", "hasExample" ],
    "publisher" : [ "{}", "{}" ],
    "hasOutput" : [ {
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
    "hasComponentLocation" : [ "hasComponentLocation", "hasComponentLocation" ],
    "supportDetails" : [ "supportDetails", "supportDetails" ],
    "hasVersion" : [ null, null ],
    "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
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
    "hadPrimarySource" : [ "{}", "{}" ],
    "hasSoftwareImage" : [ {
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
    }, {
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
    } ],
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
    "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
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
    "memoryRequirements" : [ "memoryRequirements", "memoryRequirements" ],
    "website" : [ "website", "website" ],
    "citation" : [ "citation", "citation" ],
    "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
    "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
    "hasSupportScriptLocation" : [ "hasSupportScriptLocation", "hasSupportScriptLocation" ],
    "label" : [ "label", "label" ],
    "hasAssumption" : [ "hasAssumption", "hasAssumption" ],
    "hasParameter" : [ {
      "hasDefaultValue" : [ "", "" ],
      "hasMaximumAcceptedValue" : [ "", "" ],
      "description" : [ "description", "description" ],
      "hasDataType" : [ "hasDataType", "hasDataType" ],
      "hasFixedValue" : [ "", "" ],
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
      "recommendedIncrement" : [ 5.637376656633329, 5.637376656633329 ],
      "type" : [ "type", "type" ],
      "hasMinimumAcceptedValue" : [ "", "" ],
      "hasAcceptedValues" : [ "hasAcceptedValues", "hasAcceptedValues" ],
      "adjustsVariable" : [ {
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
      "relevantForIntervention" : [ {
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
      "position" : [ 2, 2 ],
      "id" : "id",
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
      } ],
      "hasStepSize" : [ 7.061401241503109, 7.061401241503109 ]
    }, {
      "hasDefaultValue" : [ "", "" ],
      "hasMaximumAcceptedValue" : [ "", "" ],
      "description" : [ "description", "description" ],
      "hasDataType" : [ "hasDataType", "hasDataType" ],
      "hasFixedValue" : [ "", "" ],
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
      "recommendedIncrement" : [ 5.637376656633329, 5.637376656633329 ],
      "type" : [ "type", "type" ],
      "hasMinimumAcceptedValue" : [ "", "" ],
      "hasAcceptedValues" : [ "hasAcceptedValues", "hasAcceptedValues" ],
      "adjustsVariable" : [ {
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
      "relevantForIntervention" : [ {
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
      "position" : [ 2, 2 ],
      "id" : "id",
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
      } ],
      "hasStepSize" : [ 7.061401241503109, 7.061401241503109 ]
    } ],
    "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
    "hasInput" : [ {
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
  } ],
  "author" : [ "{}", "{}" ],
  "processorRequirements" : [ "processorRequirements", "processorRequirements" ],
  "hasUsageNotes" : [ "hasUsageNotes", "hasUsageNotes" ],
  "shortDescription" : [ "shortDescription", "shortDescription" ],
  "label" : [ "label", "label" ],
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
  } ],
  "hasVersionId" : [ "hasVersionId", "hasVersionId" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/softwareversions'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(software_version),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
