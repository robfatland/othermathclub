import networkx as nx
import matplotlib.pyplot as plt

# Create a dodecahedron graph
G = nx.dodecahedral_graph()

# Create a figure with a larger size for better visibility
plt.figure(figsize=(12, 10))

# Draw the graph with a nice layout
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

# Draw the graph with customized appearance
nx.draw(G, pos, 
        node_color='lightblue',
        node_size=500,
        edge_color='gray',
        width=2,
        with_labels=True,
        font_size=10,
        font_weight='bold')

plt.title("Dodecahedron Graph (20 vertices, 12 faces)", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

print("Dodecahedron graph properties:")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Is planar: {nx.is_planar(G)}")

plt.show()
