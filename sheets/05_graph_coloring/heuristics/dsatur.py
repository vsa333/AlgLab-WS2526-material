import networkx as nx


class GCDsatur:

    def __init__(self, G: nx.Graph):
        self.graph = self.init_graph(G)
        self.nodes = self.graph.nodes()

    def init_graph(self, G):

        graph = nx.Graph()
        for node in G.nodes:
            graph.add_node(node, color=0)

        graph.add_edges_from(G.edges)

        return graph



    def max_satur_degree(self, nodes):



    def solve(self):

        unc_nodes = list(self.nodes)
        for i in range(len(self.nodes)):
            nxt_node = self.max_satur_deg(unc_nodes)

            color = min(self.graph.nodes[neighbor]["color"] for neighbor in self.graph.neighbors(nxt_node))-1
            if color < 1:
                color = max(self.graph.nodes[neighbor]["color"] for neighbor in self.graph.neighbors(nxt_node))+1

            self.graph.nodes[nxt_node]["color"] = color
            unc_nodes.remove(nxt_node)

        sol = max(self.graph.nodes[node]["color"] for node in self.graph.nodes)
        print("Solution found: ", sol)
        return sol