# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class VariablePresentation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_default_value=None, has_standard_variable=None, has_maximum_accepted_value=None, has_constraint=None, description=None, label=None, type=None, has_long_name=None, has_short_name=None, has_minimum_accepted_value=None, id=None, part_of_dataset=None, uses_unit=None):  # noqa: E501
        """VariablePresentation - a model defined in OpenAPI

        :param has_default_value: The has_default_value of this VariablePresentation.  # noqa: E501
        :type has_default_value: List[str]
        :param has_standard_variable: The has_standard_variable of this VariablePresentation.  # noqa: E501
        :type has_standard_variable: List[StandardVariable]
        :param has_maximum_accepted_value: The has_maximum_accepted_value of this VariablePresentation.  # noqa: E501
        :type has_maximum_accepted_value: List[str]
        :param has_constraint: The has_constraint of this VariablePresentation.  # noqa: E501
        :type has_constraint: List[str]
        :param description: The description of this VariablePresentation.  # noqa: E501
        :type description: List[str]
        :param label: The label of this VariablePresentation.  # noqa: E501
        :type label: List[str]
        :param type: The type of this VariablePresentation.  # noqa: E501
        :type type: List[str]
        :param has_long_name: The has_long_name of this VariablePresentation.  # noqa: E501
        :type has_long_name: List[str]
        :param has_short_name: The has_short_name of this VariablePresentation.  # noqa: E501
        :type has_short_name: List[str]
        :param has_minimum_accepted_value: The has_minimum_accepted_value of this VariablePresentation.  # noqa: E501
        :type has_minimum_accepted_value: List[str]
        :param id: The id of this VariablePresentation.  # noqa: E501
        :type id: str
        :param part_of_dataset: The part_of_dataset of this VariablePresentation.  # noqa: E501
        :type part_of_dataset: List[DatasetSpecification]
        :param uses_unit: The uses_unit of this VariablePresentation.  # noqa: E501
        :type uses_unit: List[object]
        """
        from openapi_server.models.dataset_specification import DatasetSpecification
        from openapi_server.models.standard_variable import StandardVariable

          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'has_default_value': List[str],
            'has_standard_variable': List[StandardVariable],
            'has_maximum_accepted_value': List[str],
            'has_constraint': List[str],
            'description': List[str],
            'label': List[str],
            'type': List[str],
            'has_long_name': List[str],
            'has_short_name': List[str],
            'has_minimum_accepted_value': List[str],
            'id': str,
            'part_of_dataset': List[DatasetSpecification],
            'uses_unit': List[object]
        }

        self.attribute_map = {
            'has_default_value': 'hasDefaultValue',
            'has_standard_variable': 'hasStandardVariable',
            'has_maximum_accepted_value': 'hasMaximumAcceptedValue',
            'has_constraint': 'hasConstraint',
            'description': 'description',
            'label': 'label',
            'type': 'type',
            'has_long_name': 'hasLongName',
            'has_short_name': 'hasShortName',
            'has_minimum_accepted_value': 'hasMinimumAcceptedValue',
            'id': 'id',
            'part_of_dataset': 'partOfDataset',
            'uses_unit': 'usesUnit'
        }

        self._has_default_value = has_default_value
        self._has_standard_variable = has_standard_variable
        self._has_maximum_accepted_value = has_maximum_accepted_value
        self._has_constraint = has_constraint
        self._description = description
        self._label = label
        self._type = type
        self._has_long_name = has_long_name
        self._has_short_name = has_short_name
        self._has_minimum_accepted_value = has_minimum_accepted_value
        self._id = id
        self._part_of_dataset = part_of_dataset
        self._uses_unit = uses_unit

    @classmethod
    def from_dict(cls, dikt) -> 'VariablePresentation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VariablePresentation of this VariablePresentation.  # noqa: E501
        :rtype: VariablePresentation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_default_value(self):
        """Gets the has_default_value of this VariablePresentation.


        :return: The has_default_value of this VariablePresentation.
        :rtype: List[str]
        """
        return self._has_default_value

    @has_default_value.setter
    def has_default_value(self, has_default_value):
        """Sets the has_default_value of this VariablePresentation.


        :param has_default_value: The has_default_value of this VariablePresentation.
        :type has_default_value: List[str]
        """

        self._has_default_value = has_default_value

    @property
    def has_standard_variable(self):
        """Gets the has_standard_variable of this VariablePresentation.


        :return: The has_standard_variable of this VariablePresentation.
        :rtype: List[StandardVariable]
        """
        return self._has_standard_variable

    @has_standard_variable.setter
    def has_standard_variable(self, has_standard_variable):
        """Sets the has_standard_variable of this VariablePresentation.


        :param has_standard_variable: The has_standard_variable of this VariablePresentation.
        :type has_standard_variable: List[StandardVariable]
        """

        self._has_standard_variable = has_standard_variable

    @property
    def has_maximum_accepted_value(self):
        """Gets the has_maximum_accepted_value of this VariablePresentation.


        :return: The has_maximum_accepted_value of this VariablePresentation.
        :rtype: List[str]
        """
        return self._has_maximum_accepted_value

    @has_maximum_accepted_value.setter
    def has_maximum_accepted_value(self, has_maximum_accepted_value):
        """Sets the has_maximum_accepted_value of this VariablePresentation.


        :param has_maximum_accepted_value: The has_maximum_accepted_value of this VariablePresentation.
        :type has_maximum_accepted_value: List[str]
        """

        self._has_maximum_accepted_value = has_maximum_accepted_value

    @property
    def has_constraint(self):
        """Gets the has_constraint of this VariablePresentation.


        :return: The has_constraint of this VariablePresentation.
        :rtype: List[str]
        """
        return self._has_constraint

    @has_constraint.setter
    def has_constraint(self, has_constraint):
        """Sets the has_constraint of this VariablePresentation.


        :param has_constraint: The has_constraint of this VariablePresentation.
        :type has_constraint: List[str]
        """

        self._has_constraint = has_constraint

    @property
    def description(self):
        """Gets the description of this VariablePresentation.


        :return: The description of this VariablePresentation.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariablePresentation.


        :param description: The description of this VariablePresentation.
        :type description: List[str]
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this VariablePresentation.


        :return: The label of this VariablePresentation.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VariablePresentation.


        :param label: The label of this VariablePresentation.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this VariablePresentation.


        :return: The type of this VariablePresentation.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VariablePresentation.


        :param type: The type of this VariablePresentation.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_long_name(self):
        """Gets the has_long_name of this VariablePresentation.


        :return: The has_long_name of this VariablePresentation.
        :rtype: List[str]
        """
        return self._has_long_name

    @has_long_name.setter
    def has_long_name(self, has_long_name):
        """Sets the has_long_name of this VariablePresentation.


        :param has_long_name: The has_long_name of this VariablePresentation.
        :type has_long_name: List[str]
        """

        self._has_long_name = has_long_name

    @property
    def has_short_name(self):
        """Gets the has_short_name of this VariablePresentation.


        :return: The has_short_name of this VariablePresentation.
        :rtype: List[str]
        """
        return self._has_short_name

    @has_short_name.setter
    def has_short_name(self, has_short_name):
        """Sets the has_short_name of this VariablePresentation.


        :param has_short_name: The has_short_name of this VariablePresentation.
        :type has_short_name: List[str]
        """

        self._has_short_name = has_short_name

    @property
    def has_minimum_accepted_value(self):
        """Gets the has_minimum_accepted_value of this VariablePresentation.


        :return: The has_minimum_accepted_value of this VariablePresentation.
        :rtype: List[str]
        """
        return self._has_minimum_accepted_value

    @has_minimum_accepted_value.setter
    def has_minimum_accepted_value(self, has_minimum_accepted_value):
        """Sets the has_minimum_accepted_value of this VariablePresentation.


        :param has_minimum_accepted_value: The has_minimum_accepted_value of this VariablePresentation.
        :type has_minimum_accepted_value: List[str]
        """

        self._has_minimum_accepted_value = has_minimum_accepted_value

    @property
    def id(self):
        """Gets the id of this VariablePresentation.


        :return: The id of this VariablePresentation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VariablePresentation.


        :param id: The id of this VariablePresentation.
        :type id: str
        """

        self._id = id

    @property
    def part_of_dataset(self):
        """Gets the part_of_dataset of this VariablePresentation.


        :return: The part_of_dataset of this VariablePresentation.
        :rtype: List[DatasetSpecification]
        """
        return self._part_of_dataset

    @part_of_dataset.setter
    def part_of_dataset(self, part_of_dataset):
        """Sets the part_of_dataset of this VariablePresentation.


        :param part_of_dataset: The part_of_dataset of this VariablePresentation.
        :type part_of_dataset: List[DatasetSpecification]
        """

        self._part_of_dataset = part_of_dataset

    @property
    def uses_unit(self):
        """Gets the uses_unit of this VariablePresentation.


        :return: The uses_unit of this VariablePresentation.
        :rtype: List[object]
        """
        return self._uses_unit

    @uses_unit.setter
    def uses_unit(self, uses_unit):
        """Sets the uses_unit of this VariablePresentation.


        :param uses_unit: The uses_unit of this VariablePresentation.
        :type uses_unit: List[object]
        """

        self._uses_unit = uses_unit
