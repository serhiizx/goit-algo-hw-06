import matplotlib.pyplot as plt
import networkx as nx
from graph_data import create_graph

G = create_graph()

plt.figure(figsize=(14, 10))

pos = nx.spring_layout(G, seed=42, k=3, iterations=10)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', 
        node_size=3000, font_weight='bold', font_size=9)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)
plt.tight_layout()
plt.show()
