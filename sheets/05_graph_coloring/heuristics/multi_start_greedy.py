import networkx as nx


class GCMultiStartGreedy:

    def __init__(self, G: nx.Graph):
        self.start_graph = self.init_graph(G)
        self.nodes_arr = self.nodes_to_array(self.start_graph.nodes())
        self.best_graph = None
        self.best_cnum = None

    def init_graph(self, G):

        graph = nx.Graph()
        for node in G.nodes:
            graph.add_node(node, color=0)

        graph.add_edges_from(G.edges)
        return graph

    def nodes_to_array(self, nodes):
        arr = []
        for node in nodes:
            arr.append(node)
        return arr

    def solve(self):

        n = len(self.nodes_arr)
        for i in range(n):
            curr_cnum = 0
            graph = self.start_graph.copy()

            for j in range(n):
                idx = (j + i) % n 
                graph.nodes[self.nodes_arr[idx]]["color"] = max(graph.nodes[neighbor]["color"] for neighbor in graph.neighbors(self.nodes_arr[idx]))+1


            curr_cnum = max(graph.nodes[node]["color"] for node in graph.nodes)
            if self.best_cnum is None or curr_cnum < self.best_cnum:
                print("New best solution found: ", curr_cnum)
                self.best_cnum = curr_cnum
                self.best_graph = graph


        return self.best_cnum