import networkx as nx
from models.sat.sat_form_decision_variant import GCSATDecisionVariant
from heuristics.multi_start_greedy import GCMultiStartGreedy

class GCSATSolver:


    def __init__(self, G: nx.Graph):
        self.graph = G
        self.nodes = self.graph.nodes()
        self.k = GCMultiStartGreedy(self.graph).solve()
        self.colors = [i+1 for i in range(self.k)]


    def solve(self):
  
        while True:

            split_idx = len(self.colors) // 2
            left_side = [color for color in self.colors if color <= self.colors[split_idx-1]]
            right_side = [color for color in self.colors if color > self.colors[split_idx-1]]

            gc_solver = GCSATDecisionVariant(self.graph, self.colors[split_idx-1])
            coloring = gc_solver.solve()
            
            if coloring is None:
                self.colors = right_side
            else:
                self.colors = left_side

            if len(self.colors) <= 1:
                gc_solver = GCSATDecisionVariant(self.graph, self.colors[0])
                coloring = gc_solver.solve()
                self.graph = gc_solver.graph
                return coloring