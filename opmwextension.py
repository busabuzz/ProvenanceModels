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