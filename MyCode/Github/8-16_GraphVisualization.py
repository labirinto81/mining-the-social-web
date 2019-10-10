import os
import json
import networkx as nx
from IPython.display import IFrame
from IPython.core.display import display
from networkx.readwrite import  json_graph

g = nx.DiGraph()

print("Stats on the full graph")
print(nx.info(g))

mtsw_users = [n for n in g if g.node[n]['type'] == 'users']
h = g.subgraph(mtsw_users)

print("Stats on the extracted graph")
print(nx.info(h))

d = json_graph.node_link_data(h)
json.dump(d, open('force.json','w'))

viz_file = 'force.html'

display(IFrame(viz_file,'100%','500px'))
