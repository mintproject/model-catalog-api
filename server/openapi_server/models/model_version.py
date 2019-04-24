# coding: utf-8

from __future__ import absolute_import

from typing import List  # noqa: F401

from openapi_server import util
from openapi_server.models.base_model_ import Model
from openapi_server.models.model_configuration import  ModelConfiguration
from openapi_server.static_vars import *

class ModelVersion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, label=None, type=["https://w3id.org/mint/modelCatalog#ModelVersion"], has_documentation=None, has_version_id=None, has_configuration=None, description=None):  # noqa: E501
        """ModelVersion - a model defined in OpenAPI

        :param id: The id of this ModelVersion.  # noqa: E501
        :type id: str
        :param label: The label of this ModelVersion.  # noqa: E501
        :type label: str
        :param type: The type of this ModelVersion.  # noqa: E501
        :type type: List[str]
        :param has_documentation: The has_documentation of this ModelVersion.  # noqa: E501
        :type has_documentation: List[str]
        :param has_version_id: The has_version_id of this ModelVersion.  # noqa: E501
        :type has_version_id: str
        :param has_configuration: The has_configuration of this ModelVersion.  # noqa: E501
        :type has_configuration: List[ModelConfiguration]
        :param description: The description of this ModelVersion.  # noqa: E501
        :type description: str
        """
        self.openapi_types = {
            'id': str,
            'label': str,
            'type': List[str],
            'has_documentation': List[str],
            'has_version_id': str,
            'has_configuration': List[ModelConfiguration],
            'description': str
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'has_documentation': 'hasDocumentation',
            'has_version_id': 'hasVersionId',
            'has_configuration': 'hasConfiguration',
            'description': 'description'
        }

        self._id = id
        self._label = label
        self._type = type
        self._has_documentation = has_documentation
        self._has_version_id = has_version_id
        self._has_configuration = has_configuration
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'ModelVersion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModelVersion of this ModelVersion.  # noqa: E501
        :rtype: ModelVersion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ModelVersion.


        :return: The id of this ModelVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelVersion.


        :param id: The id of this ModelVersion.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def label(self):
        """Gets the label of this ModelVersion.


        :return: The label of this ModelVersion.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModelVersion.


        :param label: The label of this ModelVersion.
        :type label: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this ModelVersion.


        :return: The type of this ModelVersion.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelVersion.


        :param type: The type of this ModelVersion.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_documentation(self):
        """Gets the has_documentation of this ModelVersion.


        :return: The has_documentation of this ModelVersion.
        :rtype: List[str]
        """
        return self._has_documentation

    @has_documentation.setter
    def has_documentation(self, has_documentation):
        """Sets the has_documentation of this ModelVersion.


        :param has_documentation: The has_documentation of this ModelVersion.
        :type has_documentation: List[str]
        """

        self._has_documentation = has_documentation

    @property
    def has_version_id(self):
        """Gets the has_version_id of this ModelVersion.


        :return: The has_version_id of this ModelVersion.
        :rtype: str
        """
        return self._has_version_id

    @has_version_id.setter
    def has_version_id(self, has_version_id):
        """Sets the has_version_id of this ModelVersion.


        :param has_version_id: The has_version_id of this ModelVersion.
        :type has_version_id: str
        """

        self._has_version_id = has_version_id

    @property
    def has_configuration(self):
        """Gets the has_configuration of this ModelVersion.


        :return: The has_configuration of this ModelVersion.
        :rtype: List[ModelConfiguration]
        """
        return self._has_configuration

    @has_configuration.setter
    def has_configuration(self, has_configuration):
        """Sets the has_configuration of this ModelVersion.


        :param has_configuration: The has_configuration of this ModelVersion.
        :type has_configuration: List[ModelConfiguration]
        """

        self._has_configuration = has_configuration

    @property
    def description(self):
        """Gets the description of this ModelVersion.


        :return: The description of this ModelVersion.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelVersion.


        :param description: The description of this ModelVersion.
        :type description: str
        """

        self._description = description
