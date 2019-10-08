# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class CausalDiagram(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, label=None, type=None, has_part=None):  # noqa: E501
        """CausalDiagram - a model defined in OpenAPI

        :param id: The id of this CausalDiagram.  # noqa: E501
        :type id: str
        :param label: The label of this CausalDiagram.  # noqa: E501
        :type label: List[str]
        :param type: The type of this CausalDiagram.  # noqa: E501
        :type type: List[str]
        :param has_part: The has_part of this CausalDiagram.  # noqa: E501
        :type has_part: List[object]
        """


        self.openapi_types = {
            'id': str,
            'label': List[str],
            'type': List[str],
            'has_part': List[object]
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'has_part': 'hasPart'
        }

        self._id = id
        self._label = label
        self._type = type
        self._has_part = has_part

    @classmethod
    def from_dict(cls, dikt) -> 'CausalDiagram':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CausalDiagram of this CausalDiagram.  # noqa: E501
        :rtype: CausalDiagram
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this CausalDiagram.


        :return: The id of this CausalDiagram.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CausalDiagram.


        :param id: The id of this CausalDiagram.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this CausalDiagram.


        :return: The label of this CausalDiagram.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CausalDiagram.


        :param label: The label of this CausalDiagram.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this CausalDiagram.


        :return: The type of this CausalDiagram.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CausalDiagram.


        :param type: The type of this CausalDiagram.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_part(self):
        """Gets the has_part of this CausalDiagram.


        :return: The has_part of this CausalDiagram.
        :rtype: List[object]
        """
        return self._has_part

    @has_part.setter
    def has_part(self, has_part):
        """Sets the has_part of this CausalDiagram.


        :param has_part: The has_part of this CausalDiagram.
        :type has_part: List[object]
        """

        self._has_part = has_part
