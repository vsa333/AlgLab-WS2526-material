import networkx as nx

class GCPreprocessor:

    """
    A preprocessor that removes low-degree vertices from the graph.
    This needs to be a class as it maintains state between the preprocessing and postprocessing steps.
    """
    def __init__(self, graph: nx.Graph):
        self.graph = self.init_graph(graph)  # the original graph
        self.removed_vertices = []
        self.lower_bound = nx.approximation.large_clique_size(graph)
        #print(f"lower bound: {self.lower_bound}")
        #print([node for node in self.graph.nodes() if self.graph.degree(node) == 1])

    def init_graph(self, G):

        graph = nx.Graph()
        for node in G.nodes:
            graph.add_node(node, color=0)

        graph.add_edges_from(G.edges)
        return graph


    def preprocess(self) -> nx.Graph:
        """
        Return a preprocessed graph.
        """
        rdc_graph = self.graph.copy()
        removable_vertices = [node for node in rdc_graph.nodes() if rdc_graph.degree(node) < self.lower_bound]

        while len(removable_vertices) > 0:
            node = removable_vertices.pop()
            self.removed_vertices.append(node)
            neighbors = rdc_graph.neighbors(node)
            rdc_graph.remove_node(node)
            removable_vertices += [neighbor for neighbor in neighbors if rdc_graph.degree(neighbor) < self.lower_bound and neighbor not in removable_vertices]

        return rdc_graph


    def postprocess(self, sol_G: nx.Graph, cnum):


        for node in sol_G:
            self.graph.nodes[node]["color"] = sol_G.nodes[node]["color"]
        
        n = len(self.removed_vertices)        
        for i in range(1, n+1):
            node = self.removed_vertices[n-i]

            used_colors = {}
            for neighbor in self.graph.neighbors(node):
                used_colors[neighbor] = self.graph.nodes[neighbor]["color"]

            for j in range(1, cnum+1):
                if j not in used_colors.values():
                    self.graph.nodes[node]["color"] = i
                    break
            
        return self.graph