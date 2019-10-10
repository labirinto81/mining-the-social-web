import networkx as nx

#Creating the NULL graph
G1 = nx.Graph()

#Adding the edges will automatically add the nodes
G1.add_edges_from([(1,2), (2,3), (3,4)])

#Visulazing using matplotlib
import matplotlib.pyplot as plt
nx.draw(G1, with_labels=True)
plt.show()