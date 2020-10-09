from prov.dot import prov_to_dot
from prov.graph import *


d1 = ProvDocument()

d1.add_namespace('execution', 'http://www.adaptiveworkflowtemplates.org/adaptiveworkflowexecutions/')
d1.add_namespace('adaptation', 'http://www.adaptiveworkflowtemplates.org/adaptations/')
d1.add_namespace('inoutdata', 'http://www.adaptiveworkflowtemplates.org/inoutdata/')

d1.entity('inoutdata:1')
d1.entity('inoutdata:2')
d1.entity('inoutdata:3')
d1.entity('inoutdata:4')
d1.entity('inoutdata:5')
d1.entity('inoutdata:6')
d1.entity('inoutdata:7')

d1.entity('execution:1')
d1.entity('execution:2')
d1.entity('execution:3')
d1.entity('execution:4')
d1.entity('execution:5')

d1.wasGeneratedBy('inoutdata:2', 'execution:1')
d1.wasGeneratedBy('inoutdata:3', 'execution:2')
d1.wasGeneratedBy('inoutdata:4', 'execution:3')
d1.wasGeneratedBy('inoutdata:5', 'execution:4')
d1.wasGeneratedBy('inoutdata:7', 'execution:5')

d1.used('execution:1', 'inoutdata:1')
d1.used('execution:2', 'inoutdata:2')
d1.used('execution:3', 'inoutdata:3')
d1.used('execution:4', 'inoutdata:3')
d1.used('execution:5', 'inoutdata:6')

dot = prov_to_dot(d1)
dot.write_png('executions.png')


