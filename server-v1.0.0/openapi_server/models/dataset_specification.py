# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class DatasetSpecification(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_dimensionality=None, has_format=None, has_file_structure=None, has_presentation=None, position=None, id=None, label=None, type=None, has_fixed_resource=None):  # noqa: E501
        """DatasetSpecification - a model defined in OpenAPI

        :param has_dimensionality: The has_dimensionality of this DatasetSpecification.  # noqa: E501
        :type has_dimensionality: List[float]
        :param has_format: The has_format of this DatasetSpecification.  # noqa: E501
        :type has_format: List[str]
        :param has_file_structure: The has_file_structure of this DatasetSpecification.  # noqa: E501
        :type has_file_structure: object
        :param has_presentation: The has_presentation of this DatasetSpecification.  # noqa: E501
        :type has_presentation: List[VariablePresentation]
        :param position: The position of this DatasetSpecification.  # noqa: E501
        :type position: List[float]
        :param id: The id of this DatasetSpecification.  # noqa: E501
        :type id: str
        :param label: The label of this DatasetSpecification.  # noqa: E501
        :type label: str
        :param type: The type of this DatasetSpecification.  # noqa: E501
        :type type: List[str]
        :param has_fixed_resource: The has_fixed_resource of this DatasetSpecification.  # noqa: E501
        :type has_fixed_resource: List[SampleResource]
        """
        from openapi_server.models.sample_resource import SampleResource
        from openapi_server.models.variable_presentation import VariablePresentation

          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'has_dimensionality': List[float],
            'has_format': List[str],
            'has_file_structure': object,
            'has_presentation': List[VariablePresentation],
            'position': List[float],
            'id': str,
            'label': str,
            'type': List[str],
            'has_fixed_resource': List[SampleResource]
        }

        self.attribute_map = {
            'has_dimensionality': 'hasDimensionality',
            'has_format': 'hasFormat',
            'has_file_structure': 'hasFileStructure',
            'has_presentation': 'hasPresentation',
            'position': 'position',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'has_fixed_resource': 'hasFixedResource'
        }

        self._has_dimensionality = has_dimensionality
        self._has_format = has_format
        self._has_file_structure = has_file_structure
        self._has_presentation = has_presentation
        self._position = position
        self._id = id
        self._label = label
        self._type = type
        self._has_fixed_resource = has_fixed_resource

    @classmethod
    def from_dict(cls, dikt) -> 'DatasetSpecification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DatasetSpecification of this DatasetSpecification.  # noqa: E501
        :rtype: DatasetSpecification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_dimensionality(self):
        """Gets the has_dimensionality of this DatasetSpecification.


        :return: The has_dimensionality of this DatasetSpecification.
        :rtype: List[float]
        """
        return self._has_dimensionality

    @has_dimensionality.setter
    def has_dimensionality(self, has_dimensionality):
        """Sets the has_dimensionality of this DatasetSpecification.


        :param has_dimensionality: The has_dimensionality of this DatasetSpecification.
        :type has_dimensionality: List[float]
        """

        self._has_dimensionality = has_dimensionality

    @property
    def has_format(self):
        """Gets the has_format of this DatasetSpecification.


        :return: The has_format of this DatasetSpecification.
        :rtype: List[str]
        """
        return self._has_format

    @has_format.setter
    def has_format(self, has_format):
        """Sets the has_format of this DatasetSpecification.


        :param has_format: The has_format of this DatasetSpecification.
        :type has_format: List[str]
        """

        self._has_format = has_format

    @property
    def has_file_structure(self):
        """Gets the has_file_structure of this DatasetSpecification.


        :return: The has_file_structure of this DatasetSpecification.
        :rtype: object
        """
        return self._has_file_structure

    @has_file_structure.setter
    def has_file_structure(self, has_file_structure):
        """Sets the has_file_structure of this DatasetSpecification.


        :param has_file_structure: The has_file_structure of this DatasetSpecification.
        :type has_file_structure: object
        """

        self._has_file_structure = has_file_structure

    @property
    def has_presentation(self):
        """Gets the has_presentation of this DatasetSpecification.


        :return: The has_presentation of this DatasetSpecification.
        :rtype: List[VariablePresentation]
        """
        return self._has_presentation

    @has_presentation.setter
    def has_presentation(self, has_presentation):
        """Sets the has_presentation of this DatasetSpecification.


        :param has_presentation: The has_presentation of this DatasetSpecification.
        :type has_presentation: List[VariablePresentation]
        """

        self._has_presentation = has_presentation

    @property
    def position(self):
        """Gets the position of this DatasetSpecification.


        :return: The position of this DatasetSpecification.
        :rtype: List[float]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DatasetSpecification.


        :param position: The position of this DatasetSpecification.
        :type position: List[float]
        """

        self._position = position

    @property
    def id(self):
        """Gets the id of this DatasetSpecification.


        :return: The id of this DatasetSpecification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatasetSpecification.


        :param id: The id of this DatasetSpecification.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this DatasetSpecification.


        :return: The label of this DatasetSpecification.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DatasetSpecification.


        :param label: The label of this DatasetSpecification.
        :type label: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this DatasetSpecification.


        :return: The type of this DatasetSpecification.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DatasetSpecification.


        :param type: The type of this DatasetSpecification.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_fixed_resource(self):
        """Gets the has_fixed_resource of this DatasetSpecification.


        :return: The has_fixed_resource of this DatasetSpecification.
        :rtype: List[SampleResource]
        """
        return self._has_fixed_resource

    @has_fixed_resource.setter
    def has_fixed_resource(self, has_fixed_resource):
        """Sets the has_fixed_resource of this DatasetSpecification.


        :param has_fixed_resource: The has_fixed_resource of this DatasetSpecification.
        :type has_fixed_resource: List[SampleResource]
        """

        self._has_fixed_resource = has_fixed_resource
