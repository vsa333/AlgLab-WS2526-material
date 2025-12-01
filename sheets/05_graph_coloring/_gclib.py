import networkx as nx
import pathlib
import os

class GCGraphInstance():


    def __init__(self, type = "", gen = None):
        
        self.graphs = {}

        if gen is not None:

            match type:
                case "barabasi":
                    for i in range(gen):
                        graph = nx.barabasi_albert_graph(i+50, 5)
                        self.graphs[i] = graph
                
                case "kneser":
                    for i in range(gen):
                        graph = nx.kneser_graph(i+7, 2+i)
                        self.graphs[i] = graph

                case "erdos":
                    for i in range(gen):
                        graph = nx.erdos_renyi_graph(i+50, 0.5)
                        self.graphs[i] = graph

                case "cycle":
                    for i in range(gen):
                        graph = nx.cycle_graph(i+100)
                        self.graphs[i] = graph

                case "wheel":
                    for i in range(gen):
                        graph = nx.wheel_graph(i+100)
                        self.graphs[i] = graph
             
        else:
            self._files = []
            for file in os.listdir("instances/"):
                self._files.append(file)
            self._read_graphs()


    def _read_graphs(self):

        for i in range(len(self._files)):

            graph = nx.Graph()
            file = open("instances/" + self._files[i])

            for line in file:
                line = line.strip()
                if line[0] != 'e':
                    continue

                node1, node2 = self._read_edge(line)
                graph.add_edge(node1, node2)
            
            string = pathlib.Path(self._files[i]).stem
            self.graphs[string] = graph.copy()
            file.close()


    def _read_edge(self, string):
        tokens = string.split()

        return int(tokens[1]), int(tokens[2])