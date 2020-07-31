




class OPMWModel:
    def __init__(self):
        pass


class DataVariable:
    def __init__(self):
        pass


class ParameterVariable:
    def __init__(self):
        pass


class WorkflowExecutionAccount:
    def __init__(self):
        pass


class WorkflowExecutionArtifact:
    def __init__(self):
        pass


class WorkflowExecutionProcess:
    def __init__(self):
        pass


class WorkflowTemplate:
    def __init__(self):
        pass


class WorkflowTemplateArtifact:
    def __init__(self):
        pass


class Adaptation:

    def __init__(self, name, instancetype, version, change, signature, timestamp, predecessor):
        self.name = name
        self.instancetype = instancetype
        self.version = version
        self.change = change
        self.signature = signature
        self.timestamp = timestamp
        self.predecessor = predecessor  # hash of predecessor provenance object


class ExecutionTrace:

    def __init__(self, provenance_hash, instance_id, instance_type, version, data_in, data_out, invocation_sig, execution_sig, timestamp, predecessor):
        self.provenance_hash = provenance_hash  # hashed attributes
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.version = version
        self.data_in = data_in
        self.data_out = data_out
        self.invocation_sig = invocation_sig
        self.execution_sig = execution_sig
        self.timestamp = timestamp
        self.predecessor = predecessor  # hash of predecessor provenance object


if __name__ == '__main__':
    pass

