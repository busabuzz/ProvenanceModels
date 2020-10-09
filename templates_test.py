from prov.dot import prov_to_dot
from prov.graph import *


d1 = ProvDocument()

d1.add_namespace('template', 'http://www.adaptiveworkflowtemplates.org/adaptiveworkflowtemplates/')
d1.add_namespace('adaptation', 'http://www.adaptiveworkflowtemplates.org/adaptations/')

d1.entity('template:1')
d1.entity('template:2')
d1.entity('template:3')

d1.activity('adaptation:1')
d1.activity('adaptation:2')

d1.used('adaptation:1', 'template:1')
d1.used('adaptation:2', 'template:2')

d1.wasGeneratedBy('template:2', 'adaptation:1')
d1.wasGeneratedBy('template:3', 'adaptation:2')

dot = prov_to_dot(d1)
dot.write_png('templates.png')
