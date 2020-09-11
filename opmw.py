
class DataVariable:
    def __init__(self, label, isGeneratedBy, hasDimensionality, template):
        self.label = label
        self.isGeneratedBy = isGeneratedBy
        self.hasDimensionality = hasDimensionality
        self.template = template


class ParameterVariable:
    def __init__(self, label, template):
        self.label = label
        self.template = template


class WorkflowExecutionAccount:
    def __init__(self, status, executedInWorkflowSystem, startTime, endTime, template, label="", executionDiagram=""):
        self.hasStatus = status
        self.executedInWorkflowSystem = executedInWorkflowSystem
        self.hasExecutionDiagram = executionDiagram
        self.hasStartTime = startTime
        self.hasEndTime = endTime
        self.hasLabel = label
        self.correspondsToTemplate = template


class WorkflowExecutionArtifact:
    def __init__(self, hasLocation, wasGeneratedBy, hasSize, hasWorkflowTemplateArtifact, hasLabel=""):
        self.hasLocation = hasLocation
        self.wasGeneratedBy = wasGeneratedBy
        self.hasLabel = hasLabel
        self.hasSize = hasSize
        self.hasWorkflowTemplateArtifact = hasWorkflowTemplateArtifact


class WorkflowExecutionProcess:
    def __init__(self, hasLabel, used, wasControlledBy, hasWorkflowTemplateProcess):
        self.hasLabel = hasLabel
        self.used = used  # WorkflowExecutionArtifact
        self.wasControlledBy = wasControlledBy
        self.hasWorkflowTemplateProcess = hasWorkflowTemplateProcess


class WorkflowTemplate:
    def __init__(self, hasLabel, contributor, modified, hasVersion):
        self.hasLabel = hasLabel
        self.contributor = contributor
        self.modified = modified
        self.hasVersion = hasVersion  # unique identifier


class WorkflowTemplateArtifact:
    """ Data/Parameter variables """
    def __init__(self):
        pass


class WorkflowTemplateProces:
    def __init__(self, template, uses):
        self.template = template
        self.uses = uses  # data variable



