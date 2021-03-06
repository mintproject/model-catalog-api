# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Organization(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, identifier=None, website=None, description=None, id=None, label=None, type=None):  # noqa: E501
        """Organization - a model defined in OpenAPI

        :param identifier: The identifier of this Organization.  # noqa: E501
        :type identifier: List[str]
        :param website: The website of this Organization.  # noqa: E501
        :type website: List[str]
        :param description: The description of this Organization.  # noqa: E501
        :type description: List[str]
        :param id: The id of this Organization.  # noqa: E501
        :type id: str
        :param label: The label of this Organization.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Organization.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'identifier': List[str],
            'website': List[str],
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'website': 'website',
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._identifier = identifier
        self._website = website
        self._description = description
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Organization':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Organization of this Organization.  # noqa: E501
        :rtype: Organization
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identifier(self):
        """Gets the identifier of this Organization.

        Identifier of the resource being described  # noqa: E501

        :return: The identifier of this Organization.
        :rtype: List[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Organization.

        Identifier of the resource being described  # noqa: E501

        :param identifier: The identifier of this Organization.
        :type identifier: List[str]
        """

        self._identifier = identifier

    @property
    def website(self):
        """Gets the website of this Organization.

        Website of the software  # noqa: E501

        :return: The website of this Organization.
        :rtype: List[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Organization.

        Website of the software  # noqa: E501

        :param website: The website of this Organization.
        :type website: List[str]
        """

        self._website = website

    @property
    def description(self):
        """Gets the description of this Organization.

        small description  # noqa: E501

        :return: The description of this Organization.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Organization.

        small description  # noqa: E501

        :param description: The description of this Organization.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Organization.

        identifier  # noqa: E501

        :return: The id of this Organization.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.

        identifier  # noqa: E501

        :param id: The id of this Organization.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Organization.

        short description of the resource  # noqa: E501

        :return: The label of this Organization.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Organization.

        short description of the resource  # noqa: E501

        :param label: The label of this Organization.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Organization.

        type of the resource  # noqa: E501

        :return: The type of this Organization.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Organization.

        type of the resource  # noqa: E501

        :param type: The type of this Organization.
        :type type: List[str]
        """

        self._type = type
