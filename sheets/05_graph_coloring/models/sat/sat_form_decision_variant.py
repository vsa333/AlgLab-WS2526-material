import networkx as nx
from pysat.solvers import Solver as SATSolver
from threading import Timer
import math


class GCSATDecisionVariant:
    def __init__(self, G: nx.Graph, k: int, time_limit: float = math.inf) -> None:
        self.solver = SATSolver("Gluecard4")

        def interrupt(sig):
            sig.interrupt()

        if time_limit <= math.inf:
            self.timer = Timer(time_limit, interrupt, [self.solver])
            self.timer.start()

        self.graph = G
        self.nodes = self.graph.nodes()
        self.colors = [i+1 for i in range(k)]
        self.k = k
        self.x = {}
        i = 1
        for node in self.nodes:
            for color in self.colors:
                self.x[(node, color)] = i
                i += 1



        self.add_assign_color_constraint()
        self.add_adjacency_constraint()

    def add_assign_color_constraint(self):
        for node in self.nodes:
            self.solver.add_clause(self.x[(node, color)] for color in self.colors)


    def add_adjacency_constraint(self):
        for edge in self.graph.edges():
            for color in self.colors:
                self.solver.add_clause([-self.x[(edge[0], color)], -self.x[(edge[1], color)]])

    def make_colored_graph(self, model):
        if model is None:
            return
        for node in self.nodes:
            for color in self.colors:
                if self.x[(node, color)] in model:
                    self.graph.nodes[node]["color"] = self.x[(node, color)] % self.k+1

    def get_chromatic_number(self, model):
        if model is None:
            return None
        self.make_colored_graph(model)
        return max(self.graph.nodes[node]["color"] for node in self.graph)


    def solve(self):
        model = None
        self.status = self.solver.solve_limited(expect_interrupt=True)
        model = self.solver.get_model()
        return self.get_chromatic_number(model)