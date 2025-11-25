"""
Implement the Dantzig-Fulkerson-Johnson formulation for the TSP.
"""

import logging
import typing

import gurobipy as gp
import networkx as nx


class GurobiTspRelaxationSolver:
    """
    IMPLEMENT ME!
    """

    def __init__(self, G: nx.Graph, k: int = 2):
        """
        G is a weighted networkx graph, where the weight of an edge is stored in the
        "weight" attribute. It is strictly positive.
        """
        self.graph = G
        self.k = k
        assert (
            G.number_of_edges() == G.number_of_nodes() * (G.number_of_nodes() - 1) / 2
        ), "Invalid graph"
        assert all(
            weight > 0
            for _, _, weight in G.edges.data("weight", default=None)  # type: ignore[attr-defined]
        ), "Invalid graph"
        assert k in {1, 2}, "Invalid k"
        logging.info("Creating model ...")
        logging.info(
            "Graph has %d nodes and %d edges", G.number_of_nodes(), G.number_of_edges()
        )
        logging.info("Implementing subtour elimination with >= %d", k)
        self._model = gp.Model()
        # TODO: Implement me!
        
        self._vars = {
            frozenset((u, v)): self._model.addVar(vtype=gp.GRB.CONTINUOUS, lb=0, ub=1, name=f"edge_{u}_{v}")
            for u, v in G.edges
        }

        self.add_degree_constraints()

        #gleiche anzahl kanten wie knoten (für hamiltonkreis)
        self._model.addConstr(gp.quicksum(self._vars[frozenset(u, v)] for u, v in G.edges) == len(G.nodes))
        self.add_objective()
    
    def add_objective(self):

        self._model.setObjective(gp.quicksum(edge[2] * self._vars[frozenset((edge[0], edge[1]))] for edge in self.graph.edges(data=True)), gp.GRB.MINIMIZE)

    def get_lower_bound(self) -> float:
        """
        Return the current lower bound.
        """
        # TODO: Implement me!
        return self._model.ObjBound


    def get_solution(self) -> typing.Optional[nx.Graph]:
        """
        Return the current solution as a graph.

        The solution should be a networkx Graph were the
        fractional value of the edge is stored in the "x" attribute.
        You do not have to add edges with x=0.

        ```python
        graph = nx.Graph()
        graph.add_edge(0, 1, x=0.5)
        graph.add_edge(1, 2, x=1.0)
        ```
        """
        # TODO: Implement me!
        edges = self.get_selection()
        nodes = self.get_nodes_from_tour(edges)

        graph = nx.Graph
        graph.add_edges_from(edges)
        graph.add_nodes_from(nodes)

        return graph

    def get_objective(self) -> typing.Optional[float]:
        """
        Return the objective value of the last solution.
        """
        # TODO: Implement me!
        return self._model.ObjVal
    
    def add_degree_constraints(self):

        for node in self.graph.nodes():
            self._model.addConstr(gp.quicksum(self._vars[frozenset((node, neighbor))] for neighbor in self.graph.neighbors(node)) == 2, name=f"deg_constr{node}")

    def get_components(self, tour_nodes, tour_edges):
        
        G = nx.Graph()
        G.add_nodes_from(tour_nodes)
        G.add_edges_from(tour_edges)

        c = list(nx.connected_components(G))
        
        return len(c)

    def add_subtour_constraint(self, tour_nodes, tour_edges):

        c = self.get_components(tour_nodes, tour_edges)

        for component_nodes in c:
            clause = []
            for node in component_nodes:
                clause += [self._vars[frozenset((node, neighbor))] for neighbor in self.graph.neighbors(node) if neighbor not in component_nodes]

        self._model.addConstr(gp.quicksum(clause) >= self.k)

        return len(c)

    def get_selection(self):
        return [edge for edge in self.edges if self._vars[frozenset((edge[0], edge[1]))].X >= 0.001]
    
    def get_nodes_from_tour(self, tour):
        nodes = []
        for edge in tour:
            nodes.append(edge[0])
        return nodes


    def solve(self) -> None:
        """
        Solve the model. After solving the model, the solution, its objective value,
        and the lower bounds should be available via the corresponding methods.
        """
        logging.info("Solving model ...")
        # Set parameters for the solver.
        self._model.Params.LogToConsole = 1

        # TODO: Implement me!
        while True:

            self._model.optimize()
            selection = []                
            selection = self.get_selection()
            c = self.get_components(self.get_nodes_from_tour(selection), selection)
            
            if (len(c) != 1):
                self.add_subtour_constraint(self.get_nodes_from_tour(selection), selection)
            else:
                break
