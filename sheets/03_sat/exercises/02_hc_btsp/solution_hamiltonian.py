import itertools

import networkx as nx
from pysat.solvers import Solver as SATSolver


class HamiltonianCycleModel:
    def __init__(self, graph: nx.Graph) -> None:
        self.graph = graph
        self.solver = SATSolver("Minicard")
        self.assumptions = []
        self.edges = self.graph.edges()
        # TODO: Implement me!
        self.vars = {edge: i for i, edge in enumerate(self.edges)}

        self.add_degree_constraints()

    def add_degree_constraints(self):
        for node in self.graph.nodes():
            self.solver.add_atmost([self.vars[(node, neighbor)] for neighbor in self.graph.neighbors(node)], 2)
            self.solver.add_atmost([-self.vars[(node, neighbor)] for neighbor in self.graph.neighbors(node)], 2)

    def solve(self) -> list[tuple[int, int]] | None:
        """
        Solves the Hamiltonian Cycle Problem. If a HC is found,
        its edges are returned as a list.
        If the graph has no HC, 'None' is returned.
        """
        # TODO: Implement me!
