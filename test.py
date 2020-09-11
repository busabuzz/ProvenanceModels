import json
from opmwextension import *
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('testdata.json') as data_file:
        data = json.load(data_file)

        adaptiveworkflowtemplates = data["adaptiveWorkflowTemplates"]
        G = nx.Graph()

        plt.subplot(121)

        for awft in adaptiveworkflowtemplates:
            G.add_node(awft["id"])

        for awft in adaptiveworkflowtemplates:
            G.add_edge(awft["id"], awft["predecessor"])

        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

