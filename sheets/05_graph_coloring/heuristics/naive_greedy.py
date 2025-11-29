import networkx as nx


class GCNaiveGreedy:

    def __init__(self, G: nx.Graph):
        self.graph = self.init_graph(G)

    def init_graph(self, G):

        graph = nx.Graph()
        for node in G.nodes:
            graph.add_node(node, color=0)

        graph.add_edges_from(G.edges)
        return graph


    def solve(self):

        for node in self.graph.nodes:                            
            self.graph.nodes[node]["color"] = max(self.graph.nodes[neighbor]["color"] for neighbor in self.graph.neighbors(node))+1

        sol = max(self.graph.nodes[node]["color"] for node in self.graph.nodes)
        print("Solution found: ", sol)
        return sol