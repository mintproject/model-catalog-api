# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Model(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_documentation=None, keywords=None, has_grid=None, software_requirements=None, has_version=None, has_typical_data_source=None, has_download_url=None, reference_publication=None, description=None, screenshot=None, type=None, has_installation_instructions=None, has_model_category=None, date_created=None, contributor=None, has_faq=None, logo=None, has_contact_person=None, has_purpose=None, id=None, has_sample_visualization=None, memory_requirements=None, identifier=None, website=None, citation=None, author=None, processor_requirements=None, short_description=None, label=None, has_assumption=None, date_published=None, operating_systems=None, license=None, has_source_code=None, has_explanation_diagram=None, has_equation=None, publisher=None, funding_source=None):  # noqa: E501
        """Model - a model defined in OpenAPI

        :param has_documentation: The has_documentation of this Model.  # noqa: E501
        :type has_documentation: List[str]
        :param keywords: The keywords of this Model.  # noqa: E501
        :type keywords: List[str]
        :param has_grid: The has_grid of this Model.  # noqa: E501
        :type has_grid: List[Grid]
        :param software_requirements: The software_requirements of this Model.  # noqa: E501
        :type software_requirements: List[str]
        :param has_version: The has_version of this Model.  # noqa: E501
        :type has_version: List[object]
        :param has_typical_data_source: The has_typical_data_source of this Model.  # noqa: E501
        :type has_typical_data_source: List[str]
        :param has_download_url: The has_download_url of this Model.  # noqa: E501
        :type has_download_url: List[str]
        :param reference_publication: The reference_publication of this Model.  # noqa: E501
        :type reference_publication: List[str]
        :param description: The description of this Model.  # noqa: E501
        :type description: List[str]
        :param screenshot: The screenshot of this Model.  # noqa: E501
        :type screenshot: List[object]
        :param type: The type of this Model.  # noqa: E501
        :type type: List[str]
        :param has_installation_instructions: The has_installation_instructions of this Model.  # noqa: E501
        :type has_installation_instructions: List[str]
        :param has_model_category: The has_model_category of this Model.  # noqa: E501
        :type has_model_category: List[str]
        :param date_created: The date_created of this Model.  # noqa: E501
        :type date_created: List[str]
        :param contributor: The contributor of this Model.  # noqa: E501
        :type contributor: List[object]
        :param has_faq: The has_faq of this Model.  # noqa: E501
        :type has_faq: List[str]
        :param logo: The logo of this Model.  # noqa: E501
        :type logo: List[object]
        :param has_contact_person: The has_contact_person of this Model.  # noqa: E501
        :type has_contact_person: List[object]
        :param has_purpose: The has_purpose of this Model.  # noqa: E501
        :type has_purpose: List[str]
        :param id: The id of this Model.  # noqa: E501
        :type id: str
        :param has_sample_visualization: The has_sample_visualization of this Model.  # noqa: E501
        :type has_sample_visualization: List[object]
        :param memory_requirements: The memory_requirements of this Model.  # noqa: E501
        :type memory_requirements: List[str]
        :param identifier: The identifier of this Model.  # noqa: E501
        :type identifier: List[str]
        :param website: The website of this Model.  # noqa: E501
        :type website: List[str]
        :param citation: The citation of this Model.  # noqa: E501
        :type citation: List[str]
        :param author: The author of this Model.  # noqa: E501
        :type author: List[object]
        :param processor_requirements: The processor_requirements of this Model.  # noqa: E501
        :type processor_requirements: List[str]
        :param short_description: The short_description of this Model.  # noqa: E501
        :type short_description: List[str]
        :param label: The label of this Model.  # noqa: E501
        :type label: str
        :param has_assumption: The has_assumption of this Model.  # noqa: E501
        :type has_assumption: List[str]
        :param date_published: The date_published of this Model.  # noqa: E501
        :type date_published: List[str]
        :param operating_systems: The operating_systems of this Model.  # noqa: E501
        :type operating_systems: List[str]
        :param license: The license of this Model.  # noqa: E501
        :type license: List[str]
        :param has_source_code: The has_source_code of this Model.  # noqa: E501
        :type has_source_code: List[object]
        :param has_explanation_diagram: The has_explanation_diagram of this Model.  # noqa: E501
        :type has_explanation_diagram: List[object]
        :param has_equation: The has_equation of this Model.  # noqa: E501
        :type has_equation: List[Equation]
        :param publisher: The publisher of this Model.  # noqa: E501
        :type publisher: List[object]
        :param funding_source: The funding_source of this Model.  # noqa: E501
        :type funding_source: List[object]
        """
        from openapi_server.models.equation import Equation
        from openapi_server.models.grid import Grid

          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'has_documentation': List[str],
            'keywords': List[str],
            'has_grid': List[Grid],
            'software_requirements': List[str],
            'has_version': List[object],
            'has_typical_data_source': List[str],
            'has_download_url': List[str],
            'reference_publication': List[str],
            'description': List[str],
            'screenshot': List[object],
            'type': List[str],
            'has_installation_instructions': List[str],
            'has_model_category': List[str],
            'date_created': List[str],
            'contributor': List[object],
            'has_faq': List[str],
            'logo': List[object],
            'has_contact_person': List[object],
            'has_purpose': List[str],
            'id': str,
            'has_sample_visualization': List[object],
            'memory_requirements': List[str],
            'identifier': List[str],
            'website': List[str],
            'citation': List[str],
            'author': List[object],
            'processor_requirements': List[str],
            'short_description': List[str],
            'label': str,
            'has_assumption': List[str],
            'date_published': List[str],
            'operating_systems': List[str],
            'license': List[str],
            'has_source_code': List[object],
            'has_explanation_diagram': List[object],
            'has_equation': List[Equation],
            'publisher': List[object],
            'funding_source': List[object]
        }

        self.attribute_map = {
            'has_documentation': 'hasDocumentation',
            'keywords': 'keywords',
            'has_grid': 'hasGrid',
            'software_requirements': 'softwareRequirements',
            'has_version': 'hasVersion',
            'has_typical_data_source': 'hasTypicalDataSource',
            'has_download_url': 'hasDownloadURL',
            'reference_publication': 'referencePublication',
            'description': 'description',
            'screenshot': 'screenshot',
            'type': 'type',
            'has_installation_instructions': 'hasInstallationInstructions',
            'has_model_category': 'hasModelCategory',
            'date_created': 'dateCreated',
            'contributor': 'contributor',
            'has_faq': 'hasFAQ',
            'logo': 'logo',
            'has_contact_person': 'hasContactPerson',
            'has_purpose': 'hasPurpose',
            'id': 'id',
            'has_sample_visualization': 'hasSampleVisualization',
            'memory_requirements': 'memoryRequirements',
            'identifier': 'identifier',
            'website': 'website',
            'citation': 'citation',
            'author': 'author',
            'processor_requirements': 'processorRequirements',
            'short_description': 'shortDescription',
            'label': 'label',
            'has_assumption': 'hasAssumption',
            'date_published': 'datePublished',
            'operating_systems': 'operatingSystems',
            'license': 'license',
            'has_source_code': 'hasSourceCode',
            'has_explanation_diagram': 'hasExplanationDiagram',
            'has_equation': 'hasEquation',
            'publisher': 'publisher',
            'funding_source': 'fundingSource'
        }

        self._has_documentation = has_documentation
        self._keywords = keywords
        self._has_grid = has_grid
        self._software_requirements = software_requirements
        self._has_version = has_version
        self._has_typical_data_source = has_typical_data_source
        self._has_download_url = has_download_url
        self._reference_publication = reference_publication
        self._description = description
        self._screenshot = screenshot
        self._type = type
        self._has_installation_instructions = has_installation_instructions
        self._has_model_category = has_model_category
        self._date_created = date_created
        self._contributor = contributor
        self._has_faq = has_faq
        self._logo = logo
        self._has_contact_person = has_contact_person
        self._has_purpose = has_purpose
        self._id = id
        self._has_sample_visualization = has_sample_visualization
        self._memory_requirements = memory_requirements
        self._identifier = identifier
        self._website = website
        self._citation = citation
        self._author = author
        self._processor_requirements = processor_requirements
        self._short_description = short_description
        self._label = label
        self._has_assumption = has_assumption
        self._date_published = date_published
        self._operating_systems = operating_systems
        self._license = license
        self._has_source_code = has_source_code
        self._has_explanation_diagram = has_explanation_diagram
        self._has_equation = has_equation
        self._publisher = publisher
        self._funding_source = funding_source

    @classmethod
    def from_dict(cls, dikt) -> 'Model':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Model of this Model.  # noqa: E501
        :rtype: Model
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_documentation(self):
        """Gets the has_documentation of this Model.


        :return: The has_documentation of this Model.
        :rtype: List[str]
        """
        return self._has_documentation

    @has_documentation.setter
    def has_documentation(self, has_documentation):
        """Sets the has_documentation of this Model.


        :param has_documentation: The has_documentation of this Model.
        :type has_documentation: List[str]
        """

        self._has_documentation = has_documentation

    @property
    def keywords(self):
        """Gets the keywords of this Model.


        :return: The keywords of this Model.
        :rtype: List[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Model.


        :param keywords: The keywords of this Model.
        :type keywords: List[str]
        """

        self._keywords = keywords

    @property
    def has_grid(self):
        """Gets the has_grid of this Model.


        :return: The has_grid of this Model.
        :rtype: List[Grid]
        """
        return self._has_grid

    @has_grid.setter
    def has_grid(self, has_grid):
        """Sets the has_grid of this Model.


        :param has_grid: The has_grid of this Model.
        :type has_grid: List[Grid]
        """

        self._has_grid = has_grid

    @property
    def software_requirements(self):
        """Gets the software_requirements of this Model.


        :return: The software_requirements of this Model.
        :rtype: List[str]
        """
        return self._software_requirements

    @software_requirements.setter
    def software_requirements(self, software_requirements):
        """Sets the software_requirements of this Model.


        :param software_requirements: The software_requirements of this Model.
        :type software_requirements: List[str]
        """

        self._software_requirements = software_requirements

    @property
    def has_version(self):
        """Gets the has_version of this Model.


        :return: The has_version of this Model.
        :rtype: List[object]
        """
        return self._has_version

    @has_version.setter
    def has_version(self, has_version):
        """Sets the has_version of this Model.


        :param has_version: The has_version of this Model.
        :type has_version: List[object]
        """

        self._has_version = has_version

    @property
    def has_typical_data_source(self):
        """Gets the has_typical_data_source of this Model.


        :return: The has_typical_data_source of this Model.
        :rtype: List[str]
        """
        return self._has_typical_data_source

    @has_typical_data_source.setter
    def has_typical_data_source(self, has_typical_data_source):
        """Sets the has_typical_data_source of this Model.


        :param has_typical_data_source: The has_typical_data_source of this Model.
        :type has_typical_data_source: List[str]
        """

        self._has_typical_data_source = has_typical_data_source

    @property
    def has_download_url(self):
        """Gets the has_download_url of this Model.


        :return: The has_download_url of this Model.
        :rtype: List[str]
        """
        return self._has_download_url

    @has_download_url.setter
    def has_download_url(self, has_download_url):
        """Sets the has_download_url of this Model.


        :param has_download_url: The has_download_url of this Model.
        :type has_download_url: List[str]
        """

        self._has_download_url = has_download_url

    @property
    def reference_publication(self):
        """Gets the reference_publication of this Model.


        :return: The reference_publication of this Model.
        :rtype: List[str]
        """
        return self._reference_publication

    @reference_publication.setter
    def reference_publication(self, reference_publication):
        """Sets the reference_publication of this Model.


        :param reference_publication: The reference_publication of this Model.
        :type reference_publication: List[str]
        """

        self._reference_publication = reference_publication

    @property
    def description(self):
        """Gets the description of this Model.


        :return: The description of this Model.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Model.


        :param description: The description of this Model.
        :type description: List[str]
        """

        self._description = description

    @property
    def screenshot(self):
        """Gets the screenshot of this Model.


        :return: The screenshot of this Model.
        :rtype: List[object]
        """
        return self._screenshot

    @screenshot.setter
    def screenshot(self, screenshot):
        """Sets the screenshot of this Model.


        :param screenshot: The screenshot of this Model.
        :type screenshot: List[object]
        """

        self._screenshot = screenshot

    @property
    def type(self):
        """Gets the type of this Model.


        :return: The type of this Model.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Model.


        :param type: The type of this Model.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_installation_instructions(self):
        """Gets the has_installation_instructions of this Model.


        :return: The has_installation_instructions of this Model.
        :rtype: List[str]
        """
        return self._has_installation_instructions

    @has_installation_instructions.setter
    def has_installation_instructions(self, has_installation_instructions):
        """Sets the has_installation_instructions of this Model.


        :param has_installation_instructions: The has_installation_instructions of this Model.
        :type has_installation_instructions: List[str]
        """

        self._has_installation_instructions = has_installation_instructions

    @property
    def has_model_category(self):
        """Gets the has_model_category of this Model.


        :return: The has_model_category of this Model.
        :rtype: List[str]
        """
        return self._has_model_category

    @has_model_category.setter
    def has_model_category(self, has_model_category):
        """Sets the has_model_category of this Model.


        :param has_model_category: The has_model_category of this Model.
        :type has_model_category: List[str]
        """

        self._has_model_category = has_model_category

    @property
    def date_created(self):
        """Gets the date_created of this Model.


        :return: The date_created of this Model.
        :rtype: List[str]
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Model.


        :param date_created: The date_created of this Model.
        :type date_created: List[str]
        """

        self._date_created = date_created

    @property
    def contributor(self):
        """Gets the contributor of this Model.


        :return: The contributor of this Model.
        :rtype: List[object]
        """
        return self._contributor

    @contributor.setter
    def contributor(self, contributor):
        """Sets the contributor of this Model.


        :param contributor: The contributor of this Model.
        :type contributor: List[object]
        """

        self._contributor = contributor

    @property
    def has_faq(self):
        """Gets the has_faq of this Model.


        :return: The has_faq of this Model.
        :rtype: List[str]
        """
        return self._has_faq

    @has_faq.setter
    def has_faq(self, has_faq):
        """Sets the has_faq of this Model.


        :param has_faq: The has_faq of this Model.
        :type has_faq: List[str]
        """

        self._has_faq = has_faq

    @property
    def logo(self):
        """Gets the logo of this Model.


        :return: The logo of this Model.
        :rtype: List[object]
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Model.


        :param logo: The logo of this Model.
        :type logo: List[object]
        """

        self._logo = logo

    @property
    def has_contact_person(self):
        """Gets the has_contact_person of this Model.


        :return: The has_contact_person of this Model.
        :rtype: List[object]
        """
        return self._has_contact_person

    @has_contact_person.setter
    def has_contact_person(self, has_contact_person):
        """Sets the has_contact_person of this Model.


        :param has_contact_person: The has_contact_person of this Model.
        :type has_contact_person: List[object]
        """

        self._has_contact_person = has_contact_person

    @property
    def has_purpose(self):
        """Gets the has_purpose of this Model.


        :return: The has_purpose of this Model.
        :rtype: List[str]
        """
        return self._has_purpose

    @has_purpose.setter
    def has_purpose(self, has_purpose):
        """Sets the has_purpose of this Model.


        :param has_purpose: The has_purpose of this Model.
        :type has_purpose: List[str]
        """

        self._has_purpose = has_purpose

    @property
    def id(self):
        """Gets the id of this Model.


        :return: The id of this Model.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Model.


        :param id: The id of this Model.
        :type id: str
        """

        self._id = id

    @property
    def has_sample_visualization(self):
        """Gets the has_sample_visualization of this Model.


        :return: The has_sample_visualization of this Model.
        :rtype: List[object]
        """
        return self._has_sample_visualization

    @has_sample_visualization.setter
    def has_sample_visualization(self, has_sample_visualization):
        """Sets the has_sample_visualization of this Model.


        :param has_sample_visualization: The has_sample_visualization of this Model.
        :type has_sample_visualization: List[object]
        """

        self._has_sample_visualization = has_sample_visualization

    @property
    def memory_requirements(self):
        """Gets the memory_requirements of this Model.


        :return: The memory_requirements of this Model.
        :rtype: List[str]
        """
        return self._memory_requirements

    @memory_requirements.setter
    def memory_requirements(self, memory_requirements):
        """Sets the memory_requirements of this Model.


        :param memory_requirements: The memory_requirements of this Model.
        :type memory_requirements: List[str]
        """

        self._memory_requirements = memory_requirements

    @property
    def identifier(self):
        """Gets the identifier of this Model.


        :return: The identifier of this Model.
        :rtype: List[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Model.


        :param identifier: The identifier of this Model.
        :type identifier: List[str]
        """

        self._identifier = identifier

    @property
    def website(self):
        """Gets the website of this Model.


        :return: The website of this Model.
        :rtype: List[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Model.


        :param website: The website of this Model.
        :type website: List[str]
        """

        self._website = website

    @property
    def citation(self):
        """Gets the citation of this Model.


        :return: The citation of this Model.
        :rtype: List[str]
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this Model.


        :param citation: The citation of this Model.
        :type citation: List[str]
        """

        self._citation = citation

    @property
    def author(self):
        """Gets the author of this Model.


        :return: The author of this Model.
        :rtype: List[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Model.


        :param author: The author of this Model.
        :type author: List[object]
        """

        self._author = author

    @property
    def processor_requirements(self):
        """Gets the processor_requirements of this Model.


        :return: The processor_requirements of this Model.
        :rtype: List[str]
        """
        return self._processor_requirements

    @processor_requirements.setter
    def processor_requirements(self, processor_requirements):
        """Sets the processor_requirements of this Model.


        :param processor_requirements: The processor_requirements of this Model.
        :type processor_requirements: List[str]
        """

        self._processor_requirements = processor_requirements

    @property
    def short_description(self):
        """Gets the short_description of this Model.


        :return: The short_description of this Model.
        :rtype: List[str]
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this Model.


        :param short_description: The short_description of this Model.
        :type short_description: List[str]
        """

        self._short_description = short_description

    @property
    def label(self):
        """Gets the label of this Model.


        :return: The label of this Model.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Model.


        :param label: The label of this Model.
        :type label: str
        """

        self._label = label

    @property
    def has_assumption(self):
        """Gets the has_assumption of this Model.


        :return: The has_assumption of this Model.
        :rtype: List[str]
        """
        return self._has_assumption

    @has_assumption.setter
    def has_assumption(self, has_assumption):
        """Sets the has_assumption of this Model.


        :param has_assumption: The has_assumption of this Model.
        :type has_assumption: List[str]
        """

        self._has_assumption = has_assumption

    @property
    def date_published(self):
        """Gets the date_published of this Model.


        :return: The date_published of this Model.
        :rtype: List[str]
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this Model.


        :param date_published: The date_published of this Model.
        :type date_published: List[str]
        """

        self._date_published = date_published

    @property
    def operating_systems(self):
        """Gets the operating_systems of this Model.


        :return: The operating_systems of this Model.
        :rtype: List[str]
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """Sets the operating_systems of this Model.


        :param operating_systems: The operating_systems of this Model.
        :type operating_systems: List[str]
        """

        self._operating_systems = operating_systems

    @property
    def license(self):
        """Gets the license of this Model.


        :return: The license of this Model.
        :rtype: List[str]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Model.


        :param license: The license of this Model.
        :type license: List[str]
        """

        self._license = license

    @property
    def has_source_code(self):
        """Gets the has_source_code of this Model.


        :return: The has_source_code of this Model.
        :rtype: List[object]
        """
        return self._has_source_code

    @has_source_code.setter
    def has_source_code(self, has_source_code):
        """Sets the has_source_code of this Model.


        :param has_source_code: The has_source_code of this Model.
        :type has_source_code: List[object]
        """

        self._has_source_code = has_source_code

    @property
    def has_explanation_diagram(self):
        """Gets the has_explanation_diagram of this Model.


        :return: The has_explanation_diagram of this Model.
        :rtype: List[object]
        """
        return self._has_explanation_diagram

    @has_explanation_diagram.setter
    def has_explanation_diagram(self, has_explanation_diagram):
        """Sets the has_explanation_diagram of this Model.


        :param has_explanation_diagram: The has_explanation_diagram of this Model.
        :type has_explanation_diagram: List[object]
        """

        self._has_explanation_diagram = has_explanation_diagram

    @property
    def has_equation(self):
        """Gets the has_equation of this Model.


        :return: The has_equation of this Model.
        :rtype: List[Equation]
        """
        return self._has_equation

    @has_equation.setter
    def has_equation(self, has_equation):
        """Sets the has_equation of this Model.


        :param has_equation: The has_equation of this Model.
        :type has_equation: List[Equation]
        """

        self._has_equation = has_equation

    @property
    def publisher(self):
        """Gets the publisher of this Model.


        :return: The publisher of this Model.
        :rtype: List[object]
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this Model.


        :param publisher: The publisher of this Model.
        :type publisher: List[object]
        """

        self._publisher = publisher

    @property
    def funding_source(self):
        """Gets the funding_source of this Model.


        :return: The funding_source of this Model.
        :rtype: List[object]
        """
        return self._funding_source

    @funding_source.setter
    def funding_source(self, funding_source):
        """Sets the funding_source of this Model.


        :param funding_source: The funding_source of this Model.
        :type funding_source: List[object]
        """

        self._funding_source = funding_source
