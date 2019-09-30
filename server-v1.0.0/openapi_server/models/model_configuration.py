# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ModelConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, parameter_assignment_method=None, has_component_location=None, has_grid=None, has_process=None, has_implementation_script_location=None, type=None, calibrated_variable=None, has_model_category=None, has_software_image=None, compatible_visualization_software=None, calibration_method=None, has_region=None, has_model_result_table=None, calibration_target_variable=None, id=None, has_expert_tuned_model=None, has_calibration=None, has_causal_diagram=None, has_sample_execution=None, has_sample_result=None, has_constraint=None, adjustable_parameter=None, has_support_script_location=None, label=None, has_execution_command=None, has_parameter=None, has_explanation_diagram=None, has_equation=None, has_output=None, has_output_time_interval=None, has_input=None):  # noqa: E501
        """ModelConfiguration - a model defined in OpenAPI

        :param parameter_assignment_method: The parameter_assignment_method of this ModelConfiguration.  # noqa: E501
        :type parameter_assignment_method: List[str]
        :param has_component_location: The has_component_location of this ModelConfiguration.  # noqa: E501
        :type has_component_location: List[str]
        :param has_grid: The has_grid of this ModelConfiguration.  # noqa: E501
        :type has_grid: List[Grid]
        :param has_process: The has_process of this ModelConfiguration.  # noqa: E501
        :type has_process: List[Process]
        :param has_implementation_script_location: The has_implementation_script_location of this ModelConfiguration.  # noqa: E501
        :type has_implementation_script_location: List[str]
        :param type: The type of this ModelConfiguration.  # noqa: E501
        :type type: List[str]
        :param calibrated_variable: The calibrated_variable of this ModelConfiguration.  # noqa: E501
        :type calibrated_variable: List[object]
        :param has_model_category: The has_model_category of this ModelConfiguration.  # noqa: E501
        :type has_model_category: List[str]
        :param has_software_image: The has_software_image of this ModelConfiguration.  # noqa: E501
        :type has_software_image: List[object]
        :param compatible_visualization_software: The compatible_visualization_software of this ModelConfiguration.  # noqa: E501
        :type compatible_visualization_software: List[object]
        :param calibration_method: The calibration_method of this ModelConfiguration.  # noqa: E501
        :type calibration_method: List[str]
        :param has_region: The has_region of this ModelConfiguration.  # noqa: E501
        :type has_region: List[Region]
        :param has_model_result_table: The has_model_result_table of this ModelConfiguration.  # noqa: E501
        :type has_model_result_table: List[str]
        :param calibration_target_variable: The calibration_target_variable of this ModelConfiguration.  # noqa: E501
        :type calibration_target_variable: List[object]
        :param id: The id of this ModelConfiguration.  # noqa: E501
        :type id: str
        :param has_expert_tuned_model: The has_expert_tuned_model of this ModelConfiguration.  # noqa: E501
        :type has_expert_tuned_model: List[ModelConfiguration]
        :param has_calibration: The has_calibration of this ModelConfiguration.  # noqa: E501
        :type has_calibration: List[ModelConfiguration]
        :param has_causal_diagram: The has_causal_diagram of this ModelConfiguration.  # noqa: E501
        :type has_causal_diagram: List[CausalDiagram]
        :param has_sample_execution: The has_sample_execution of this ModelConfiguration.  # noqa: E501
        :type has_sample_execution: List[object]
        :param has_sample_result: The has_sample_result of this ModelConfiguration.  # noqa: E501
        :type has_sample_result: List[object]
        :param has_constraint: The has_constraint of this ModelConfiguration.  # noqa: E501
        :type has_constraint: List[str]
        :param adjustable_parameter: The adjustable_parameter of this ModelConfiguration.  # noqa: E501
        :type adjustable_parameter: List[object]
        :param has_support_script_location: The has_support_script_location of this ModelConfiguration.  # noqa: E501
        :type has_support_script_location: List[str]
        :param label: The label of this ModelConfiguration.  # noqa: E501
        :type label: str
        :param has_execution_command: The has_execution_command of this ModelConfiguration.  # noqa: E501
        :type has_execution_command: List[str]
        :param has_parameter: The has_parameter of this ModelConfiguration.  # noqa: E501
        :type has_parameter: List[object]
        :param has_explanation_diagram: The has_explanation_diagram of this ModelConfiguration.  # noqa: E501
        :type has_explanation_diagram: List[object]
        :param has_equation: The has_equation of this ModelConfiguration.  # noqa: E501
        :type has_equation: List[Equation]
        :param has_output: The has_output of this ModelConfiguration.  # noqa: E501
        :type has_output: List[object]
        :param has_output_time_interval: The has_output_time_interval of this ModelConfiguration.  # noqa: E501
        :type has_output_time_interval: List[TimeInterval]
        :param has_input: The has_input of this ModelConfiguration.  # noqa: E501
        :type has_input: List[object]
        """
        from openapi_server.models.causal_diagram import CausalDiagram
        from openapi_server.models.equation import Equation
        from openapi_server.models.grid import Grid
        from openapi_server.models.process import Process
        from openapi_server.models.region import Region
        from openapi_server.models.time_interval import TimeInterval

          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'parameter_assignment_method': List[str],
            'has_component_location': List[str],
            'has_grid': List[Grid],
            'has_process': List[Process],
            'has_implementation_script_location': List[str],
            'type': List[str],
            'calibrated_variable': List[object],
            'has_model_category': List[str],
            'has_software_image': List[object],
            'compatible_visualization_software': List[object],
            'calibration_method': List[str],
            'has_region': List[Region],
            'has_model_result_table': List[str],
            'calibration_target_variable': List[object],
            'id': str,
            'has_expert_tuned_model': List[ModelConfiguration],
            'has_calibration': List[ModelConfiguration],
            'has_causal_diagram': List[CausalDiagram],
            'has_sample_execution': List[object],
            'has_sample_result': List[object],
            'has_constraint': List[str],
            'adjustable_parameter': List[object],
            'has_support_script_location': List[str],
            'label': str,
            'has_execution_command': List[str],
            'has_parameter': List[object],
            'has_explanation_diagram': List[object],
            'has_equation': List[Equation],
            'has_output': List[object],
            'has_output_time_interval': List[TimeInterval],
            'has_input': List[object]
        }

        self.attribute_map = {
            'parameter_assignment_method': 'parameterAssignmentMethod',
            'has_component_location': 'hasComponentLocation',
            'has_grid': 'hasGrid',
            'has_process': 'hasProcess',
            'has_implementation_script_location': 'hasImplementationScriptLocation',
            'type': 'type',
            'calibrated_variable': 'calibratedVariable',
            'has_model_category': 'hasModelCategory',
            'has_software_image': 'hasSoftwareImage',
            'compatible_visualization_software': 'compatibleVisualizationSoftware',
            'calibration_method': 'calibrationMethod',
            'has_region': 'hasRegion',
            'has_model_result_table': 'hasModelResultTable',
            'calibration_target_variable': 'calibrationTargetVariable',
            'id': 'id',
            'has_expert_tuned_model': 'hasExpertTunedModel',
            'has_calibration': 'hasCalibration',
            'has_causal_diagram': 'hasCausalDiagram',
            'has_sample_execution': 'hasSampleExecution',
            'has_sample_result': 'hasSampleResult',
            'has_constraint': 'hasConstraint',
            'adjustable_parameter': 'adjustableParameter',
            'has_support_script_location': 'hasSupportScriptLocation',
            'label': 'label',
            'has_execution_command': 'hasExecutionCommand',
            'has_parameter': 'hasParameter',
            'has_explanation_diagram': 'hasExplanationDiagram',
            'has_equation': 'hasEquation',
            'has_output': 'hasOutput',
            'has_output_time_interval': 'hasOutputTimeInterval',
            'has_input': 'hasInput'
        }

        self._parameter_assignment_method = parameter_assignment_method
        self._has_component_location = has_component_location
        self._has_grid = has_grid
        self._has_process = has_process
        self._has_implementation_script_location = has_implementation_script_location
        self._type = type
        self._calibrated_variable = calibrated_variable
        self._has_model_category = has_model_category
        self._has_software_image = has_software_image
        self._compatible_visualization_software = compatible_visualization_software
        self._calibration_method = calibration_method
        self._has_region = has_region
        self._has_model_result_table = has_model_result_table
        self._calibration_target_variable = calibration_target_variable
        self._id = id
        self._has_expert_tuned_model = has_expert_tuned_model
        self._has_calibration = has_calibration
        self._has_causal_diagram = has_causal_diagram
        self._has_sample_execution = has_sample_execution
        self._has_sample_result = has_sample_result
        self._has_constraint = has_constraint
        self._adjustable_parameter = adjustable_parameter
        self._has_support_script_location = has_support_script_location
        self._label = label
        self._has_execution_command = has_execution_command
        self._has_parameter = has_parameter
        self._has_explanation_diagram = has_explanation_diagram
        self._has_equation = has_equation
        self._has_output = has_output
        self._has_output_time_interval = has_output_time_interval
        self._has_input = has_input

    @classmethod
    def from_dict(cls, dikt) -> 'ModelConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModelConfiguration of this ModelConfiguration.  # noqa: E501
        :rtype: ModelConfiguration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parameter_assignment_method(self):
        """Gets the parameter_assignment_method of this ModelConfiguration.


        :return: The parameter_assignment_method of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._parameter_assignment_method

    @parameter_assignment_method.setter
    def parameter_assignment_method(self, parameter_assignment_method):
        """Sets the parameter_assignment_method of this ModelConfiguration.


        :param parameter_assignment_method: The parameter_assignment_method of this ModelConfiguration.
        :type parameter_assignment_method: List[str]
        """

        self._parameter_assignment_method = parameter_assignment_method

    @property
    def has_component_location(self):
        """Gets the has_component_location of this ModelConfiguration.


        :return: The has_component_location of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._has_component_location

    @has_component_location.setter
    def has_component_location(self, has_component_location):
        """Sets the has_component_location of this ModelConfiguration.


        :param has_component_location: The has_component_location of this ModelConfiguration.
        :type has_component_location: List[str]
        """

        self._has_component_location = has_component_location

    @property
    def has_grid(self):
        """Gets the has_grid of this ModelConfiguration.


        :return: The has_grid of this ModelConfiguration.
        :rtype: List[Grid]
        """
        return self._has_grid

    @has_grid.setter
    def has_grid(self, has_grid):
        """Sets the has_grid of this ModelConfiguration.


        :param has_grid: The has_grid of this ModelConfiguration.
        :type has_grid: List[Grid]
        """

        self._has_grid = has_grid

    @property
    def has_process(self):
        """Gets the has_process of this ModelConfiguration.


        :return: The has_process of this ModelConfiguration.
        :rtype: List[Process]
        """
        return self._has_process

    @has_process.setter
    def has_process(self, has_process):
        """Sets the has_process of this ModelConfiguration.


        :param has_process: The has_process of this ModelConfiguration.
        :type has_process: List[Process]
        """

        self._has_process = has_process

    @property
    def has_implementation_script_location(self):
        """Gets the has_implementation_script_location of this ModelConfiguration.


        :return: The has_implementation_script_location of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._has_implementation_script_location

    @has_implementation_script_location.setter
    def has_implementation_script_location(self, has_implementation_script_location):
        """Sets the has_implementation_script_location of this ModelConfiguration.


        :param has_implementation_script_location: The has_implementation_script_location of this ModelConfiguration.
        :type has_implementation_script_location: List[str]
        """

        self._has_implementation_script_location = has_implementation_script_location

    @property
    def type(self):
        """Gets the type of this ModelConfiguration.


        :return: The type of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelConfiguration.


        :param type: The type of this ModelConfiguration.
        :type type: List[str]
        """

        self._type = type

    @property
    def calibrated_variable(self):
        """Gets the calibrated_variable of this ModelConfiguration.


        :return: The calibrated_variable of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._calibrated_variable

    @calibrated_variable.setter
    def calibrated_variable(self, calibrated_variable):
        """Sets the calibrated_variable of this ModelConfiguration.


        :param calibrated_variable: The calibrated_variable of this ModelConfiguration.
        :type calibrated_variable: List[object]
        """

        self._calibrated_variable = calibrated_variable

    @property
    def has_model_category(self):
        """Gets the has_model_category of this ModelConfiguration.


        :return: The has_model_category of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._has_model_category

    @has_model_category.setter
    def has_model_category(self, has_model_category):
        """Sets the has_model_category of this ModelConfiguration.


        :param has_model_category: The has_model_category of this ModelConfiguration.
        :type has_model_category: List[str]
        """

        self._has_model_category = has_model_category

    @property
    def has_software_image(self):
        """Gets the has_software_image of this ModelConfiguration.


        :return: The has_software_image of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._has_software_image

    @has_software_image.setter
    def has_software_image(self, has_software_image):
        """Sets the has_software_image of this ModelConfiguration.


        :param has_software_image: The has_software_image of this ModelConfiguration.
        :type has_software_image: List[object]
        """

        self._has_software_image = has_software_image

    @property
    def compatible_visualization_software(self):
        """Gets the compatible_visualization_software of this ModelConfiguration.


        :return: The compatible_visualization_software of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._compatible_visualization_software

    @compatible_visualization_software.setter
    def compatible_visualization_software(self, compatible_visualization_software):
        """Sets the compatible_visualization_software of this ModelConfiguration.


        :param compatible_visualization_software: The compatible_visualization_software of this ModelConfiguration.
        :type compatible_visualization_software: List[object]
        """

        self._compatible_visualization_software = compatible_visualization_software

    @property
    def calibration_method(self):
        """Gets the calibration_method of this ModelConfiguration.


        :return: The calibration_method of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._calibration_method

    @calibration_method.setter
    def calibration_method(self, calibration_method):
        """Sets the calibration_method of this ModelConfiguration.


        :param calibration_method: The calibration_method of this ModelConfiguration.
        :type calibration_method: List[str]
        """

        self._calibration_method = calibration_method

    @property
    def has_region(self):
        """Gets the has_region of this ModelConfiguration.


        :return: The has_region of this ModelConfiguration.
        :rtype: List[Region]
        """
        return self._has_region

    @has_region.setter
    def has_region(self, has_region):
        """Sets the has_region of this ModelConfiguration.


        :param has_region: The has_region of this ModelConfiguration.
        :type has_region: List[Region]
        """

        self._has_region = has_region

    @property
    def has_model_result_table(self):
        """Gets the has_model_result_table of this ModelConfiguration.


        :return: The has_model_result_table of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._has_model_result_table

    @has_model_result_table.setter
    def has_model_result_table(self, has_model_result_table):
        """Sets the has_model_result_table of this ModelConfiguration.


        :param has_model_result_table: The has_model_result_table of this ModelConfiguration.
        :type has_model_result_table: List[str]
        """

        self._has_model_result_table = has_model_result_table

    @property
    def calibration_target_variable(self):
        """Gets the calibration_target_variable of this ModelConfiguration.


        :return: The calibration_target_variable of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._calibration_target_variable

    @calibration_target_variable.setter
    def calibration_target_variable(self, calibration_target_variable):
        """Sets the calibration_target_variable of this ModelConfiguration.


        :param calibration_target_variable: The calibration_target_variable of this ModelConfiguration.
        :type calibration_target_variable: List[object]
        """

        self._calibration_target_variable = calibration_target_variable

    @property
    def id(self):
        """Gets the id of this ModelConfiguration.


        :return: The id of this ModelConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelConfiguration.


        :param id: The id of this ModelConfiguration.
        :type id: str
        """

        self._id = id

    @property
    def has_expert_tuned_model(self):
        """Gets the has_expert_tuned_model of this ModelConfiguration.


        :return: The has_expert_tuned_model of this ModelConfiguration.
        :rtype: List[ModelConfiguration]
        """
        return self._has_expert_tuned_model

    @has_expert_tuned_model.setter
    def has_expert_tuned_model(self, has_expert_tuned_model):
        """Sets the has_expert_tuned_model of this ModelConfiguration.


        :param has_expert_tuned_model: The has_expert_tuned_model of this ModelConfiguration.
        :type has_expert_tuned_model: List[ModelConfiguration]
        """

        self._has_expert_tuned_model = has_expert_tuned_model

    @property
    def has_calibration(self):
        """Gets the has_calibration of this ModelConfiguration.


        :return: The has_calibration of this ModelConfiguration.
        :rtype: List[ModelConfiguration]
        """
        return self._has_calibration

    @has_calibration.setter
    def has_calibration(self, has_calibration):
        """Sets the has_calibration of this ModelConfiguration.


        :param has_calibration: The has_calibration of this ModelConfiguration.
        :type has_calibration: List[ModelConfiguration]
        """

        self._has_calibration = has_calibration

    @property
    def has_causal_diagram(self):
        """Gets the has_causal_diagram of this ModelConfiguration.


        :return: The has_causal_diagram of this ModelConfiguration.
        :rtype: List[CausalDiagram]
        """
        return self._has_causal_diagram

    @has_causal_diagram.setter
    def has_causal_diagram(self, has_causal_diagram):
        """Sets the has_causal_diagram of this ModelConfiguration.


        :param has_causal_diagram: The has_causal_diagram of this ModelConfiguration.
        :type has_causal_diagram: List[CausalDiagram]
        """

        self._has_causal_diagram = has_causal_diagram

    @property
    def has_sample_execution(self):
        """Gets the has_sample_execution of this ModelConfiguration.


        :return: The has_sample_execution of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._has_sample_execution

    @has_sample_execution.setter
    def has_sample_execution(self, has_sample_execution):
        """Sets the has_sample_execution of this ModelConfiguration.


        :param has_sample_execution: The has_sample_execution of this ModelConfiguration.
        :type has_sample_execution: List[object]
        """

        self._has_sample_execution = has_sample_execution

    @property
    def has_sample_result(self):
        """Gets the has_sample_result of this ModelConfiguration.


        :return: The has_sample_result of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._has_sample_result

    @has_sample_result.setter
    def has_sample_result(self, has_sample_result):
        """Sets the has_sample_result of this ModelConfiguration.


        :param has_sample_result: The has_sample_result of this ModelConfiguration.
        :type has_sample_result: List[object]
        """

        self._has_sample_result = has_sample_result

    @property
    def has_constraint(self):
        """Gets the has_constraint of this ModelConfiguration.


        :return: The has_constraint of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._has_constraint

    @has_constraint.setter
    def has_constraint(self, has_constraint):
        """Sets the has_constraint of this ModelConfiguration.


        :param has_constraint: The has_constraint of this ModelConfiguration.
        :type has_constraint: List[str]
        """

        self._has_constraint = has_constraint

    @property
    def adjustable_parameter(self):
        """Gets the adjustable_parameter of this ModelConfiguration.


        :return: The adjustable_parameter of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._adjustable_parameter

    @adjustable_parameter.setter
    def adjustable_parameter(self, adjustable_parameter):
        """Sets the adjustable_parameter of this ModelConfiguration.


        :param adjustable_parameter: The adjustable_parameter of this ModelConfiguration.
        :type adjustable_parameter: List[object]
        """

        self._adjustable_parameter = adjustable_parameter

    @property
    def has_support_script_location(self):
        """Gets the has_support_script_location of this ModelConfiguration.


        :return: The has_support_script_location of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._has_support_script_location

    @has_support_script_location.setter
    def has_support_script_location(self, has_support_script_location):
        """Sets the has_support_script_location of this ModelConfiguration.


        :param has_support_script_location: The has_support_script_location of this ModelConfiguration.
        :type has_support_script_location: List[str]
        """

        self._has_support_script_location = has_support_script_location

    @property
    def label(self):
        """Gets the label of this ModelConfiguration.


        :return: The label of this ModelConfiguration.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModelConfiguration.


        :param label: The label of this ModelConfiguration.
        :type label: str
        """

        self._label = label

    @property
    def has_execution_command(self):
        """Gets the has_execution_command of this ModelConfiguration.


        :return: The has_execution_command of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._has_execution_command

    @has_execution_command.setter
    def has_execution_command(self, has_execution_command):
        """Sets the has_execution_command of this ModelConfiguration.


        :param has_execution_command: The has_execution_command of this ModelConfiguration.
        :type has_execution_command: List[str]
        """

        self._has_execution_command = has_execution_command

    @property
    def has_parameter(self):
        """Gets the has_parameter of this ModelConfiguration.


        :return: The has_parameter of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._has_parameter

    @has_parameter.setter
    def has_parameter(self, has_parameter):
        """Sets the has_parameter of this ModelConfiguration.


        :param has_parameter: The has_parameter of this ModelConfiguration.
        :type has_parameter: List[object]
        """

        self._has_parameter = has_parameter

    @property
    def has_explanation_diagram(self):
        """Gets the has_explanation_diagram of this ModelConfiguration.


        :return: The has_explanation_diagram of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._has_explanation_diagram

    @has_explanation_diagram.setter
    def has_explanation_diagram(self, has_explanation_diagram):
        """Sets the has_explanation_diagram of this ModelConfiguration.


        :param has_explanation_diagram: The has_explanation_diagram of this ModelConfiguration.
        :type has_explanation_diagram: List[object]
        """

        self._has_explanation_diagram = has_explanation_diagram

    @property
    def has_equation(self):
        """Gets the has_equation of this ModelConfiguration.


        :return: The has_equation of this ModelConfiguration.
        :rtype: List[Equation]
        """
        return self._has_equation

    @has_equation.setter
    def has_equation(self, has_equation):
        """Sets the has_equation of this ModelConfiguration.


        :param has_equation: The has_equation of this ModelConfiguration.
        :type has_equation: List[Equation]
        """

        self._has_equation = has_equation

    @property
    def has_output(self):
        """Gets the has_output of this ModelConfiguration.


        :return: The has_output of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._has_output

    @has_output.setter
    def has_output(self, has_output):
        """Sets the has_output of this ModelConfiguration.


        :param has_output: The has_output of this ModelConfiguration.
        :type has_output: List[object]
        """

        self._has_output = has_output

    @property
    def has_output_time_interval(self):
        """Gets the has_output_time_interval of this ModelConfiguration.


        :return: The has_output_time_interval of this ModelConfiguration.
        :rtype: List[TimeInterval]
        """
        return self._has_output_time_interval

    @has_output_time_interval.setter
    def has_output_time_interval(self, has_output_time_interval):
        """Sets the has_output_time_interval of this ModelConfiguration.


        :param has_output_time_interval: The has_output_time_interval of this ModelConfiguration.
        :type has_output_time_interval: List[TimeInterval]
        """

        self._has_output_time_interval = has_output_time_interval

    @property
    def has_input(self):
        """Gets the has_input of this ModelConfiguration.


        :return: The has_input of this ModelConfiguration.
        :rtype: List[object]
        """
        return self._has_input

    @has_input.setter
    def has_input(self, has_input):
        """Sets the has_input of this ModelConfiguration.


        :param has_input: The has_input of this ModelConfiguration.
        :type has_input: List[object]
        """

        self._has_input = has_input
