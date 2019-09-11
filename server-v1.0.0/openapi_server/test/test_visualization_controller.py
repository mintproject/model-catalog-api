# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.visualization import Visualization  # noqa: E501
from openapi_server.test import BaseTestCase


class TestVisualizationController(BaseTestCase):
    """VisualizationController integration test stubs"""

    def test_visualizations_get(self):
        """Test case for visualizations_get

        List all Visualization entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/visualizations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_visualizations_id_delete(self):
        """Test case for visualizations_id_delete

        Delete a Visualization
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/visualizations/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_visualizations_id_get(self):
        """Test case for visualizations_id_get

        Get a Visualization
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/visualizations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_visualizations_id_put(self):
        """Test case for visualizations_id_put

        Update a Visualization
        """
        visualization = {
  "hasFormat" : [ "hasFormat", "hasFormat" ],
  "wasDerivedFromSoftware" : [ {
    "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
    "keywords" : [ "keywords", "keywords" ],
    "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
    "hasVersion" : [ null, null ],
    "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
    "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
    "referencePublication" : [ "referencePublication", "referencePublication" ],
    "description" : [ "description", "description" ],
    "screenshot" : [ {
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
    }, {
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
    } ],
    "type" : [ "type", "type" ],
    "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
    "dateCreated" : [ "dateCreated", "dateCreated" ],
    "contributor" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    } ],
    "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
    "hasContactPerson" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    } ],
    "logo" : [ {
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
    }, {
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
    } ],
    "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
    "id" : "id",
    "hasSampleVisualization" : [ null, null ],
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
    "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
    "license" : [ "license", "license" ],
    "hasSourceCode" : [ {
      "license" : [ "license", "license" ],
      "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
      "codeRepository" : [ "codeRepository", "codeRepository" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "license" : [ "license", "license" ],
      "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
      "codeRepository" : [ "codeRepository", "codeRepository" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ],
    "publisher" : [ "{}", "{}" ],
    "fundingSource" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ]
  }, {
    "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
    "keywords" : [ "keywords", "keywords" ],
    "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
    "hasVersion" : [ null, null ],
    "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
    "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
    "referencePublication" : [ "referencePublication", "referencePublication" ],
    "description" : [ "description", "description" ],
    "screenshot" : [ {
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
    }, {
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
    } ],
    "type" : [ "type", "type" ],
    "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
    "dateCreated" : [ "dateCreated", "dateCreated" ],
    "contributor" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    } ],
    "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
    "hasContactPerson" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    } ],
    "logo" : [ {
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
    }, {
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
    } ],
    "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
    "id" : "id",
    "hasSampleVisualization" : [ null, null ],
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
    "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
    "license" : [ "license", "license" ],
    "hasSourceCode" : [ {
      "license" : [ "license", "license" ],
      "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
      "codeRepository" : [ "codeRepository", "codeRepository" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "license" : [ "license", "license" ],
      "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
      "codeRepository" : [ "codeRepository", "codeRepository" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ],
    "publisher" : [ "{}", "{}" ],
    "fundingSource" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ]
  } ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/visualizations/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(visualization),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_visualizations_post(self):
        """Test case for visualizations_post

        Create a Visualization
        """
        visualization = {
  "hasFormat" : [ "hasFormat", "hasFormat" ],
  "wasDerivedFromSoftware" : [ {
    "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
    "keywords" : [ "keywords", "keywords" ],
    "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
    "hasVersion" : [ null, null ],
    "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
    "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
    "referencePublication" : [ "referencePublication", "referencePublication" ],
    "description" : [ "description", "description" ],
    "screenshot" : [ {
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
    }, {
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
    } ],
    "type" : [ "type", "type" ],
    "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
    "dateCreated" : [ "dateCreated", "dateCreated" ],
    "contributor" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    } ],
    "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
    "hasContactPerson" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    } ],
    "logo" : [ {
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
    }, {
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
    } ],
    "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
    "id" : "id",
    "hasSampleVisualization" : [ null, null ],
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
    "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
    "license" : [ "license", "license" ],
    "hasSourceCode" : [ {
      "license" : [ "license", "license" ],
      "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
      "codeRepository" : [ "codeRepository", "codeRepository" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "license" : [ "license", "license" ],
      "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
      "codeRepository" : [ "codeRepository", "codeRepository" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ],
    "publisher" : [ "{}", "{}" ],
    "fundingSource" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ]
  }, {
    "hasDocumentation" : [ "hasDocumentation", "hasDocumentation" ],
    "keywords" : [ "keywords", "keywords" ],
    "softwareRequirements" : [ "softwareRequirements", "softwareRequirements" ],
    "hasVersion" : [ null, null ],
    "hasTypicalDataSource" : [ "hasTypicalDataSource", "hasTypicalDataSource" ],
    "hasDownloadURL" : [ "hasDownloadURL", "hasDownloadURL" ],
    "referencePublication" : [ "referencePublication", "referencePublication" ],
    "description" : [ "description", "description" ],
    "screenshot" : [ {
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
    }, {
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
    } ],
    "type" : [ "type", "type" ],
    "hasInstallationInstructions" : [ "hasInstallationInstructions", "hasInstallationInstructions" ],
    "dateCreated" : [ "dateCreated", "dateCreated" ],
    "contributor" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    } ],
    "hasFAQ" : [ "hasFAQ", "hasFAQ" ],
    "hasContactPerson" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ],
      "email" : [ "email", "email" ]
    } ],
    "logo" : [ {
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
    }, {
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
    } ],
    "hasPurpose" : [ "hasPurpose", "hasPurpose" ],
    "id" : "id",
    "hasSampleVisualization" : [ null, null ],
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
    "operatingSystems" : [ "operatingSystems", "operatingSystems" ],
    "license" : [ "license", "license" ],
    "hasSourceCode" : [ {
      "license" : [ "license", "license" ],
      "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
      "codeRepository" : [ "codeRepository", "codeRepository" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "license" : [ "license", "license" ],
      "programmingLanguage" : [ "programmingLanguage", "programmingLanguage" ],
      "codeRepository" : [ "codeRepository", "codeRepository" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ],
    "publisher" : [ "{}", "{}" ],
    "fundingSource" : [ {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    }, {
      "identifier" : [ "identifier", "identifier" ],
      "website" : [ "website", "website" ],
      "id" : "id",
      "label" : "label",
      "type" : [ "type", "type" ]
    } ]
  } ],
  "id" : "id",
  "label" : "label",
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.0.0/visualizations'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(visualization),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
