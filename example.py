from prov.dot import prov_to_dot
from prov.graph import *
import json


# generates a Prov document object from a python(json) object
def generate_document(input_data):
    document = ProvDocument()  # create prov document

    # declare document namespaces
    document.add_namespace('template', 'http://www.adaptiveworkflowtemplates.org/adaptiveworkflowtemplates/')
    document.add_namespace('adaptation', 'http://www.adaptiveworkflowtemplates.org/adaptations/')
    document.add_namespace('execution', 'http://www.adaptiveworkflowtemplates.org/adaptiveworkflowexecutions/')
    document.add_namespace('inoutdata', 'http://www.adaptiveworkflowtemplates.org/inoutdata/')

    # generate document contents for workflow templates
    for item in input_data["workflows"]:
        document.entity('template:'+str(item["id"]))
        if item["predecessor"] != "":
            # add adaptation function activity and relationships
            document.activity('adaptation:'+str(item["id"]))
            document.wasGeneratedBy('template:'+str(item["id"]), 'adaptation:'+str(item["id"]))
            document.used('adaptation:'+str(item["adaptation_function"]), 'template:'+str(item["predecessor"]))

    # generate document contents for workflow executions, assumes order of executions.
    inout_ids = []
    for item in input_data["executions"]:
        # adds execution entity
        document.entity('execution:' + str(item["id"]))

        # adds input file entities if they are not output of previous executions
        if item["input"] not in inout_ids and item["input"] != "":
            inout_ids.append(item["input"])
            document.entity('inoutdata:'+str(item["input"]))

        # adds output file entities if an execution has output and adds execution relationships
        if item["output"] != "":
            inout_ids.append(item["output"])
            document.entity('inoutdata:' + str(item["output"]))
            document.wasGeneratedBy('inoutdata:' + str(item["output"]), 'execution:' + str(item["id"]))
            if item["input"] != "":
                document.used('execution:' + str(item["id"]), 'inoutdata:' + str(item["input"]))
            if len(input_data["workflows"]) > 0:
                document.wasDerivedFrom('execution:'+str(item["id"]), 'template:'+str(item["template"]))

    return document


# reads a json input file
def read_input():
    with open('templates_input.json') as input_file:
        data_temp = json.load(input_file)
        return data_temp


# writes a Prov document to a serialized format (xml/json)
def serialize_provenance_document(document, output_format):
    document.serialize('graph.xml', format=output_format)


# produces a png image file displaying the graph of the prov document provided
def document_to_png(document):
    dot = prov_to_dot(document)
    dot.write_png('graph_image.png')


if __name__ == '__main__':
    data = read_input()
    document = generate_document(data)
    document_to_png(document)
    serialize_provenance_document(document, 'xml')

