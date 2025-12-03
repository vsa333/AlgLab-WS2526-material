import networkx as nx

class GCPreprocessor:

    """
    A preprocessor that removes low-degree vertices from the graph.
    This needs to be a class as it maintains state between the preprocessing and postprocessing steps.
    """
    def __init__(self, graph: nx.Graph):
        self.graph = graph  # the original graph
        self.removed_vertices = []
        self.lower_bound = nx.approximation.large_clique_size(graph)

    def preprocess(self) -> nx.Graph:
        """
        Return a preprocessed graph.
        """
        rdc_graph = self.graph.copy()
        removable_vertices = [node for node in self.graph.nodes() if self.graph.degree(node) < self.lower_bound]

        while len(removable_vertices) > 0:
            node = removable_vertices.pop()
            self.removed_vertices.append(node)
            rdc_graph.remove_node(node)
            removable_vertices.append([neighbor for neighbor in self.graph.neighbors(node) if rdc_graph.degree(neighbor) < self.lower_bound and neighbor not in removable_vertices])

        return rdc_graph


    def postprocess(self, sol_G: nx.Graph):
        """
        Convert a solution for the reduced graph back to the original graph.
        As we are also interested in the lower bound, also pass it through.
        """
        pass