# Pattern for INSERT query call names
INSERT_PATTERN = "INSERT DATA { GRAPH ?_g_iri { <s> <p> <o> }}"

DEFAULT_MINT_INSTANCE = "https://w3id.org/mint/instance/"


PREFIX_CONTEXT = {
    "qudt": "http://qudt.org/schema/qudt/",
    "owl": "http://www.w3.org/2002/07/owl",
    "xsd": "http://www.w3.org/2001/XMLSchema",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns",
    "purl": "http://purl.org/dc/terms/",
    "mc": "https://w3id.org/mint/modelCatalog#",
    "wingsexport": "https://w3id.org/wings/export/",
    "onsf": "http://ontosoft.org/software#",
    "label": "rdf:label"
}
PREDICATE_CONTEXT = {
    "has_file_structure": "https://w3id.org/mint/modelCatalog#hasFileStructure",
     "has_configuration": "https://w3id.org/mint/modelCatalog#hasConfiguration",
     "has_support_script_location": "https://w3id.org/mint/modelCatalog#hasSupportScriptLocation",
     "has_identifier": "http://ontosoft.org/software#hasIdentifier",
     "has_version_id": "http://ontosoft.org/software#hasVersionId",
     "had_grid": "https://w3id.org/mint/modelCatalog#hadGrid",
     "has_data_type": "https://w3id.org/mint/modelCatalog#hasDataType",
     "has_process": "https://w3id.org/mint/modelCatalog#hasProcess",
     "has_container": "http://ontosoft.org/software#hasContainer",
     "has_implementation_script_location": "http://ontosoft.org/software#hasImplementationScriptLocation",
     "has_installation_instructions": "http://ontosoft.org/software#hasInstallationInstructions",
     "has_presentation": "https://w3id.org/mint/modelCatalog#hasPresentation",
     "has_default_value": "https://w3id.org/mint/modelCatalog#hasDefaultValue",
     "has_constraint": "https://w3id.org/mint/modelCatalog#hasConstraint",
     "has_module": "https://w3id.org/mint/modelCatalog#hasModule",
     "has_documentation": "http://ontosoft.org/software#hasDocumentation",
     "has_cag": "https://w3id.org/mint/modelCatalog#hasCAG",
     "has_standard_variable": "https://w3id.org/mint/modelCatalog#hasStandardVariable",
     "has_short_name": "https://w3id.org/mint/modelCatalog#hasShortName",
     "has_parameter": "https://w3id.org/mint/modelCatalog#hasParameter",
     "influences": "https://w3id.org/mint/modelCatalog#influences",
     "has_relevance_level": "https://w3id.org/mint/modelCatalog#hasRelevanceLevel",
     "has_assumption": "https://w3id.org/mint/modelCatalog#hasAssumption",
     "has_maximum_accepted_value": "https://w3id.org/mint/modelCatalog#hasMaximumAcceptedValue",
     "has_dimensionality": "https://w3id.org/mint/modelCatalog#hasDimensionality",
     "has_part": "https://w3id.org/mint/modelCatalog#hasPart",
     "has_value": "https://w3id.org/mint/modelCatalog#hasValue",
     "has_input": "https://w3id.org/mint/modelCatalog#hasInput",
     "has_long_name": "https://w3id.org/mint/modelCatalog#hasLongName",
     "has_output": "https://w3id.org/mint/modelCatalog#hasOutput",
     "uses_unit": "https://w3id.org/mint/modelCatalog#usesUnit",
     "has_dataset": "https://w3id.org/mint/modelCatalog#hasDataset",
     "description": "http://purl.org/dc/terms/description",
     "has_time_interval": "https://w3id.org/mint/modelCatalog#hasTimeInterval",
     "has_format": "https://w3id.org/mint/modelCatalog#hasFormat",
     "has_execution_command": "http://ontosoft.org/software#hasExecutionCommand",
     "has_minimum_accepted_value": "https://w3id.org/mint/modelCatalog#hasMinimumAcceptedValue",
     "has_model_category": "https://w3id.org/mint/modelCatalog#hasModelCategory",
     "has_software_version": "http://ontosoft.org/software#hasSoftwareVersion",
     "has_component_location": "https://w3id.org/mint/modelCatalog#hasComponentLocation",
     "abbreviation": "http://qudt.org/schema/qudt/abbreviation"
}
MINT_CONTEXT = PREFIX_CONTEXT.update(PREDICATE_CONTEXT)
# todo: support unit

MODELCONFIGURTION_TYPE = "mc:ModelConfiguration"
CAG_TYPE = "mc:CAG"
CONCEPT_TYPE = "mc:CONCEPT"
DATASTRUCTUREDEFINITION_TYPE = "mc:DataStructureDefinition"
DATASET_TYPE = "mc:Dataset"
DATASETSPECIFICATION_TYPE = "mc:DatasetSpecification"
EMPIRICALMODEL_TYPE = "mc:EmpiricalModel"
GRID_TYPE = "mc:Grid"
GSNVARIABLE_TYPE = "mc:GSNVariable"
HYBRIDMODEL_TYPE = "mc:HybridModel"
ICASAVARIABLE_TYPE = "mc:ICASAVariable"
MODEL_TYPE = "mc:Model"
MODELCONFIGURATION_TYPE = "mc:ModelConfiguration"
MODELVERSION_TYPE = "mc:ModelVersion"
MODULE_TYPE = "mc:Module"
PARAMETER_TYPE = "mc:Parameter"
PROCESS_TYPE = "mc:Process"
STANDARDVARIABLE_TYPE = "mc:StandardVariable"
THEORYBASEDMODEL_TYPE = "mc:TheoryBasedModel"
TIMEINTERVAL_TYPE = "mc:TimeInterval"
UNIT_TYPE = "mc:Unit"
VARIABLE_TYPE = "mc:Variable"

# todo: a relation can be PROCESS_TYPE or PARAMETER_TYPE
MAPPING_TYPE = {
    'has_file_structure': 'mc:DataStructureDefinition',
    'has_configuration': 'mc:ModelConfiguration',
    'had_grid': 'mc:Grid',
    'has_container': 'onsf:Container',
    'has_module': 'mc:Module',
    'has_standard_variable': 'mc:StandardVariable',
    'has_input': 'mc:DatasetSpecification',
    'has_output': 'mc:DatasetSpecification',
    'uses_unit': 'qudt:Unit',
    'has_software_version': 'onsf:SoftwareVersion',
    "has_process": PROCESS_TYPE,
    "has_cag": CAG_TYPE,
    "has_time_interval": TIMEINTERVAL_TYPE,
    "has_parameter": PARAMETER_TYPE,
    "influences": PROCESS_TYPE,
    "has_presentation": VARIABLE_TYPE
}

SUPPORTED_CLASSES = [class_type for class_type, _ in MAPPING_TYPE.items()]
