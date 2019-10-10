# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class FundingInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, label=None, type=None, funding_source=None, funding_grant=None):  # noqa: E501
        """FundingInformation - a model defined in OpenAPI

        :param id: The id of this FundingInformation.  # noqa: E501
        :type id: str
        :param label: The label of this FundingInformation.  # noqa: E501
        :type label: List[str]
        :param type: The type of this FundingInformation.  # noqa: E501
        :type type: List[str]
        :param funding_source: The funding_source of this FundingInformation.  # noqa: E501
        :type funding_source: List[Organization]
        :param funding_grant: The funding_grant of this FundingInformation.  # noqa: E501
        :type funding_grant: List[str]
        """
        from openapi_server.models.organization import Organization

          # noqa: E501

        self.openapi_types = {
            'id': str,
            'label': List[str],
            'type': List[str],
            'funding_source': List[Organization],
            'funding_grant': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'funding_source': 'fundingSource',
            'funding_grant': 'fundingGrant'
        }

        self._id = id
        self._label = label
        self._type = type
        self._funding_source = funding_source
        self._funding_grant = funding_grant

    @classmethod
    def from_dict(cls, dikt) -> 'FundingInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FundingInformation of this FundingInformation.  # noqa: E501
        :rtype: FundingInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this FundingInformation.


        :return: The id of this FundingInformation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FundingInformation.


        :param id: The id of this FundingInformation.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this FundingInformation.


        :return: The label of this FundingInformation.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this FundingInformation.


        :param label: The label of this FundingInformation.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this FundingInformation.


        :return: The type of this FundingInformation.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FundingInformation.


        :param type: The type of this FundingInformation.
        :type type: List[str]
        """

        self._type = type

    @property
    def funding_source(self):
        """Gets the funding_source of this FundingInformation.


        :return: The funding_source of this FundingInformation.
        :rtype: List[Organization]
        """
        return self._funding_source

    @funding_source.setter
    def funding_source(self, funding_source):
        """Sets the funding_source of this FundingInformation.


        :param funding_source: The funding_source of this FundingInformation.
        :type funding_source: List[Organization]
        """

        self._funding_source = funding_source

    @property
    def funding_grant(self):
        """Gets the funding_grant of this FundingInformation.


        :return: The funding_grant of this FundingInformation.
        :rtype: List[str]
        """
        return self._funding_grant

    @funding_grant.setter
    def funding_grant(self, funding_grant):
        """Sets the funding_grant of this FundingInformation.


        :param funding_grant: The funding_grant of this FundingInformation.
        :type funding_grant: List[str]
        """

        self._funding_grant = funding_grant