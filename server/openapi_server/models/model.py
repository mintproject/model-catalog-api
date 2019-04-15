# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Model(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, label=None, type=["https://w3id.org/mint/modelCatalog#Model"], has_software_version=None, has_model_category=None, has_documentation=None):  # noqa: E501
        """Model - a model defined in OpenAPI

        :param id: The id of this Model.  # noqa: E501
        :type id: str
        :param label: The label of this Model.  # noqa: E501
        :type label: str
        :param type: The type of this Model.  # noqa: E501
        :type type: List[str]
        :param has_software_version: The has_software_version of this Model.  # noqa: E501
        :type has_software_version: List[object]
        :param has_model_category: The has_model_category of this Model.  # noqa: E501
        :type has_model_category: List[str]
        :param has_documentation: The has_documentation of this Model.  # noqa: E501
        :type has_documentation: List[str]
        """
        self.openapi_types = {
            'id': str,
            'label': str,
            'type': List[str],
            'has_software_version': List[object],
            'has_model_category': List[str],
            'has_documentation': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'has_software_version': 'hasSoftwareVersion',
            'has_model_category': 'hasModelCategory',
            'has_documentation': 'hasDocumentation'
        }

        self._id = id
        self._label = label
        self._type = type
        self._has_software_version = has_software_version
        self._has_model_category = has_model_category
        self._has_documentation = has_documentation

    @classmethod
    def from_dict(cls, dikt) -> 'Model':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Model of this Model.  # noqa: E501
        :rtype: Model
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Model.


        :return: The id of this Model.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Model.


        :param id: The id of this Model.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def label(self):
        """Gets the label of this Model.


        :return: The label of this Model.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Model.


        :param label: The label of this Model.
        :type label: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Model.


        :return: The type of this Model.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Model.


        :param type: The type of this Model.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_software_version(self):
        """Gets the has_software_version of this Model.


        :return: The has_software_version of this Model.
        :rtype: List[object]
        """
        return self._has_software_version

    @has_software_version.setter
    def has_software_version(self, has_software_version):
        """Sets the has_software_version of this Model.


        :param has_software_version: The has_software_version of this Model.
        :type has_software_version: List[object]
        """

        self._has_software_version = has_software_version

    @property
    def has_model_category(self):
        """Gets the has_model_category of this Model.


        :return: The has_model_category of this Model.
        :rtype: List[str]
        """
        return self._has_model_category

    @has_model_category.setter
    def has_model_category(self, has_model_category):
        """Sets the has_model_category of this Model.


        :param has_model_category: The has_model_category of this Model.
        :type has_model_category: List[str]
        """

        self._has_model_category = has_model_category

    @property
    def has_documentation(self):
        """Gets the has_documentation of this Model.


        :return: The has_documentation of this Model.
        :rtype: List[str]
        """
        return self._has_documentation

    @has_documentation.setter
    def has_documentation(self, has_documentation):
        """Sets the has_documentation of this Model.


        :param has_documentation: The has_documentation of this Model.
        :type has_documentation: List[str]
        """

        self._has_documentation = has_documentation
