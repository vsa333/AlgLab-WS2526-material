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


    def get_color(self, node):


        i = 1
        while True:
            col_found = True
            
            for neighbor in self.graph.neighbors(node):
                if self.graph.nodes[neighbor]["color"] == i:
                    i += 1
                    col_found = False
                    break
            
            if col_found:
                return i
            


    def solve(self):

        for node in self.graph.nodes:
            color = self.get_color(node)
            self.graph.nodes[node]["color"] = color

        sol = max(self.graph.nodes[node]["color"] for node in self.graph.nodes)
        print("Solution found: ", sol)
        return sol