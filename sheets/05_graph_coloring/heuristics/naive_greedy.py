import networkx as nx


class GCNaiveGreedy:

    def __init__(self, G: nx.Graph):
        self.graph = self.init_graph(G)

    def init_graph(self, G):

        graph = nx.Graph()
        for node in G.nodes:
            graph.add_node(node, color=1)

        graph.add_edges_from(G.edges)
        return graph


    def solve(self):

        for node in self.graph.nodes:
            i = 0
            color_found = False
            while not color_found:
                i += 1
                skip = False
                for neighbor in self.graph.neighbors(node):
                    if self.graph.nodes[neighbor]["color"] == i:
                        skip = True
                        break
                
                if skip: continue
                color_found = True   
            
            self.graph.nodes[node]["color"] = i

        return max(self.graph.nodes[node]["color"] for node in self.graph.nodes)