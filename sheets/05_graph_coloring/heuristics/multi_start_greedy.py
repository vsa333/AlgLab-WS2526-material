import networkx as nx
from heuristics.naive_greedy import GCNaiveGreedy


class GCMultiStartGreedy:

    def __init__(self, G: nx.Graph):
        self.start_graph = self.init_graph(G)
        self.nodes_arr = list(self.start_graph.nodes())
        self.best_graph = None
        self.best_cnum = None

    def init_graph(self, G):

        graph = nx.Graph()
        for node in G.nodes:
            graph.add_node(node, color=0)

        graph.add_edges_from(G.edges)
        return graph
    
    
    def get_color(self, node, graph):

        i = 1
        while True:
            col_found = True
            
            for neighbor in graph.neighbors(node):
                if graph.nodes[neighbor]["color"] == i:
                    i += 1
                    col_found = False
                    break
            
            if col_found:
                return i

    def solve(self):

        n = len(self.nodes_arr)
        for i in range(n):
            curr_cnum = 0
            graph = self.start_graph.copy()

            ng = GCNaiveGreedy(graph)
            curr_cnum = ng.solve(self.nodes_arr[i])

            if self.best_cnum is None or curr_cnum < self.best_cnum:
                self.best_cnum = curr_cnum
                self.best_graph = ng.graph

        print("MS - Solution found: ", self.best_cnum)
        return self.best_cnum