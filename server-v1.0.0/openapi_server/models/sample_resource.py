# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SampleResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data_catalog_identifier=None, id=None, label=None, type=None):  # noqa: E501
        """SampleResource - a model defined in OpenAPI

        :param data_catalog_identifier: The data_catalog_identifier of this SampleResource.  # noqa: E501
        :type data_catalog_identifier: List[str]
        :param id: The id of this SampleResource.  # noqa: E501
        :type id: str
        :param label: The label of this SampleResource.  # noqa: E501
        :type label: str
        :param type: The type of this SampleResource.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'data_catalog_identifier': List[str],
            'id': str,
            'label': str,
            'type': List[str]
        }

        self.attribute_map = {
            'data_catalog_identifier': 'dataCatalogIdentifier',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._data_catalog_identifier = data_catalog_identifier
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'SampleResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SampleResource of this SampleResource.  # noqa: E501
        :rtype: SampleResource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_catalog_identifier(self):
        """Gets the data_catalog_identifier of this SampleResource.


        :return: The data_catalog_identifier of this SampleResource.
        :rtype: List[str]
        """
        return self._data_catalog_identifier

    @data_catalog_identifier.setter
    def data_catalog_identifier(self, data_catalog_identifier):
        """Sets the data_catalog_identifier of this SampleResource.


        :param data_catalog_identifier: The data_catalog_identifier of this SampleResource.
        :type data_catalog_identifier: List[str]
        """

        self._data_catalog_identifier = data_catalog_identifier

    @property
    def id(self):
        """Gets the id of this SampleResource.


        :return: The id of this SampleResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SampleResource.


        :param id: The id of this SampleResource.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this SampleResource.


        :return: The label of this SampleResource.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SampleResource.


        :param label: The label of this SampleResource.
        :type label: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SampleResource.


        :return: The type of this SampleResource.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SampleResource.


        :param type: The type of this SampleResource.
        :type type: List[str]
        """

        self._type = type
