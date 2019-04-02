# Pattern for INSERT query call names
INSERT_PATTERN = "INSERT DATA { GRAPH ?_g_iri { <s> <p> <o> }}"

DEFAULT_MINT_INSTANCE = "https://w3id.org/mint/instance/"

MINT_CONTEXT = {
    "qudt": "http://qudt.org/schema/qudt",
    "owl": "http://www.w3.org/2002/07/owl",
    "xsd": "http://www.w3.org/2001/XMLSchema",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns",
    "purl": "http://purl.org/dc/terms/",
    "mc": "https://w3id.org/mint/modelCatalog#",
    "wingsexport": "https://w3id.org/wings/export/",
    "onsf": "http://ontosoft.org/software#",
    "label": "rdf:label",
'has_file_structure': 'mc:hasFileStructure',
 'has_configuration': 'mc:hasConfiguration',
 'has_support_script_location': 'mc:hasSupportScriptLocation',
 'has_identifier': 'onsf:hasIdentifier',
 'has_version_id': 'onsf:hasVersionId',
 'had_grid': 'mc:hadGrid',
 'has_data_type': 'mc:hasDataType',
 'has_process': 'mc:hasProcess',
 'has_container': 'onsf:hasContainer',
 'has_implementation_script_location': 'onsf:hasImplementationScriptLocation',
 'has_installation_instructions': 'onsf:hasInstallationInstructions',
 'has_presentation': 'mc:hasPresentation',
 'has_default_value': 'mc:hasDefaultValue',
 'has_constraint': 'mc:hasConstraint',
 'has_module': 'mc:hasModule',
 'has_documentation': 'onsf:hasDocumentation',
 'has_cag': 'mc:hasCAG',
 'has_standard_variable': 'mc:hasStandardVariable',
 'has_short_name': 'mc:hasShortName',
 'has_parameter': 'mc:hasParameter',
 'influences': 'mc:influences',
 'has_relevance_level': 'mc:hasRelevanceLevel',
 'has_assumption': 'mc:hasAssumption',
 'has_maximum_accepted_value': 'mc:hasMaximumAcceptedValue',
 'has_dimensionality': 'mc:hasDimensionality',
 'has_part': 'mc:hasPart',
 'has_value': 'mc:hasValue',
 'has_input': 'mc:hasInput',
 'has_long_name': 'mc:hasLongName',
 'has_output': 'mc:hasOutput',
 'uses_unit': 'mc:usesUnit',
 'has_dataset': 'mc:hasDataset',
 'description': 'purl:description',
 'has_time_interval': 'mc:hasTimeInterval',
 'has_format': 'mc:hasFormat',
 'has_execution_command': 'onsf:hasExecutionCommand',
 'has_minimum_accepted_value': 'mc:hasMinimumAcceptedValue',
 'has_model_category': 'mc:hasModelCategory',
 'has_software_version': 'onsf:hasSoftwareVersion',
 'has_component_location': 'mc:hasComponentLocation',
 'abbreviation': 'qudt:abbreviation'
}
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
    "has_input": DATASET_TYPE,
    "has_output": DATASET_TYPE,
    "has_process": PROCESS_TYPE,
    "has_cag": CAG_TYPE,
    "has_time_interval": TIMEINTERVAL_TYPE,
    "has_parameter": PARAMETER_TYPE,
    "influences": PROCESS_TYPE,
    "has_presentation": VARIABLE_TYPE
}

SUPPORTED_CLASSES = [class_type for class_type, _ in MAPPING_TYPE.items()]
