import networkx as nx
from heuristics.multi_start_greedy import GCMultiStartGreedy


from ortools.sat.python.cp_model import FEASIBLE, OPTIMAL, CpModel, CpSolver

# :)
class CP_ALLDIFF:

    def __init__(self, G: nx.Graph):
        self.graph = G
        self.nodes = self.graph.nodes()
        self.model = CpModel()
        self.solver = CpSolver()
        self.solver.parameters.log_search_progress = True


        ub = GCMultiStartGreedy(self.graph).solve()
        self.z = {node: self.model.new_int_var(1, ub, f"{node}") for node in self.nodes}
        self.z_max = self.model.new_int_var(1, ub, "z_max")

        self.add_neq_constraint()
        self.add_zmax_constraint()
        self.add_clique_constraint()
        self.add_objective()


    def add_clique_constraint(self):
        cliques = nx.find_cliques(self.graph)
        n = len(self.nodes)
        for i, clique in enumerate(cliques):
            if i > n: break
            self.model.add_all_different(self.z[node] for node in clique)

    def add_neq_constraint(self):
        for edge in self.graph.edges():
            self.model.add(self.z[edge[0]] != self.z[edge[1]])

    def add_zmax_constraint(self):
        for node in self.nodes:
            self.model.add(self.z[node] <= self.z_max)

    def add_objective(self):
        self.model.minimize(self.z_max)


    def make_colored_graph(self):

        for node in self.graph.nodes:
            self.graph.nodes[node]["color"] = self.solver.Value(self.z[node])

    def solve(self):

        status = self.solver.solve(self.model)
        self.make_colored_graph()
        return self.solver.ObjectiveValue()
