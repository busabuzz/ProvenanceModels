from opmw import *


class AdaptiveWorkflowTemplate(WorkflowTemplate):

    def __init__(self, label, contributor, modified, version, adaptation, predecessor):
        super().__init__(label, contributor, modified, version)
        self.adaptation = adaptation  # computable function
        self.predecessor = predecessor


class AdaptiveWorkflowExecutionAccount(WorkflowExecutionAccount):

    def __init__(self, status, executedInWorkflowSystem, startTime, endTime, template, invokeSignature, executionSignature, data_input, data_output, label="", executionDiagram=""):
        super().__init__(status, executedInWorkflowSystem, startTime, endTime, template, label, executionDiagram)
        self.invokeSignature = invokeSignature
        self.executionSignature = executionSignature
        self.input = data_input
        self.output = data_output


