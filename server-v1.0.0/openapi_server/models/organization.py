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

    def __init__(self, identifier=None, website=None, id=None, label=None, type=None):  # noqa: E501
        """Organization - a model defined in OpenAPI

        :param identifier: The identifier of this Organization.  # noqa: E501
        :type identifier: List[str]
        :param website: The website of this Organization.  # noqa: E501
        :type website: List[str]
        :param id: The id of this Organization.  # noqa: E501
        :type id: str
        :param label: The label of this Organization.  # noqa: E501
        :type label: str
        :param type: The type of this Organization.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'identifier': List[str],
            'website': List[str],
            'id': str,
            'label': str,
            'type': List[str]
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'website': 'website',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._identifier = identifier
        self._website = website
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


        :return: The identifier of this Organization.
        :rtype: List[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Organization.


        :param identifier: The identifier of this Organization.
        :type identifier: List[str]
        """

        self._identifier = identifier

    @property
    def website(self):
        """Gets the website of this Organization.


        :return: The website of this Organization.
        :rtype: List[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Organization.


        :param website: The website of this Organization.
        :type website: List[str]
        """

        self._website = website

    @property
    def id(self):
        """Gets the id of this Organization.


        :return: The id of this Organization.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.


        :param id: The id of this Organization.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Organization.


        :return: The label of this Organization.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Organization.


        :param label: The label of this Organization.
        :type label: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Organization.


        :return: The type of this Organization.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Organization.


        :param type: The type of this Organization.
        :type type: List[str]
        """

        self._type = type
