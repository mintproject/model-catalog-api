# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SpatialResolution(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, label=None, type=None):  # noqa: E501
        """SpatialResolution - a model defined in OpenAPI

        :param id: The id of this SpatialResolution.  # noqa: E501
        :type id: List[str]
        :param label: The label of this SpatialResolution.  # noqa: E501
        :type label: List[str]
        :param type: The type of this SpatialResolution.  # noqa: E501
        :type type: List[str]
        """
        self.openapi_types = {
            'id': List[str],
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'SpatialResolution':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpatialResolution of this SpatialResolution.  # noqa: E501
        :rtype: SpatialResolution
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SpatialResolution.


        :return: The id of this SpatialResolution.
        :rtype: List[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpatialResolution.


        :param id: The id of this SpatialResolution.
        :type id: List[str]
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def label(self):
        """Gets the label of this SpatialResolution.


        :return: The label of this SpatialResolution.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SpatialResolution.


        :param label: The label of this SpatialResolution.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SpatialResolution.


        :return: The type of this SpatialResolution.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SpatialResolution.


        :param type: The type of this SpatialResolution.
        :type type: List[str]
        """

        self._type = type
