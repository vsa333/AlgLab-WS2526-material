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

    def max_satur_deg(self, nodes):

        best_node = None
        best_node_deg = 0
        max_sat = 0
        for node in nodes:
            neighbors = self.graph.neighbors(node)
            colors = {}
            for neighbor in neighbors:
                color = self.graph.nodes[neighbor]["color"]
                colors[color] = 1
            
            saturation = len(colors.values())
            if saturation > max_sat:
                best_node = node 
                max_sat = saturation

            if saturation == max_sat:
                if self.graph.degree(node) > best_node_deg:
                    best_node = node
                    best_node_deg = self.graph.degree(node)

        return best_node



    def solve(self):

        unc_nodes = list(self.nodes)
        for i in range(len(self.nodes)):
            nxt_node = self.max_satur_deg(unc_nodes)

            color = self.get_color(nxt_node)
            self.graph.nodes[nxt_node]["color"] = color
            unc_nodes.remove(nxt_node)

        sol = max(self.graph.nodes[node]["color"] for node in self.graph.nodes)
        print("DS - Solution found: ", sol)
        return sol