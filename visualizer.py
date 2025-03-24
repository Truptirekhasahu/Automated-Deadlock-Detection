import matplotlib.pyplot as plt
import networkx as nx

def show_graph(graph):
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", edge_color="black", node_size=2000, font_size=10)
    plt.title("Process Dependency Graph")
    plt.show()
