# Pattern for INSERT query call names
INSERT_PATTERN = "INSERT DATA { GRAPH ?_g_iri { <s> <p> <o> }}"

DEFAULT_MINT_INSTANCE = "https://w3id.org/mint/instance/"

PREFIX_CONTEXT = {
}

PREDICATE_CONTEXT = {
    "@context": {
        "@base": "https://w3id.org/mint/instance/",
        "abbreviation": {
            "@id": "http://qudt.org/schema/qudt/abbreviation"
        },
        "ccut": "https://www.w3id.org/mint/ccut#",
        "description": {
            "@id": "http://purl.org/dc/terms/description"
        },
        "hasAssumption": {
            "@id": "https://w3id.org/mint/modelCatalog#hasAssumption",
            "@container": "@set"
        },
        "hasCAG": {
            "@id": "https://w3id.org/mint/modelCatalog#hasCAG",
            "@type": "@id",
            "@container": "@set"
        },
        "hasComponentLocation": {
            "@id": "https://w3id.org/mint/modelCatalog#hasComponentLocation",
            "@container": "@set"
        },
        "hasConfiguration": {
            "@id": "https://w3id.org/mint/modelCatalog#hasConfiguration",
            "@type": "@id",
            "@container": "@set"
        },
        "hasConstraint": {
            "@id": "https://w3id.org/mint/modelCatalog#hasConstraint",
            "@container": "@set"
        },
        "hasContainer": {
            "@id": "http://ontosoft.org/software#hasContainer",
            "@type": "@id",
            "@container": "@set"
        },
        "hasDataType": {
            "@id": "https://w3id.org/mint/modelCatalog#hasDataType",
            "@container": "@set"
        },
        "hasDataset": {
            "@id": "https://w3id.org/mint/modelCatalog#hasDataset",
            "@type": "@id",
            "@container": "@set"
        },
        "hasDefaultValue": {
            "@id": "https://w3id.org/mint/modelCatalog#hasDefaultValue",
            "@container": "@set"
        },
        "hasDimensionality": {
            "@id": "https://w3id.org/mint/modelCatalog#hasDimensionality",
            "@container": "@set"

        },
        "hasDocumentation": {
            "@id": "http://ontosoft.org/software#hasDocumentation",
            "@container": "@set"
        },
        "hasExecutionCommand": {
            "@id": "http://ontosoft.org/software#hasExecutionCommand",
            "@container": "@set"
        },
        "hasFileStructure": {
            "@id": "https://w3id.org/mint/modelCatalog#hasFileStructure",
            "@type": "@id",
            "@container": "@set"
        },
        "hasFormat": {
            "@id": "https://w3id.org/mint/modelCatalog#hasFormat",
            "@container": "@set"
        },
        "hasGrid": {
            "@id": "https://w3id.org/mint/modelCatalog#hadGrid",
            "@type": "@id",
            "@container": "@set"
        },
        "hasIdentifier": {
            "@id": "http://ontosoft.org/software#hasIdentifier"
        },
        "hasImplementationScriptLocation": {
            "@id": "http://ontosoft.org/software#hasImplementationScriptLocation"
        },
        "hasInput": {
            "@id": "https://w3id.org/mint/modelCatalog#hasInput",
            "@type": "@id",
            "@container": "@set"
        },
        "hasInstallationInstructions": {
            "@id": "http://ontosoft.org/software#hasInstallationInstructions",
            "@container": "@set"
        },
        "hasLongName": {
            "@id": "https://w3id.org/mint/modelCatalog#hasLongName",
            "@container": "@set"
        },
        "hasMaximumAcceptedValue": {
            "@id": "https://w3id.org/mint/modelCatalog#hasMaximumAcceptedValue",
            "@container": "@set"
        },
        "hasMinimumAcceptedValue": {
            "@id": "https://w3id.org/mint/modelCatalog#hasMinimumAcceptedValue",
            "@container": "@set"
        },
        "hasModelCategory": {
            "@id": "https://w3id.org/mint/modelCatalog#hasModelCategory",
            "@container": "@set"
        },
        "hasModule": {
            "@id": "https://w3id.org/mint/modelCatalog#hasModule",
            "@type": "@id"
        },
        "hasOutput": {
            "@id": "https://w3id.org/mint/modelCatalog#hasOutput",
            "@type": "@id",
            "@container": "@set"
        },
        "hasParameter": {
            "@id": "https://w3id.org/mint/modelCatalog#hasParameter",
            "@type": "@id",
            "@container": "@set"
        },
        "hasPart": {
            "@id": "https://w3id.org/mint/modelCatalog#hasPart",
            "@type": "@id",
            "@container": "@set"
        },
        "hasPresentation": {
            "@id": "https://w3id.org/mint/modelCatalog#hasPresentation",
            "@type": "@id",
            "@container": "@set"
        },
        "hasProcess": {
            "@id": "https://w3id.org/mint/modelCatalog#hasProcess",
            "@type": "@id",
            "@container": "@set"
        },
        "hasRelevanceLevel": {
            "@id": "https://w3id.org/mint/modelCatalog#hasRelevanceLevel",
            "@container": "@set"
        },
        "hasShortName": {
            "@id": "https://w3id.org/mint/modelCatalog#hasShortName",
            "@container": "@set"
        },
        "hasSoftwareVersion": {
            "@id": "http://ontosoft.org/software#hasSoftwareVersion",
            "@type": "@id",
            "@container": "@set"
        },
        "hasStandardVariable": {
            "@id": "https://w3id.org/mint/modelCatalog#hasStandardVariable",
            "@type": "@id",
            "@container": "@set"
        },
        "hasSupportScriptLocation": {
            "@id": "https://w3id.org/mint/modelCatalog#hasSupportScriptLocation",
            "@container": "@set"
        },
        "hasTimeInterval": {
            "@id": "https://w3id.org/mint/modelCatalog#hasTimeInterval",
            "@type": "@id",
            "@container": "@set"
        },
        "hasValue": {
            "@id": "https://w3id.org/mint/modelCatalog#hasValue",
            "@container": "@set"
        },
        "hasVersionId": {
            "@id": "http://ontosoft.org/software#hasVersionId",
            "@container": "@set"
        },
        "has_assumption": {
            "@id": "https://w3id.org/mint/modelCatalog#hasAssumption"
        },
        "has_cag": {
            "@id": "https://w3id.org/mint/modelCatalog#hasCAG",
            "@type": "@id",
            "@container": "@set"
        },
        "has_component_location": {
            "@id": "https://w3id.org/mint/modelCatalog#hasComponentLocation"
        },
        "has_configuration": {
            "@id": "https://w3id.org/mint/modelCatalog#hasConfiguration",
            "@type": "@id",
            "@container": "@set"
        },
        "has_constraint": {
            "@id": "https://w3id.org/mint/modelCatalog#hasConstraint"
        },
        "has_container": {
            "@id": "http://ontosoft.org/software#hasContainer",
            "@type": "@id",
            "@container": "@set"
        },
        "has_data_type": {
            "@id": "https://w3id.org/mint/modelCatalog#hasDataType"
        },
        "has_dataset": {
            "@id": "https://w3id.org/mint/modelCatalog#hasDataset",
            "@type": "@id",
            "@container": "@set"
        },
        "has_default_value": {
            "@id": "https://w3id.org/mint/modelCatalog#hasDefaultValue"
        },
        "has_dimensionality": {
            "@id": "https://w3id.org/mint/modelCatalog#hasDimensionality"
        },
        "has_documentation": {
            "@id": "http://ontosoft.org/software#hasDocumentation",
            "@container": "@set"
        },
        "has_execution_command": {
            "@id": "http://ontosoft.org/software#hasExecutionCommand"
        },
        "has_file_structure": {
            "@id": "https://w3id.org/mint/modelCatalog#hasFileStructure",
            "@type": "@id",
            "@container": "@set"
        },
        "has_format": {
            "@id": "https://w3id.org/mint/modelCatalog#hasFormat"
        },
        "has_grid": {
            "@id": "https://w3id.org/mint/modelCatalog#hadGrid",
            "@type": "@id",
            "@container": "@set"
        },
        "has_identifier": {
            "@id": "http://ontosoft.org/software#hasIdentifier"
        },
        "has_implementation_script_location": {
            "@id": "http://ontosoft.org/software#hasImplementationScriptLocation"
        },
        "has_input": {
            "@id": "https://w3id.org/mint/modelCatalog#hasInput",
            "@type": "@id",
            "@container": "@set"
        },
        "has_installation_instructions": {
            "@id": "http://ontosoft.org/software#hasInstallationInstructions"
        },
        "has_long_name": {
            "@id": "https://w3id.org/mint/modelCatalog#hasLongName"
        },
        "has_maximum_accepted_value": {
            "@id": "https://w3id.org/mint/modelCatalog#hasMaximumAcceptedValue"
        },
        "has_minimum_accepted_value": {
            "@id": "https://w3id.org/mint/modelCatalog#hasMinimumAcceptedValue"
        },
        "has_model_category": {
            "@id": "https://w3id.org/mint/modelCatalog#hasModelCategory"
        },
        "has_module": {
            "@id": "https://w3id.org/mint/modelCatalog#hasModule",
            "@type": "@id",
            "@container": "@set"
        },
        "has_output": {
            "@id": "https://w3id.org/mint/modelCatalog#hasOutput",
            "@type": "@id",
            "@container": "@set"
        },
        "has_parameter": {
            "@id": "https://w3id.org/mint/modelCatalog#hasParameter",
            "@type": "@id",
            "@container": "@set"
        },
        "has_part": {
            "@id": "https://w3id.org/mint/modelCatalog#hasPart",
            "@type": "@id",
            "@container": "@set"
        },
        "has_presentation": {
            "@id": "https://w3id.org/mint/modelCatalog#hasPresentation",
            "@type": "@id",
            "@container": "@set"
        },
        "has_process": {
            "@id": "https://w3id.org/mint/modelCatalog#hasProcess",
            "@type": "@id",
            "@container": "@set"
        },
        "has_relevance_level": {
            "@id": "https://w3id.org/mint/modelCatalog#hasRelevanceLevel"
        },
        "has_short_name": {
            "@id": "https://w3id.org/mint/modelCatalog#hasShortName"
        },
        "has_software_version": {
            "@id": "http://ontosoft.org/software#hasSoftwareVersion",
            "@type": "@id",
            "@container": "@set"
        },
        "has_standard_variable": {
            "@id": "https://w3id.org/mint/modelCatalog#hasStandardVariable",
            "@type": "@id",
            "@container": "@set"
        },
        "has_support_script_location": {
            "@id": "https://w3id.org/mint/modelCatalog#hasSupportScriptLocation"
        },
        "has_time_interval": {
            "@id": "https://w3id.org/mint/modelCatalog#hasTimeInterval",
            "@type": "@id",
            "@container": "@set"
        },
        "has_value": {
            "@id": "https://w3id.org/mint/modelCatalog#hasValue"
        },
        "has_version_id": {
            "@id": "http://ontosoft.org/software#hasVersionId"
        },
        "id": "@id",
        "influences": {
            "@id": "https://w3id.org/mint/modelCatalog#influences",
            "@type": "@id",
            "@container": "@set"
        },
        "label": {
            "@id": "http://www.w3.org/2000/01/rdf-schema#label"
        },
        "type": "@type",
        "usesUnit": {
            "@id": "https://w3id.org/mint/modelCatalog#usesUnit",
            "@type": "@id",
            "@container": "@set"
        },
        "uses_unit": {
            "@id": "https://w3id.org/mint/modelCatalog#usesUnit",
            "@type": "@id",
            "@container": "@set"
        }
    },
    "@type": "https://w3id.org/mint/modelCatalog#ModelConfiguration"
}


