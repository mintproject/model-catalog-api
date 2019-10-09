# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SampleExecution(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, id=None, label=None, type=None, has_execution_command=None):  # noqa: E501
        """SampleExecution - a model defined in OpenAPI

        :param description: The description of this SampleExecution.  # noqa: E501
        :type description: List[str]
        :param id: The id of this SampleExecution.  # noqa: E501
        :type id: str
        :param label: The label of this SampleExecution.  # noqa: E501
        :type label: List[str]
        :param type: The type of this SampleExecution.  # noqa: E501
        :type type: List[str]
        :param has_execution_command: The has_execution_command of this SampleExecution.  # noqa: E501
        :type has_execution_command: List[str]
        """


        self.openapi_types = {
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str],
            'has_execution_command': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'has_execution_command': 'hasExecutionCommand'
        }

        self._description = description
        self._id = id
        self._label = label
        self._type = type
        self._has_execution_command = has_execution_command

    @classmethod
    def from_dict(cls, dikt) -> 'SampleExecution':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SampleExecution of this SampleExecution.  # noqa: E501
        :rtype: SampleExecution
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this SampleExecution.


        :return: The description of this SampleExecution.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SampleExecution.


        :param description: The description of this SampleExecution.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this SampleExecution.


        :return: The id of this SampleExecution.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SampleExecution.


        :param id: The id of this SampleExecution.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this SampleExecution.


        :return: The label of this SampleExecution.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SampleExecution.


        :param label: The label of this SampleExecution.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SampleExecution.


        :return: The type of this SampleExecution.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SampleExecution.


        :param type: The type of this SampleExecution.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_execution_command(self):
        """Gets the has_execution_command of this SampleExecution.


        :return: The has_execution_command of this SampleExecution.
        :rtype: List[str]
        """
        return self._has_execution_command

    @has_execution_command.setter
    def has_execution_command(self, has_execution_command):
        """Sets the has_execution_command of this SampleExecution.


        :param has_execution_command: The has_execution_command of this SampleExecution.
        :type has_execution_command: List[str]
        """

        self._has_execution_command = has_execution_command
