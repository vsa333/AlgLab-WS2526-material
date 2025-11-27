import networkx as nx


class GCGraphInstance():


    def __init__(self):
        self._files = [
            "myciel3.col",
            "myciel4.col",
            "myciel5.col",
            "myciel6.col",
            "myciel7.col",
        ]

        self.graphs = {}
        self._read_graphs()


    def _read_graphs(self):

        for i in range(len(self._files)):

            graph = nx.Graph()
            file = open("instances/" + self._files[i])
            j = 0
            for line in file:
                line = line.strip()
                if j < 6:
                    j += 1
                    continue
                node1, node2 = self._read_edge(line)
                graph.add_edge(node1, node2)
            
            string = "myciel" + str(i+3)
            self.graphs[string] = graph.copy()
            file.close()


    def _read_edge(self, string):
        tokens = string.split()

        return int(tokens[1]), int(tokens[2])