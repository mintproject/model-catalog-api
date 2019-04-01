
# Pattern for INSERT query call names
INSERT_PATTERN = "INSERT DATA { GRAPH ?_g_iri { <s> <p> <o> }}"

DEFAULT_MINT_INSTANCE = "https://w3id.org/instance/mint/"

MINT_CONTEXT = {
        "qudt": "http://qudt.org/schema/qudt",
        "owl": "http://www.w3.org/2002/07/owl",
        "xsd": "http://www.w3.org/2001/XMLSchema",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns",
        "purl": "http://purl.org/dc/terms/",
        "mc": "https://w3id.org/mint/modelCatalog#",
        "wingsexport": "https://w3id.org/wings/export/",
        "label": "rdf:label",
        "description": "purl:description",
        "cag": "mc:hasCAG",
        "inputs": "mc:hasInput",
        "outputs": "mc:hasOutput",
        "process": "mc:hasProcess",
        "intervaltime": "mc:hasTimeInterval",
        "implementationScriptLocation": "mc:hasImplementationScriptLocation",
        "container": "mc:hasContainer",
        "constrainT": "mc:hasConstraint",
        "parameters": "mc:hasParameter",
        "componentLocation": "mc:hasComponentLocation"
}


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


MAPPING_TYPE = {
    "inputs": DATASET_TYPE,
    "outputs": DATASET_TYPE,
    "process": PROCESS_TYPE,
    "cag": CAG_TYPE,
    "interval_time": TIMEINTERVAL_TYPE,
    "parameters": PARAMETER_TYPE
}

SUPPORTED_CLASSES = ["inputs", "outputs", "process", "cag", "interval_time", "parameters", "relations", "presentations"]

