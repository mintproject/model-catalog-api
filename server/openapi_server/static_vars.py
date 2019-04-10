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
PREDICATE_CONTEXT = {'hasFileStructure': 'https://w3id.org/mint/modelCatalog#hasFileStructure',
                     'hasConfiguration': 'https://w3id.org/mint/modelCatalog#hasConfiguration',
                     'hasSupportScriptLocation': 'https://w3id.org/mint/modelCatalog#hasSupportScriptLocation',
                     'hasIdentifier': 'http://ontosoft.org/software#hasIdentifier',
                     'hasVersionId': 'http://ontosoft.org/software#hasVersionId',
                     'hadGrid': 'https://w3id.org/mint/modelCatalog#hadGrid',
                     'hasDataType': 'https://w3id.org/mint/modelCatalog#hasDataType',
                     'hasProcess': 'https://w3id.org/mint/modelCatalog#hasProcess',
                     'hasContainer': 'http://ontosoft.org/software#hasContainer',
                     'hasImplementationScriptLocation': 'http://ontosoft.org/software#hasImplementationScriptLocation',
                     'hasInstallationInstructions': 'http://ontosoft.org/software#hasInstallationInstructions',
                     'hasPresentation': 'https://w3id.org/mint/modelCatalog#hasPresentation',
                     'hasDefaultValue': 'https://w3id.org/mint/modelCatalog#hasDefaultValue',
                     'hasConstraint': 'https://w3id.org/mint/modelCatalog#hasConstraint',
                     'hasModule': 'https://w3id.org/mint/modelCatalog#hasModule',
                     'hasDocumentation': 'http://ontosoft.org/software#hasDocumentation',
                     'hasCag': 'https://w3id.org/mint/modelCatalog#hasCAG',
                     'hasStandardVariable': 'https://w3id.org/mint/modelCatalog#hasStandardVariable',
                     'hasShortName': 'https://w3id.org/mint/modelCatalog#hasShortName',
                     'hasParameter': 'https://w3id.org/mint/modelCatalog#hasParameter',
                     'influences': 'https://w3id.org/mint/modelCatalog#influences',
                     'hasRelevanceLevel': 'https://w3id.org/mint/modelCatalog#hasRelevanceLevel',
                     'hasAssumption': 'https://w3id.org/mint/modelCatalog#hasAssumption',
                     'hasMaximumAcceptedValue': 'https://w3id.org/mint/modelCatalog#hasMaximumAcceptedValue',
                     'hasDimensionality': 'https://w3id.org/mint/modelCatalog#hasDimensionality',
                     'hasPart': 'https://w3id.org/mint/modelCatalog#hasPart',
                     'hasValue': 'https://w3id.org/mint/modelCatalog#hasValue',
                     'hasInput': 'https://w3id.org/mint/modelCatalog#hasInput',
                     'hasLongName': 'https://w3id.org/mint/modelCatalog#hasLongName',
                     'hasOutput': 'https://w3id.org/mint/modelCatalog#hasOutput',
                     'usesUnit': 'https://w3id.org/mint/modelCatalog#usesUnit',
                     'hasDataset': 'https://w3id.org/mint/modelCatalog#hasDataset',
                     'description': 'http://purl.org/dc/terms/description',
                     'hasTimeInterval': 'https://w3id.org/mint/modelCatalog#hasTimeInterval',
                     'hasFormat': 'https://w3id.org/mint/modelCatalog#hasFormat',
                     'hasExecutionCommand': 'http://ontosoft.org/software#hasExecutionCommand',
                     'hasMinimumAcceptedValue': 'https://w3id.org/mint/modelCatalog#hasMinimumAcceptedValue',
                     'hasModelCategory': 'https://w3id.org/mint/modelCatalog#hasModelCategory',
                     'hasSoftwareVersion': 'http://ontosoft.org/software#hasSoftwareVersion',
                     'hasComponentLocation': 'https://w3id.org/mint/modelCatalog#hasComponentLocation',
                     'abbreviation': 'http://qudt.org/schema/qudt/abbreviation'}

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