def merge_two_dicts(x, y):
    z = x.copy()  # start with x's keys and values
    z.update(y)  # modifies z with y's keys and values & returns None
    return z


MINT_CONTEXT = merge_two_dicts(PREFIX_CONTEXT, PREDICATE_CONTEXT)

# todo: support unit

MODELCONFIGURTION_TYPE = "https://w3id.org/mint/modelCatalog#ModelConfiguration"
CAG_TYPE = "https://w3id.org/mint/modelCatalog#CAG"
CONCEPT_TYPE = "https://w3id.org/mint/modelCatalog#CONCEPT"
DATASTRUCTUREDEFINITION_TYPE = "https://w3id.org/mint/modelCatalog#DataStructureDefinition"
DATASET_TYPE = "https://w3id.org/mint/modelCatalog#Dataset"
DATASETSPECIFICATION_TYPE = "https://w3id.org/mint/modelCatalog#DatasetSpecification"
EMPIRICALMODEL_TYPE = "https://w3id.org/mint/modelCatalog#EmpiricalModel"
GRID_TYPE = "https://w3id.org/mint/modelCatalog#Grid"
GSNVARIABLE_TYPE = "https://w3id.org/mint/modelCatalog#GSNVariable"
HYBRIDMODEL_TYPE = "https://w3id.org/mint/modelCatalog#HybridModel"
ICASAVARIABLE_TYPE = "https://w3id.org/mint/modelCatalog#ICASAVariable"
MODEL_TYPE = "https://w3id.org/mint/modelCatalog#Model"
MODELCONFIGURATION_TYPE = "https://w3id.org/mint/modelCatalog#ModelConfiguration"
MODELVERSION_TYPE = "https://w3id.org/mint/modelCatalog#ModelVersion"
MODULE_TYPE = "https://w3id.org/mint/modelCatalog#Module"
PARAMETER_TYPE = "https://w3id.org/mint/modelCatalog#Parameter"
PROCESS_TYPE = "https://w3id.org/mint/modelCatalog#Process"
STANDARDVARIABLE_TYPE = "https://w3id.org/mint/modelCatalog#StandardVariable"
THEORYBASEDMODEL_TYPE = "https://w3id.org/mint/modelCatalog#TheoryBasedModel"
TIMEINTERVAL_TYPE = "https://w3id.org/mint/modelCatalog#TimeInterval"
UNIT_TYPE = "https://w3id.org/mint/modelCatalog#Unit"
VARIABLE_TYPE = "https://w3id.org/mint/modelCatalog#Variable"
VARIABLE_PRESENTATION_TYPE = "https://w3id.org/mint/modelCatalog#VariablePresentation"


HAS_PARAMETER = "https://w3id.org/mint/modelCatalog#hasParameter"
HAS_INPUT = "https://w3id.org/mint/modelCatalog#hasInput"
HAS_OUTPUT = "https://w3id.org/mint/modelCatalog#hasOutput"
HAS_PRESENTATION = "https://w3id.org/mint/modelCatalog#hasPresentation"


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
