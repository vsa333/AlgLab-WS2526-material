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
        self.vars = {frozenset((edge[0], edge[1])): i for i, edge in enumerate(self.edges, 1)}

        self.add_degree_constraints()

    def add_degree_constraints(self):

        for node in self.graph.nodes():
            self.solver.add_atmost([self.vars[frozenset((node, neighbor))] for neighbor in self.graph.neighbors(node)], 2)
            negative_vars = [-self.vars[frozenset((node, neighbor))] for neighbor in self.graph.neighbors(node)]
            self.solver.add_atmost(negative_vars, len(negative_vars)-2)

    def add_subtour_constraint(self, tour_nodes, tour_edges):

        G = nx.Graph()
        G.add_nodes_from(tour_nodes)
        G.add_edges_from(tour_edges)

        c = list(nx.connected_components(G))
        
        if len(c) == 1:
            return 1

        for component_nodes in c:
            clause = []
            for node in component_nodes:
                clause += [self.vars[frozenset((node, neighbor))] for neighbor in self.graph.neighbors(node) if neighbor not in component_nodes]
                #print([self.vars[frozenset((node, neighbor))] for neighbor in self.graph.neighbors(node) if neighbor not in component_nodes])
            #print(clause)
            self.solver.add_clause(clause)


        return len(c)
    
    
    def get_nodes_from_tour(self, tour):
        nodes = []
        for edge in tour:
            nodes.append(edge[0])
        return nodes

    def get_selection(self, model):
        return [edge for edge in self.edges if self.vars[frozenset((edge[0], edge[1]))] in model]

    def solve(self) -> list[tuple[int, int]] | None:
        """
        Solves the Hamiltonian Cycle Problem. If a HC is found,
        its edges are returned as a list.
        If the graph has no HC, 'None' is returned.
        """
        # TODO: Implement me!
        selection = []
        c = 2
        while True:

            if c == 1 and len(selection) == len(self.graph.nodes()):
                return selection
            
            c = self.add_subtour_constraint(self.get_nodes_from_tour(selection), selection)
            
            if c == 1: continue
            
            self.solver.solve()
            model = self.solver.get_model()
            
            if model is None:
                return None

            selection = self.get_selection(model)
            #print(selection)
            #print(selection)
