# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class FarmingPractices(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, id=None, label=None, type=None):  # noqa: E501
        """FarmingPractices - a model defined in OpenAPI

        :param description: The description of this FarmingPractices.  # noqa: E501
        :type description: List[str]
        :param id: The id of this FarmingPractices.  # noqa: E501
        :type id: str
        :param label: The label of this FarmingPractices.  # noqa: E501
        :type label: List[str]
        :param type: The type of this FarmingPractices.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._description = description
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'FarmingPractices':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FarmingPractices of this FarmingPractices.  # noqa: E501
        :rtype: FarmingPractices
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this FarmingPractices.


        :return: The description of this FarmingPractices.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FarmingPractices.


        :param description: The description of this FarmingPractices.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this FarmingPractices.


        :return: The id of this FarmingPractices.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FarmingPractices.


        :param id: The id of this FarmingPractices.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this FarmingPractices.


        :return: The label of this FarmingPractices.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this FarmingPractices.


        :param label: The label of this FarmingPractices.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this FarmingPractices.


        :return: The type of this FarmingPractices.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FarmingPractices.


        :param type: The type of this FarmingPractices.
        :type type: List[str]
        """

        self._type = type