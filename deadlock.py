import networkx as nx

class DeadlockDetector:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_dependency(self, p1, p2):
        self.graph.add_edge(p1, p2)

    def detect_deadlock(self):
        try:
            cycle = nx.find_cycle(self.graph, orientation='original')
            return [node for node, *_ in cycle]
        except nx.NetworkXNoCycle:
            return None
