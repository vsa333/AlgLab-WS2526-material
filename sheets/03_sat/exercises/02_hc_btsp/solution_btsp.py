import math
from enum import Enum

import networkx as nx
from _timer import Timer
from solution_hamiltonian import HamiltonianCycleModel


class SearchStrategy(Enum):
    """
    Different search strategies for the solver.
    """

    SEQUENTIAL_UP = 1  # Try smallest possible k first.
    SEQUENTIAL_DOWN = 2  # Try any improvement.
    BINARY_SEARCH = 3  # Try a binary search for the optimal k.

    def __str__(self):
        return self.name.title()

    @staticmethod
    def from_str(s: str):
        return SearchStrategy[s.upper()]


class BottleneckTSPSolver:
    def __init__(self, graph: nx.Graph) -> None:
        """
        Creates a solver for the Bottleneck Traveling Salesman Problem on the given networkx graph.
        You can assume that the input graph is complete, so all nodes are neighbors.
        The distance between two neighboring nodes is a numeric value (int / float), saved as
        an edge data parameter called "weight".
        There are multiple ways to access this data, and networkx also implements
        several algorithms that automatically make use of this value.
        Check the networkx documentation for more information!
        """
        self.graph = graph
        
        # TODO: Implement me!
        self.weights_dict = {frozenset((edge[0], edge[1])): edge[2]["weight"] for edge in self.graph.edges(data=True)}
        self.weights = sorted([edge[2]["weight"] for edge in self.graph.edges(data=True)])


    def lower_bound(self) -> float:
        # TODO: Implement me!
        return

    def get_max_weight(self, cycle):
        return max(self.weights_dict[frozenset((edge[0], edge[1]))] for edge in cycle)


    def optimize_bottleneck(
        self,
        time_limit: float = math.inf,
        search_strategy: SearchStrategy = SearchStrategy.BINARY_SEARCH,
    ) -> list[tuple[int, int]] | None:
        """
        Find the optimal bottleneck tsp tour.
        """

        self.timer = Timer(time_limit)
        # TODO: Implement me!
        
        G = self.graph.copy()

#        best_solution = None
  
        while True:

            split_idx = len(self.weights) // 2
            left_side = [weight for weight in self.weights if weight < self.weights[split_idx]]
            right_side = [weight for weight in self.weights if weight >= self.weights[split_idx]]
            removable_edges = [edge for edge in G.edges(data=True) if edge[2]["weight"] > self.weights[split_idx]]

            G.remove_edges_from(removable_edges)

            hc_solver = HamiltonianCycleModel(G)
            cycle = hc_solver.solve()
            
            if cycle is None:
                G.add_edges_from(removable_edges)
                self.weights = right_side

            else:
                self.weights = left_side

            if len(self.weights) <= 1:
                return cycle










            """
            hc_solver = HamiltonianCycleModel(G)

            cycle = hc_solver.solve()

            if cycle is None:
                return best_solution
            
            best_solution = cycle            
            max_weight = self.get_max_weight(cycle)

            self.weights = [weight for weight in self.weights if weight < max_weight]

            removable_edges = [edge for edge in G.edges(data=True) if edge[2]["weight"] >= max_weight]
            if len(self.weights) < 1:
                return best_solution

            G.remove_edges_from(removable_edges)
            """