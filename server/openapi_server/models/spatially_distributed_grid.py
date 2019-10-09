# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SpatiallyDistributedGrid(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_dimensionality=None, has_format=None, has_file_structure=None, description=None, has_presentation=None, label=None, type=None, has_fixed_resource=None, has_spatial_resolution=None, has_coordinate_system=None, has_shape=None, has_dimension=None, position=None, id=None):  # noqa: E501
        """SpatiallyDistributedGrid - a model defined in OpenAPI

        :param has_dimensionality: The has_dimensionality of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_dimensionality: List[float]
        :param has_format: The has_format of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_format: List[str]
        :param has_file_structure: The has_file_structure of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_file_structure: object
        :param description: The description of this SpatiallyDistributedGrid.  # noqa: E501
        :type description: List[str]
        :param has_presentation: The has_presentation of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_presentation: List[object]
        :param label: The label of this SpatiallyDistributedGrid.  # noqa: E501
        :type label: List[str]
        :param type: The type of this SpatiallyDistributedGrid.  # noqa: E501
        :type type: List[str]
        :param has_fixed_resource: The has_fixed_resource of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_fixed_resource: List[object]
        :param has_spatial_resolution: The has_spatial_resolution of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_spatial_resolution: List[str]
        :param has_coordinate_system: The has_coordinate_system of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_coordinate_system: List[str]
        :param has_shape: The has_shape of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_shape: List[str]
        :param has_dimension: The has_dimension of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_dimension: List[str]
        :param position: The position of this SpatiallyDistributedGrid.  # noqa: E501
        :type position: List[float]
        :param id: The id of this SpatiallyDistributedGrid.  # noqa: E501
        :type id: str
        """


        self.openapi_types = {
            'has_dimensionality': List[float],
            'has_format': List[str],
            'has_file_structure': object,
            'description': List[str],
            'has_presentation': List[object],
            'label': List[str],
            'type': List[str],
            'has_fixed_resource': List[object],
            'has_spatial_resolution': List[str],
            'has_coordinate_system': List[str],
            'has_shape': List[str],
            'has_dimension': List[str],
            'position': List[float],
            'id': str
        }

        self.attribute_map = {
            'has_dimensionality': 'hasDimensionality',
            'has_format': 'hasFormat',
            'has_file_structure': 'hasFileStructure',
            'description': 'description',
            'has_presentation': 'hasPresentation',
            'label': 'label',
            'type': 'type',
            'has_fixed_resource': 'hasFixedResource',
            'has_spatial_resolution': 'hasSpatialResolution',
            'has_coordinate_system': 'hasCoordinateSystem',
            'has_shape': 'hasShape',
            'has_dimension': 'hasDimension',
            'position': 'position',
            'id': 'id'
        }

        self._has_dimensionality = has_dimensionality
        self._has_format = has_format
        self._has_file_structure = has_file_structure
        self._description = description
        self._has_presentation = has_presentation
        self._label = label
        self._type = type
        self._has_fixed_resource = has_fixed_resource
        self._has_spatial_resolution = has_spatial_resolution
        self._has_coordinate_system = has_coordinate_system
        self._has_shape = has_shape
        self._has_dimension = has_dimension
        self._position = position
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'SpatiallyDistributedGrid':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpatiallyDistributedGrid of this SpatiallyDistributedGrid.  # noqa: E501
        :rtype: SpatiallyDistributedGrid
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_dimensionality(self):
        """Gets the has_dimensionality of this SpatiallyDistributedGrid.


        :return: The has_dimensionality of this SpatiallyDistributedGrid.
        :rtype: List[float]
        """
        return self._has_dimensionality

    @has_dimensionality.setter
    def has_dimensionality(self, has_dimensionality):
        """Sets the has_dimensionality of this SpatiallyDistributedGrid.


        :param has_dimensionality: The has_dimensionality of this SpatiallyDistributedGrid.
        :type has_dimensionality: List[float]
        """

        self._has_dimensionality = has_dimensionality

    @property
    def has_format(self):
        """Gets the has_format of this SpatiallyDistributedGrid.


        :return: The has_format of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._has_format

    @has_format.setter
    def has_format(self, has_format):
        """Sets the has_format of this SpatiallyDistributedGrid.


        :param has_format: The has_format of this SpatiallyDistributedGrid.
        :type has_format: List[str]
        """

        self._has_format = has_format

    @property
    def has_file_structure(self):
        """Gets the has_file_structure of this SpatiallyDistributedGrid.


        :return: The has_file_structure of this SpatiallyDistributedGrid.
        :rtype: object
        """
        return self._has_file_structure

    @has_file_structure.setter
    def has_file_structure(self, has_file_structure):
        """Sets the has_file_structure of this SpatiallyDistributedGrid.


        :param has_file_structure: The has_file_structure of this SpatiallyDistributedGrid.
        :type has_file_structure: object
        """

        self._has_file_structure = has_file_structure

    @property
    def description(self):
        """Gets the description of this SpatiallyDistributedGrid.


        :return: The description of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SpatiallyDistributedGrid.


        :param description: The description of this SpatiallyDistributedGrid.
        :type description: List[str]
        """

        self._description = description

    @property
    def has_presentation(self):
        """Gets the has_presentation of this SpatiallyDistributedGrid.


        :return: The has_presentation of this SpatiallyDistributedGrid.
        :rtype: List[object]
        """
        return self._has_presentation

    @has_presentation.setter
    def has_presentation(self, has_presentation):
        """Sets the has_presentation of this SpatiallyDistributedGrid.


        :param has_presentation: The has_presentation of this SpatiallyDistributedGrid.
        :type has_presentation: List[object]
        """

        self._has_presentation = has_presentation

    @property
    def label(self):
        """Gets the label of this SpatiallyDistributedGrid.


        :return: The label of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SpatiallyDistributedGrid.


        :param label: The label of this SpatiallyDistributedGrid.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SpatiallyDistributedGrid.


        :return: The type of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SpatiallyDistributedGrid.


        :param type: The type of this SpatiallyDistributedGrid.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_fixed_resource(self):
        """Gets the has_fixed_resource of this SpatiallyDistributedGrid.


        :return: The has_fixed_resource of this SpatiallyDistributedGrid.
        :rtype: List[object]
        """
        return self._has_fixed_resource

    @has_fixed_resource.setter
    def has_fixed_resource(self, has_fixed_resource):
        """Sets the has_fixed_resource of this SpatiallyDistributedGrid.


        :param has_fixed_resource: The has_fixed_resource of this SpatiallyDistributedGrid.
        :type has_fixed_resource: List[object]
        """

        self._has_fixed_resource = has_fixed_resource

    @property
    def has_spatial_resolution(self):
        """Gets the has_spatial_resolution of this SpatiallyDistributedGrid.


        :return: The has_spatial_resolution of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._has_spatial_resolution

    @has_spatial_resolution.setter
    def has_spatial_resolution(self, has_spatial_resolution):
        """Sets the has_spatial_resolution of this SpatiallyDistributedGrid.


        :param has_spatial_resolution: The has_spatial_resolution of this SpatiallyDistributedGrid.
        :type has_spatial_resolution: List[str]
        """

        self._has_spatial_resolution = has_spatial_resolution

    @property
    def has_coordinate_system(self):
        """Gets the has_coordinate_system of this SpatiallyDistributedGrid.


        :return: The has_coordinate_system of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._has_coordinate_system

    @has_coordinate_system.setter
    def has_coordinate_system(self, has_coordinate_system):
        """Sets the has_coordinate_system of this SpatiallyDistributedGrid.


        :param has_coordinate_system: The has_coordinate_system of this SpatiallyDistributedGrid.
        :type has_coordinate_system: List[str]
        """

        self._has_coordinate_system = has_coordinate_system

    @property
    def has_shape(self):
        """Gets the has_shape of this SpatiallyDistributedGrid.


        :return: The has_shape of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._has_shape

    @has_shape.setter
    def has_shape(self, has_shape):
        """Sets the has_shape of this SpatiallyDistributedGrid.


        :param has_shape: The has_shape of this SpatiallyDistributedGrid.
        :type has_shape: List[str]
        """

        self._has_shape = has_shape

    @property
    def has_dimension(self):
        """Gets the has_dimension of this SpatiallyDistributedGrid.


        :return: The has_dimension of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._has_dimension

    @has_dimension.setter
    def has_dimension(self, has_dimension):
        """Sets the has_dimension of this SpatiallyDistributedGrid.


        :param has_dimension: The has_dimension of this SpatiallyDistributedGrid.
        :type has_dimension: List[str]
        """

        self._has_dimension = has_dimension

    @property
    def position(self):
        """Gets the position of this SpatiallyDistributedGrid.


        :return: The position of this SpatiallyDistributedGrid.
        :rtype: List[float]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this SpatiallyDistributedGrid.


        :param position: The position of this SpatiallyDistributedGrid.
        :type position: List[float]
        """

        self._position = position

    @property
    def id(self):
        """Gets the id of this SpatiallyDistributedGrid.


        :return: The id of this SpatiallyDistributedGrid.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpatiallyDistributedGrid.


        :param id: The id of this SpatiallyDistributedGrid.
        :type id: str
        """

        self._id = id
