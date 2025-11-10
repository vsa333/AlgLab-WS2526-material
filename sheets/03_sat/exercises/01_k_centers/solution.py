import bisect
import logging
import math
from typing import Iterable

import networkx as nx
from pysat.solvers import Solver as SATSolver

logging.basicConfig(level=logging.INFO)

# Define the node ID type. It is an integer but this helps to make the code more readable.
NodeId = int


class Distances:
    """
    This class provides a convenient interface to query distances between nodes in a graph.
    All distances are precomputed and stored in a dictionary, making lookups efficient.
    """

    def __init__(self, graph: nx.Graph) -> None:
        self.graph = graph
        self._distances = dict(nx.all_pairs_dijkstra_path_length(self.graph))

    def all_vertices(self) -> Iterable[NodeId]:
        """Returns an iterable of all node IDs in the graph."""
        return self._distances.keys()

    def dist(self, u: NodeId, v: NodeId) -> float:
        """Returns the distance between nodes `u` and `v`."""
        return self._distances[u].get(v, math.inf)

    def max_dist(self, centers: Iterable[NodeId]) -> float:
        """Returns the maximum distance from any node to the closest center."""
        return max(min(self.dist(c, u) for c in centers) for u in self.all_vertices())

    def vertices_in_range(self, u: NodeId, limit: float) -> Iterable[NodeId]:
        """Returns an iterable of nodes within `limit` distance from node `u`."""
        return (v for v, d in self._distances[u].items() if d <= limit)

    def sorted_distances(self) -> list[float]:
        """Returns a sorted list of all pairwise distances in the graph."""
        return sorted(
            dist
            for dist_dict in self._distances.values()
            for dist in dist_dict.values()
        )


class KCenterDecisionVariant:
    def __init__(self, distances: Distances, k: int) -> None:
        self.distances = distances
        self.nodes = self.distances.all_vertices()
        # TODO: Implement me!
        self._vars = {node: i for i, node in enumerate(self.nodes, 1)}
        self.k = k
        self.solver = SATSolver("Gluecard4")

        self.solver.add_atmost([self._vars[node] for node in self.nodes], self.k)

        # Solution model
        self._solution: list[NodeId] | None = None


    def limit_distance(self, limit: float) -> None:
        """Adds constraints to the SAT solver to ensure coverage within the given distance."""
        logging.info("Limiting to distance: %f", limit)
        # TODO: Implement me!
        for node in self.nodes:
            nodes_in_range = self.distances.vertices_in_range(node, limit)
            self.solver.add_clause(nodes_in_range)

    def get_selection(self, model):
        return [node for node in self.nodes if self._vars[node] in model]


    def solve(self) -> list[NodeId] | None:
        """Solves the SAT problem and returns the list of selected nodes, if feasible."""
        # TODO: Implement me!
        self.solver.solve()
        model = self.solver.get_model()
        
        if model is None:
            self._solution = None
            return self._solution

        self._solution = self.get_selection(model)
        return self._solution

    def get_solution(self) -> list[NodeId]:
        """Returns the solution if available; raises an error otherwise."""
        if self._solution is None:
            msg = "No solution available. Ensure `solve` is called first."
            raise ValueError(msg)
        return self._solution




class KCentersSolver:
    def __init__(self, graph: nx.Graph) -> None:
        """
        Creates a solver for the k-centers problem on the given networkx graph.
        The graph may not be complete, and edge weights are used to represent distances.
        """
        self.graph = graph
        # TODO: Implement me!
        
        self.distances = Distances(graph)
        self.nodes = self.distances.all_vertices()

    def solve_heur(self, k: int) -> list[NodeId]:
        """
        Calculate a heuristic solution to the k-centers problem.
        Returns the k selected centers as a list of node IDs.
        """
        # TODO: Implement me!
        centers = []
        for i in range(k):
            if i == 0:
                centers.append(list(self.nodes)[0])
            distance = self.distances.max_dist(centers)
            for u in self.nodes:
                for center in centers:
                    if self.distances.dist(u, center) == distance:
                        centers.append(u)

        return centers


    def solve(self, k: int) -> list[NodeId]:
        """
        Calculate the optimal solution to the k-centers problem for the given k.
        Returns the selected centers as a list of node IDs.
        """
        # Start with a heuristic solution
        possible_values = self.distances.sorted_distances()
        decision_variant = KCenterDecisionVariant(self.distances, k)
        centers = self.solve_heur(k)
        while True:
            obj = self.distances.max_dist(centers)
            possible_values = [value for value in possible_values if value <= obj]
            decision_variant.limit_distance(possible_values[-1])
            result = decision_variant.solve()
            if result is None:
                break
            if result == centers:
                break
            centers = result
            print(result)

        return centers
