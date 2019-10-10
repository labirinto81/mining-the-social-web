import networkx as nx

#Create a direcrted graph
g = nx.DiGraph()

#Add an edge to the directed graph from X to Y
g.add_edge('X','Y')

#Print some statistics about the graph
print(nx.info(g))

#Get the nodes and edges from the graph
print("Nodes:", g.nodes())
print("Edges:", g.edges())
print()

#Get node properties

print("X props:", g.node['X'])
print("Y props:", g.node['Y'])

#Get Edge properties
print("X=>Y props:", g['X']['Y'])
print()

#Update a node property
g.node['X'].update({'prop1' : 'value1'})
print("X props: " , g.node['X'])
print()

#Update an edge property
g['X']['Y'].update({'label' : 'label1'})
print("X=> props:", g['X']['Y'])