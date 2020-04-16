# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TheoryGuidedModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_funding=None, keywords=None, has_documentation=None, has_grid=None, support_details=None, software_requirements=None, has_version=None, has_typical_data_source=None, has_download_url=None, description=None, reference_publication=None, screenshot=None, type=None, has_installation_instructions=None, has_model_category=None, had_primary_source=None, date_created=None, compatible_visualization_software=None, contributor=None, has_faq=None, logo=None, has_contact_person=None, has_purpose=None, id=None, has_sample_visualization=None, identifier=None, memory_requirements=None, website=None, citation=None, author=None, processor_requirements=None, has_usage_notes=None, short_description=None, label=None, has_assumption=None, date_published=None, operating_systems=None, license=None, has_source_code=None, has_explanation_diagram=None, has_example=None, publisher=None, has_equation=None, useful_for_calculating_index=None):  # noqa: E501
        """TheoryGuidedModel - a model defined in OpenAPI

        :param has_funding: The has_funding of this TheoryGuidedModel.  # noqa: E501
        :type has_funding: List[FundingInformation]
        :param keywords: The keywords of this TheoryGuidedModel.  # noqa: E501
        :type keywords: List[str]
        :param has_documentation: The has_documentation of this TheoryGuidedModel.  # noqa: E501
        :type has_documentation: List[str]
        :param has_grid: The has_grid of this TheoryGuidedModel.  # noqa: E501
        :type has_grid: List[Grid]
        :param support_details: The support_details of this TheoryGuidedModel.  # noqa: E501
        :type support_details: List[str]
        :param software_requirements: The software_requirements of this TheoryGuidedModel.  # noqa: E501
        :type software_requirements: List[str]
        :param has_version: The has_version of this TheoryGuidedModel.  # noqa: E501
        :type has_version: List[SoftwareVersion]
        :param has_typical_data_source: The has_typical_data_source of this TheoryGuidedModel.  # noqa: E501
        :type has_typical_data_source: List[str]
        :param has_download_url: The has_download_url of this TheoryGuidedModel.  # noqa: E501
        :type has_download_url: List[str]
        :param description: The description of this TheoryGuidedModel.  # noqa: E501
        :type description: List[str]
        :param reference_publication: The reference_publication of this TheoryGuidedModel.  # noqa: E501
        :type reference_publication: List[str]
        :param screenshot: The screenshot of this TheoryGuidedModel.  # noqa: E501
        :type screenshot: List[Image]
        :param type: The type of this TheoryGuidedModel.  # noqa: E501
        :type type: List[str]
        :param has_installation_instructions: The has_installation_instructions of this TheoryGuidedModel.  # noqa: E501
        :type has_installation_instructions: List[str]
        :param has_model_category: The has_model_category of this TheoryGuidedModel.  # noqa: E501
        :type has_model_category: List[str]
        :param had_primary_source: The had_primary_source of this TheoryGuidedModel.  # noqa: E501
        :type had_primary_source: List[object]
        :param date_created: The date_created of this TheoryGuidedModel.  # noqa: E501
        :type date_created: List[str]
        :param compatible_visualization_software: The compatible_visualization_software of this TheoryGuidedModel.  # noqa: E501
        :type compatible_visualization_software: List[Software]
        :param contributor: The contributor of this TheoryGuidedModel.  # noqa: E501
        :type contributor: List[Person]
        :param has_faq: The has_faq of this TheoryGuidedModel.  # noqa: E501
        :type has_faq: List[str]
        :param logo: The logo of this TheoryGuidedModel.  # noqa: E501
        :type logo: List[Image]
        :param has_contact_person: The has_contact_person of this TheoryGuidedModel.  # noqa: E501
        :type has_contact_person: List[object]
        :param has_purpose: The has_purpose of this TheoryGuidedModel.  # noqa: E501
        :type has_purpose: List[str]
        :param id: The id of this TheoryGuidedModel.  # noqa: E501
        :type id: str
        :param has_sample_visualization: The has_sample_visualization of this TheoryGuidedModel.  # noqa: E501
        :type has_sample_visualization: List[Visualization]
        :param identifier: The identifier of this TheoryGuidedModel.  # noqa: E501
        :type identifier: List[str]
        :param memory_requirements: The memory_requirements of this TheoryGuidedModel.  # noqa: E501
        :type memory_requirements: List[str]
        :param website: The website of this TheoryGuidedModel.  # noqa: E501
        :type website: List[str]
        :param citation: The citation of this TheoryGuidedModel.  # noqa: E501
        :type citation: List[str]
        :param author: The author of this TheoryGuidedModel.  # noqa: E501
        :type author: List[object]
        :param processor_requirements: The processor_requirements of this TheoryGuidedModel.  # noqa: E501
        :type processor_requirements: List[str]
        :param has_usage_notes: The has_usage_notes of this TheoryGuidedModel.  # noqa: E501
        :type has_usage_notes: List[str]
        :param short_description: The short_description of this TheoryGuidedModel.  # noqa: E501
        :type short_description: List[str]
        :param label: The label of this TheoryGuidedModel.  # noqa: E501
        :type label: List[str]
        :param has_assumption: The has_assumption of this TheoryGuidedModel.  # noqa: E501
        :type has_assumption: List[str]
        :param date_published: The date_published of this TheoryGuidedModel.  # noqa: E501
        :type date_published: List[str]
        :param operating_systems: The operating_systems of this TheoryGuidedModel.  # noqa: E501
        :type operating_systems: List[str]
        :param license: The license of this TheoryGuidedModel.  # noqa: E501
        :type license: List[str]
        :param has_source_code: The has_source_code of this TheoryGuidedModel.  # noqa: E501
        :type has_source_code: List[SourceCode]
        :param has_explanation_diagram: The has_explanation_diagram of this TheoryGuidedModel.  # noqa: E501
        :type has_explanation_diagram: List[Image]
        :param has_example: The has_example of this TheoryGuidedModel.  # noqa: E501
        :type has_example: List[str]
        :param publisher: The publisher of this TheoryGuidedModel.  # noqa: E501
        :type publisher: List[object]
        :param has_equation: The has_equation of this TheoryGuidedModel.  # noqa: E501
        :type has_equation: List[Equation]
        :param useful_for_calculating_index: The useful_for_calculating_index of this TheoryGuidedModel.  # noqa: E501
        :type useful_for_calculating_index: List[NumericalIndex]
        """
        from openapi_server.models.equation import Equation
        from openapi_server.models.funding_information import FundingInformation
        from openapi_server.models.grid import Grid
        from openapi_server.models.image import Image
        from openapi_server.models.numerical_index import NumericalIndex
        from openapi_server.models.person import Person
        from openapi_server.models.software import Software
        from openapi_server.models.software_version import SoftwareVersion
        from openapi_server.models.source_code import SourceCode
        from openapi_server.models.visualization import Visualization

          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'has_funding': List[FundingInformation],
            'keywords': List[str],
            'has_documentation': List[str],
            'has_grid': List[Grid],
            'support_details': List[str],
            'software_requirements': List[str],
            'has_version': List[SoftwareVersion],
            'has_typical_data_source': List[str],
            'has_download_url': List[str],
            'description': List[str],
            'reference_publication': List[str],
            'screenshot': List[Image],
            'type': List[str],
            'has_installation_instructions': List[str],
            'has_model_category': List[str],
            'had_primary_source': List[object],
            'date_created': List[str],
            'compatible_visualization_software': List[Software],
            'contributor': List[Person],
            'has_faq': List[str],
            'logo': List[Image],
            'has_contact_person': List[object],
            'has_purpose': List[str],
            'id': str,
            'has_sample_visualization': List[Visualization],
            'identifier': List[str],
            'memory_requirements': List[str],
            'website': List[str],
            'citation': List[str],
            'author': List[object],
            'processor_requirements': List[str],
            'has_usage_notes': List[str],
            'short_description': List[str],
            'label': List[str],
            'has_assumption': List[str],
            'date_published': List[str],
            'operating_systems': List[str],
            'license': List[str],
            'has_source_code': List[SourceCode],
            'has_explanation_diagram': List[Image],
            'has_example': List[str],
            'publisher': List[object],
            'has_equation': List[Equation],
            'useful_for_calculating_index': List[NumericalIndex]
        }

        self.attribute_map = {
            'has_funding': 'hasFunding',
            'keywords': 'keywords',
            'has_documentation': 'hasDocumentation',
            'has_grid': 'hasGrid',
            'support_details': 'supportDetails',
            'software_requirements': 'softwareRequirements',
            'has_version': 'hasVersion',
            'has_typical_data_source': 'hasTypicalDataSource',
            'has_download_url': 'hasDownloadURL',
            'description': 'description',
            'reference_publication': 'referencePublication',
            'screenshot': 'screenshot',
            'type': 'type',
            'has_installation_instructions': 'hasInstallationInstructions',
            'has_model_category': 'hasModelCategory',
            'had_primary_source': 'hadPrimarySource',
            'date_created': 'dateCreated',
            'compatible_visualization_software': 'compatibleVisualizationSoftware',
            'contributor': 'contributor',
            'has_faq': 'hasFAQ',
            'logo': 'logo',
            'has_contact_person': 'hasContactPerson',
            'has_purpose': 'hasPurpose',
            'id': 'id',
            'has_sample_visualization': 'hasSampleVisualization',
            'identifier': 'identifier',
            'memory_requirements': 'memoryRequirements',
            'website': 'website',
            'citation': 'citation',
            'author': 'author',
            'processor_requirements': 'processorRequirements',
            'has_usage_notes': 'hasUsageNotes',
            'short_description': 'shortDescription',
            'label': 'label',
            'has_assumption': 'hasAssumption',
            'date_published': 'datePublished',
            'operating_systems': 'operatingSystems',
            'license': 'license',
            'has_source_code': 'hasSourceCode',
            'has_explanation_diagram': 'hasExplanationDiagram',
            'has_example': 'hasExample',
            'publisher': 'publisher',
            'has_equation': 'hasEquation',
            'useful_for_calculating_index': 'usefulForCalculatingIndex'
        }

        self._has_funding = has_funding
        self._keywords = keywords
        self._has_documentation = has_documentation
        self._has_grid = has_grid
        self._support_details = support_details
        self._software_requirements = software_requirements
        self._has_version = has_version
        self._has_typical_data_source = has_typical_data_source
        self._has_download_url = has_download_url
        self._description = description
        self._reference_publication = reference_publication
        self._screenshot = screenshot
        self._type = type
        self._has_installation_instructions = has_installation_instructions
        self._has_model_category = has_model_category
        self._had_primary_source = had_primary_source
        self._date_created = date_created
        self._compatible_visualization_software = compatible_visualization_software
        self._contributor = contributor
        self._has_faq = has_faq
        self._logo = logo
        self._has_contact_person = has_contact_person
        self._has_purpose = has_purpose
        self._id = id
        self._has_sample_visualization = has_sample_visualization
        self._identifier = identifier
        self._memory_requirements = memory_requirements
        self._website = website
        self._citation = citation
        self._author = author
        self._processor_requirements = processor_requirements
        self._has_usage_notes = has_usage_notes
        self._short_description = short_description
        self._label = label
        self._has_assumption = has_assumption
        self._date_published = date_published
        self._operating_systems = operating_systems
        self._license = license
        self._has_source_code = has_source_code
        self._has_explanation_diagram = has_explanation_diagram
        self._has_example = has_example
        self._publisher = publisher
        self._has_equation = has_equation
        self._useful_for_calculating_index = useful_for_calculating_index

    @classmethod
    def from_dict(cls, dikt) -> 'TheoryGuidedModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Theory-GuidedModel of this TheoryGuidedModel.  # noqa: E501
        :rtype: TheoryGuidedModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_funding(self):
        """Gets the has_funding of this TheoryGuidedModel.


        :return: The has_funding of this TheoryGuidedModel.
        :rtype: List[FundingInformation]
        """
        return self._has_funding

    @has_funding.setter
    def has_funding(self, has_funding):
        """Sets the has_funding of this TheoryGuidedModel.


        :param has_funding: The has_funding of this TheoryGuidedModel.
        :type has_funding: List[FundingInformation]
        """

        self._has_funding = has_funding

    @property
    def keywords(self):
        """Gets the keywords of this TheoryGuidedModel.


        :return: The keywords of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this TheoryGuidedModel.


        :param keywords: The keywords of this TheoryGuidedModel.
        :type keywords: List[str]
        """

        self._keywords = keywords

    @property
    def has_documentation(self):
        """Gets the has_documentation of this TheoryGuidedModel.


        :return: The has_documentation of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_documentation

    @has_documentation.setter
    def has_documentation(self, has_documentation):
        """Sets the has_documentation of this TheoryGuidedModel.


        :param has_documentation: The has_documentation of this TheoryGuidedModel.
        :type has_documentation: List[str]
        """

        self._has_documentation = has_documentation

    @property
    def has_grid(self):
        """Gets the has_grid of this TheoryGuidedModel.


        :return: The has_grid of this TheoryGuidedModel.
        :rtype: List[Grid]
        """
        return self._has_grid

    @has_grid.setter
    def has_grid(self, has_grid):
        """Sets the has_grid of this TheoryGuidedModel.


        :param has_grid: The has_grid of this TheoryGuidedModel.
        :type has_grid: List[Grid]
        """

        self._has_grid = has_grid

    @property
    def support_details(self):
        """Gets the support_details of this TheoryGuidedModel.


        :return: The support_details of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._support_details

    @support_details.setter
    def support_details(self, support_details):
        """Sets the support_details of this TheoryGuidedModel.


        :param support_details: The support_details of this TheoryGuidedModel.
        :type support_details: List[str]
        """

        self._support_details = support_details

    @property
    def software_requirements(self):
        """Gets the software_requirements of this TheoryGuidedModel.


        :return: The software_requirements of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._software_requirements

    @software_requirements.setter
    def software_requirements(self, software_requirements):
        """Sets the software_requirements of this TheoryGuidedModel.


        :param software_requirements: The software_requirements of this TheoryGuidedModel.
        :type software_requirements: List[str]
        """

        self._software_requirements = software_requirements

    @property
    def has_version(self):
        """Gets the has_version of this TheoryGuidedModel.


        :return: The has_version of this TheoryGuidedModel.
        :rtype: List[SoftwareVersion]
        """
        return self._has_version

    @has_version.setter
    def has_version(self, has_version):
        """Sets the has_version of this TheoryGuidedModel.


        :param has_version: The has_version of this TheoryGuidedModel.
        :type has_version: List[SoftwareVersion]
        """

        self._has_version = has_version

    @property
    def has_typical_data_source(self):
        """Gets the has_typical_data_source of this TheoryGuidedModel.


        :return: The has_typical_data_source of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_typical_data_source

    @has_typical_data_source.setter
    def has_typical_data_source(self, has_typical_data_source):
        """Sets the has_typical_data_source of this TheoryGuidedModel.


        :param has_typical_data_source: The has_typical_data_source of this TheoryGuidedModel.
        :type has_typical_data_source: List[str]
        """

        self._has_typical_data_source = has_typical_data_source

    @property
    def has_download_url(self):
        """Gets the has_download_url of this TheoryGuidedModel.


        :return: The has_download_url of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_download_url

    @has_download_url.setter
    def has_download_url(self, has_download_url):
        """Sets the has_download_url of this TheoryGuidedModel.


        :param has_download_url: The has_download_url of this TheoryGuidedModel.
        :type has_download_url: List[str]
        """

        self._has_download_url = has_download_url

    @property
    def description(self):
        """Gets the description of this TheoryGuidedModel.


        :return: The description of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TheoryGuidedModel.


        :param description: The description of this TheoryGuidedModel.
        :type description: List[str]
        """

        self._description = description

    @property
    def reference_publication(self):
        """Gets the reference_publication of this TheoryGuidedModel.


        :return: The reference_publication of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._reference_publication

    @reference_publication.setter
    def reference_publication(self, reference_publication):
        """Sets the reference_publication of this TheoryGuidedModel.


        :param reference_publication: The reference_publication of this TheoryGuidedModel.
        :type reference_publication: List[str]
        """

        self._reference_publication = reference_publication

    @property
    def screenshot(self):
        """Gets the screenshot of this TheoryGuidedModel.


        :return: The screenshot of this TheoryGuidedModel.
        :rtype: List[Image]
        """
        return self._screenshot

    @screenshot.setter
    def screenshot(self, screenshot):
        """Sets the screenshot of this TheoryGuidedModel.


        :param screenshot: The screenshot of this TheoryGuidedModel.
        :type screenshot: List[Image]
        """

        self._screenshot = screenshot

    @property
    def type(self):
        """Gets the type of this TheoryGuidedModel.


        :return: The type of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TheoryGuidedModel.


        :param type: The type of this TheoryGuidedModel.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_installation_instructions(self):
        """Gets the has_installation_instructions of this TheoryGuidedModel.


        :return: The has_installation_instructions of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_installation_instructions

    @has_installation_instructions.setter
    def has_installation_instructions(self, has_installation_instructions):
        """Sets the has_installation_instructions of this TheoryGuidedModel.


        :param has_installation_instructions: The has_installation_instructions of this TheoryGuidedModel.
        :type has_installation_instructions: List[str]
        """

        self._has_installation_instructions = has_installation_instructions

    @property
    def has_model_category(self):
        """Gets the has_model_category of this TheoryGuidedModel.


        :return: The has_model_category of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_model_category

    @has_model_category.setter
    def has_model_category(self, has_model_category):
        """Sets the has_model_category of this TheoryGuidedModel.


        :param has_model_category: The has_model_category of this TheoryGuidedModel.
        :type has_model_category: List[str]
        """

        self._has_model_category = has_model_category

    @property
    def had_primary_source(self):
        """Gets the had_primary_source of this TheoryGuidedModel.


        :return: The had_primary_source of this TheoryGuidedModel.
        :rtype: List[object]
        """
        return self._had_primary_source

    @had_primary_source.setter
    def had_primary_source(self, had_primary_source):
        """Sets the had_primary_source of this TheoryGuidedModel.


        :param had_primary_source: The had_primary_source of this TheoryGuidedModel.
        :type had_primary_source: List[object]
        """

        self._had_primary_source = had_primary_source

    @property
    def date_created(self):
        """Gets the date_created of this TheoryGuidedModel.


        :return: The date_created of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this TheoryGuidedModel.


        :param date_created: The date_created of this TheoryGuidedModel.
        :type date_created: List[str]
        """

        self._date_created = date_created

    @property
    def compatible_visualization_software(self):
        """Gets the compatible_visualization_software of this TheoryGuidedModel.


        :return: The compatible_visualization_software of this TheoryGuidedModel.
        :rtype: List[Software]
        """
        return self._compatible_visualization_software

    @compatible_visualization_software.setter
    def compatible_visualization_software(self, compatible_visualization_software):
        """Sets the compatible_visualization_software of this TheoryGuidedModel.


        :param compatible_visualization_software: The compatible_visualization_software of this TheoryGuidedModel.
        :type compatible_visualization_software: List[Software]
        """

        self._compatible_visualization_software = compatible_visualization_software

    @property
    def contributor(self):
        """Gets the contributor of this TheoryGuidedModel.


        :return: The contributor of this TheoryGuidedModel.
        :rtype: List[Person]
        """
        return self._contributor

    @contributor.setter
    def contributor(self, contributor):
        """Sets the contributor of this TheoryGuidedModel.


        :param contributor: The contributor of this TheoryGuidedModel.
        :type contributor: List[Person]
        """

        self._contributor = contributor

    @property
    def has_faq(self):
        """Gets the has_faq of this TheoryGuidedModel.


        :return: The has_faq of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_faq

    @has_faq.setter
    def has_faq(self, has_faq):
        """Sets the has_faq of this TheoryGuidedModel.


        :param has_faq: The has_faq of this TheoryGuidedModel.
        :type has_faq: List[str]
        """

        self._has_faq = has_faq

    @property
    def logo(self):
        """Gets the logo of this TheoryGuidedModel.


        :return: The logo of this TheoryGuidedModel.
        :rtype: List[Image]
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this TheoryGuidedModel.


        :param logo: The logo of this TheoryGuidedModel.
        :type logo: List[Image]
        """

        self._logo = logo

    @property
    def has_contact_person(self):
        """Gets the has_contact_person of this TheoryGuidedModel.


        :return: The has_contact_person of this TheoryGuidedModel.
        :rtype: List[object]
        """
        return self._has_contact_person

    @has_contact_person.setter
    def has_contact_person(self, has_contact_person):
        """Sets the has_contact_person of this TheoryGuidedModel.


        :param has_contact_person: The has_contact_person of this TheoryGuidedModel.
        :type has_contact_person: List[object]
        """

        self._has_contact_person = has_contact_person

    @property
    def has_purpose(self):
        """Gets the has_purpose of this TheoryGuidedModel.


        :return: The has_purpose of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_purpose

    @has_purpose.setter
    def has_purpose(self, has_purpose):
        """Sets the has_purpose of this TheoryGuidedModel.


        :param has_purpose: The has_purpose of this TheoryGuidedModel.
        :type has_purpose: List[str]
        """

        self._has_purpose = has_purpose

    @property
    def id(self):
        """Gets the id of this TheoryGuidedModel.


        :return: The id of this TheoryGuidedModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TheoryGuidedModel.


        :param id: The id of this TheoryGuidedModel.
        :type id: str
        """

        self._id = id

    @property
    def has_sample_visualization(self):
        """Gets the has_sample_visualization of this TheoryGuidedModel.


        :return: The has_sample_visualization of this TheoryGuidedModel.
        :rtype: List[Visualization]
        """
        return self._has_sample_visualization

    @has_sample_visualization.setter
    def has_sample_visualization(self, has_sample_visualization):
        """Sets the has_sample_visualization of this TheoryGuidedModel.


        :param has_sample_visualization: The has_sample_visualization of this TheoryGuidedModel.
        :type has_sample_visualization: List[Visualization]
        """

        self._has_sample_visualization = has_sample_visualization

    @property
    def identifier(self):
        """Gets the identifier of this TheoryGuidedModel.


        :return: The identifier of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this TheoryGuidedModel.


        :param identifier: The identifier of this TheoryGuidedModel.
        :type identifier: List[str]
        """

        self._identifier = identifier

    @property
    def memory_requirements(self):
        """Gets the memory_requirements of this TheoryGuidedModel.


        :return: The memory_requirements of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._memory_requirements

    @memory_requirements.setter
    def memory_requirements(self, memory_requirements):
        """Sets the memory_requirements of this TheoryGuidedModel.


        :param memory_requirements: The memory_requirements of this TheoryGuidedModel.
        :type memory_requirements: List[str]
        """

        self._memory_requirements = memory_requirements

    @property
    def website(self):
        """Gets the website of this TheoryGuidedModel.


        :return: The website of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this TheoryGuidedModel.


        :param website: The website of this TheoryGuidedModel.
        :type website: List[str]
        """

        self._website = website

    @property
    def citation(self):
        """Gets the citation of this TheoryGuidedModel.


        :return: The citation of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this TheoryGuidedModel.


        :param citation: The citation of this TheoryGuidedModel.
        :type citation: List[str]
        """

        self._citation = citation

    @property
    def author(self):
        """Gets the author of this TheoryGuidedModel.


        :return: The author of this TheoryGuidedModel.
        :rtype: List[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this TheoryGuidedModel.


        :param author: The author of this TheoryGuidedModel.
        :type author: List[object]
        """

        self._author = author

    @property
    def processor_requirements(self):
        """Gets the processor_requirements of this TheoryGuidedModel.


        :return: The processor_requirements of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._processor_requirements

    @processor_requirements.setter
    def processor_requirements(self, processor_requirements):
        """Sets the processor_requirements of this TheoryGuidedModel.


        :param processor_requirements: The processor_requirements of this TheoryGuidedModel.
        :type processor_requirements: List[str]
        """

        self._processor_requirements = processor_requirements

    @property
    def has_usage_notes(self):
        """Gets the has_usage_notes of this TheoryGuidedModel.


        :return: The has_usage_notes of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_usage_notes

    @has_usage_notes.setter
    def has_usage_notes(self, has_usage_notes):
        """Sets the has_usage_notes of this TheoryGuidedModel.


        :param has_usage_notes: The has_usage_notes of this TheoryGuidedModel.
        :type has_usage_notes: List[str]
        """

        self._has_usage_notes = has_usage_notes

    @property
    def short_description(self):
        """Gets the short_description of this TheoryGuidedModel.


        :return: The short_description of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this TheoryGuidedModel.


        :param short_description: The short_description of this TheoryGuidedModel.
        :type short_description: List[str]
        """

        self._short_description = short_description

    @property
    def label(self):
        """Gets the label of this TheoryGuidedModel.


        :return: The label of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TheoryGuidedModel.


        :param label: The label of this TheoryGuidedModel.
        :type label: List[str]
        """

        self._label = label

    @property
    def has_assumption(self):
        """Gets the has_assumption of this TheoryGuidedModel.


        :return: The has_assumption of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_assumption

    @has_assumption.setter
    def has_assumption(self, has_assumption):
        """Sets the has_assumption of this TheoryGuidedModel.


        :param has_assumption: The has_assumption of this TheoryGuidedModel.
        :type has_assumption: List[str]
        """

        self._has_assumption = has_assumption

    @property
    def date_published(self):
        """Gets the date_published of this TheoryGuidedModel.


        :return: The date_published of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this TheoryGuidedModel.


        :param date_published: The date_published of this TheoryGuidedModel.
        :type date_published: List[str]
        """

        self._date_published = date_published

    @property
    def operating_systems(self):
        """Gets the operating_systems of this TheoryGuidedModel.


        :return: The operating_systems of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """Sets the operating_systems of this TheoryGuidedModel.


        :param operating_systems: The operating_systems of this TheoryGuidedModel.
        :type operating_systems: List[str]
        """

        self._operating_systems = operating_systems

    @property
    def license(self):
        """Gets the license of this TheoryGuidedModel.


        :return: The license of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this TheoryGuidedModel.


        :param license: The license of this TheoryGuidedModel.
        :type license: List[str]
        """

        self._license = license

    @property
    def has_source_code(self):
        """Gets the has_source_code of this TheoryGuidedModel.


        :return: The has_source_code of this TheoryGuidedModel.
        :rtype: List[SourceCode]
        """
        return self._has_source_code

    @has_source_code.setter
    def has_source_code(self, has_source_code):
        """Sets the has_source_code of this TheoryGuidedModel.


        :param has_source_code: The has_source_code of this TheoryGuidedModel.
        :type has_source_code: List[SourceCode]
        """

        self._has_source_code = has_source_code

    @property
    def has_explanation_diagram(self):
        """Gets the has_explanation_diagram of this TheoryGuidedModel.


        :return: The has_explanation_diagram of this TheoryGuidedModel.
        :rtype: List[Image]
        """
        return self._has_explanation_diagram

    @has_explanation_diagram.setter
    def has_explanation_diagram(self, has_explanation_diagram):
        """Sets the has_explanation_diagram of this TheoryGuidedModel.


        :param has_explanation_diagram: The has_explanation_diagram of this TheoryGuidedModel.
        :type has_explanation_diagram: List[Image]
        """

        self._has_explanation_diagram = has_explanation_diagram

    @property
    def has_example(self):
        """Gets the has_example of this TheoryGuidedModel.


        :return: The has_example of this TheoryGuidedModel.
        :rtype: List[str]
        """
        return self._has_example

    @has_example.setter
    def has_example(self, has_example):
        """Sets the has_example of this TheoryGuidedModel.


        :param has_example: The has_example of this TheoryGuidedModel.
        :type has_example: List[str]
        """

        self._has_example = has_example

    @property
    def publisher(self):
        """Gets the publisher of this TheoryGuidedModel.


        :return: The publisher of this TheoryGuidedModel.
        :rtype: List[object]
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this TheoryGuidedModel.


        :param publisher: The publisher of this TheoryGuidedModel.
        :type publisher: List[object]
        """

        self._publisher = publisher

    @property
    def has_equation(self):
        """Gets the has_equation of this TheoryGuidedModel.


        :return: The has_equation of this TheoryGuidedModel.
        :rtype: List[Equation]
        """
        return self._has_equation

    @has_equation.setter
    def has_equation(self, has_equation):
        """Sets the has_equation of this TheoryGuidedModel.


        :param has_equation: The has_equation of this TheoryGuidedModel.
        :type has_equation: List[Equation]
        """

        self._has_equation = has_equation

    @property
    def useful_for_calculating_index(self):
        """Gets the useful_for_calculating_index of this TheoryGuidedModel.


        :return: The useful_for_calculating_index of this TheoryGuidedModel.
        :rtype: List[NumericalIndex]
        """
        return self._useful_for_calculating_index

    @useful_for_calculating_index.setter
    def useful_for_calculating_index(self, useful_for_calculating_index):
        """Sets the useful_for_calculating_index of this TheoryGuidedModel.


        :param useful_for_calculating_index: The useful_for_calculating_index of this TheoryGuidedModel.
        :type useful_for_calculating_index: List[NumericalIndex]
        """

        self._useful_for_calculating_index = useful_for_calculating_index
