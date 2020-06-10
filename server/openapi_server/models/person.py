# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Person(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, identifier=None, website=None, description=None, id=None, label=None, type=None, email=None):  # noqa: E501
        """Person - a model defined in OpenAPI

        :param identifier: The identifier of this Person.  # noqa: E501
        :type identifier: List[str]
        :param website: The website of this Person.  # noqa: E501
        :type website: List[str]
        :param description: The description of this Person.  # noqa: E501
        :type description: List[str]
        :param id: The id of this Person.  # noqa: E501
        :type id: str
        :param label: The label of this Person.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Person.  # noqa: E501
        :type type: List[str]
        :param email: The email of this Person.  # noqa: E501
        :type email: List[str]
        """


        self.openapi_types = {
            'identifier': List[str],
            'website': List[str],
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str],
            'email': List[str]
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'website': 'website',
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'email': 'email'
        }

        self._identifier = identifier
        self._website = website
        self._description = description
        self._id = id
        self._label = label
        self._type = type
        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'Person':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Person of this Person.  # noqa: E501
        :rtype: Person
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identifier(self):
        """Gets the identifier of this Person.

        Identifier of the resource being described  # noqa: E501

        :return: The identifier of this Person.
        :rtype: List[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Person.

        Identifier of the resource being described  # noqa: E501

        :param identifier: The identifier of this Person.
        :type identifier: List[str]
        """

        self._identifier = identifier

    @property
    def website(self):
        """Gets the website of this Person.

        Website of the software  # noqa: E501

        :return: The website of this Person.
        :rtype: List[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Person.

        Website of the software  # noqa: E501

        :param website: The website of this Person.
        :type website: List[str]
        """

        self._website = website

    @property
    def description(self):
        """Gets the description of this Person.

        small description  # noqa: E501

        :return: The description of this Person.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Person.

        small description  # noqa: E501

        :param description: The description of this Person.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Person.

        identifier  # noqa: E501

        :return: The id of this Person.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Person.

        identifier  # noqa: E501

        :param id: The id of this Person.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Person.

        short description of the resource  # noqa: E501

        :return: The label of this Person.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Person.

        short description of the resource  # noqa: E501

        :param label: The label of this Person.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Person.

        type of the resource  # noqa: E501

        :return: The type of this Person.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Person.

        type of the resource  # noqa: E501

        :param type: The type of this Person.
        :type type: List[str]
        """

        self._type = type

    @property
    def email(self):
        """Gets the email of this Person.

        Description not available  # noqa: E501

        :return: The email of this Person.
        :rtype: List[str]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Person.

        Description not available  # noqa: E501

        :param email: The email of this Person.
        :type email: List[str]
        """

        self._email = email
