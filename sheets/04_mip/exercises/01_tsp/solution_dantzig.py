"""
Implement the Dantzig-Fulkerson-Johnson formulation for the TSP.
"""

import logging
import typing

import gurobipy as gp
import networkx as nx


class GurobiTspSolver:
    """
    IMPLEMENT ME!
    """

    def __init__(self, G: nx.Graph, k: int = 2):
        """
        G is a weighted networkx graph, where the weight of an edge is stored in the
        "weight" attribute. It is strictly positive.
        """
        self.graph = G
        self.edges = G.edges(data=True)
        self.nodes = G.nodes()
        assert (
            G.number_of_edges() == G.number_of_nodes() * (G.number_of_nodes() - 1) / 2
        ), "Invalid graph"
        assert all(
            weight > 0
            for _, _, weight in G.edges.data("weight", default=None)  # type: ignore[attr-defined]
        ), "Invalid graph"
        assert k in {1, 2}, "Invalid k"
        self.k = k
        logging.info("Creating model ...")
        logging.info(
            "Graph has %d nodes and %d edges", G.number_of_nodes(), G.number_of_edges()
        )
        logging.info("Implementing subtour elimination with >= %d", k)
        self._model = gp.Model()
        # TODO: Implement me!

        self._vars = {
            frozenset((u, v)): self._model.addVar(vtype=gp.GRB.BINARY, name=f"edge_{u}_{v}")
            for u, v in G.edges
        }

        self.add_degree_constraints()

        #gleiche anzahl kanten wie knoten (für hamiltonkreis)
        self._model.addConstr(gp.quicksum(self._vars[frozenset(u, v)] for u, v in G.edges) == len(G.nodes))
        self.add_objective()


    def add_objective(self):

        self._model.setObjective(gp.quicksum(edge[2] * self._vars[frozenset((edge[0], edge[1]))] for edge in self.graph.edges(data=True)), gp.GRB.MINIMIZE)


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

        self._model.cbLazy(gp.quicksum(clause) >= 2)

        return len(c)


    def get_selection(self, in_callback):

        if in_callback:
            return [edge for edge in self.edges if self._model.cbGetSolution(self._vars[frozenset((edge[0], edge[1]))])]
        else:
            return [edge for edge in self.edges if self._vars[frozenset((edge[0], edge[1]))].X]


    def get_lower_bound(self) -> float:
        """
        Return the current lower bound.
        """
        # TODO: Implement me!
        return self._model.ObjBound

    def get_solution(self) -> typing.Optional[nx.Graph]:
        """
        Return the current solution as a graph.
        """
        # TODO: Implement me!
        edges = self.get_selection(False)
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
    
    def get_nodes_from_tour(self, tour):
        nodes = []
        for edge in tour:
            nodes.append(edge[0])
        return nodes

    def solve(self, time_limit: float, opt_tol: float = 0.001) -> None:
        """
        Solve the model. After solving the model, the solution, its objective value,
        and the lower bounds should be available via the corresponding methods.
        """
        logging.info("Solving model ...")
        # Set parameters for the solver.
        self._model.Params.LogToConsole = 1
        self._model.Params.TimeLimit = time_limit
        self._model.Params.LazyConstraints = 1
        self._model.Params.MIPGap = (
            opt_tol  # https://www.gurobi.com/documentation/11.0/refman/mipgap.html
        )

        # ...
        # TODO: Implement me!
        def callback(model, where):
            selection = []
            if where == gp.GRB.Callback.MIPSOL:
                
                selection = self.get_selection(True)
                c = self.get_components(self.get_nodes_from_tour(selection), selection)
                
                if (len(c) != 1):
                    self.add_subtour_constraint(self.get_nodes_from_tour(selection), selection)


        self._model.Params.LazyConstraints = 1
        self._model.optimize(callback)