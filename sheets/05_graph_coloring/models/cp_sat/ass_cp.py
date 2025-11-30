import networkx as nx
from heuristics.multi_start_greedy import GCMultiStartGreedy


from ortools.sat.python.cp_model import FEASIBLE, OPTIMAL, CpModel, CpSolver

# :)
class ASSCP:

    def __init__(self, G: nx.Graph):
        self.graph = G
        self.nodes = self.graph.nodes()
        self.model = CpModel()
        self.solver = CpSolver()
        self.solver.parameters.log_search_progress = True

        # self.colors = [i for i in range(max(dict(self.graph.degree()).values())+1)]
        self.colors = [i for i in range(GCMultiStartGreedy(self.graph).solve())]

        self.x = {(node, color): self.model.new_bool_var(f"{node}_{color}") for color in self.colors for node in self.nodes}
        self.y = {color: self.model.new_bool_var(f"{color}") for color in self.colors}

        self.add_assign_color_constraint()
        self.add_coloring_constraint()
        self.add_color_variable_constraint()
        self.add_objective()


    def add_assign_color_constraint(self):
        for node in self.graph.nodes():
            self.model.add(sum(self.x[(node, color)] for color in self.colors) == 1)

    def add_coloring_constraint(self):
        for edge in self.graph.edges:
            for color in self.colors:
                self.model.add(self.x[(edge[0], color)] + self.x[(edge[1], color)] <= 1)

    def add_color_variable_constraint(self):
        for node in self.nodes:
            for color in self.colors:
                self.model.add(self.x[(node, color)] <= self.y[color])

    def add_objective(self):
        self.model.minimize(sum(self.y[color] for color in self.colors))

    def make_colored_graph(self):
        g = nx.Graph()
        for node in self.graph.nodes:
            for c in self.colors:
                if self.solver.Value(self.x[(node, c)]) == 1:
                    g.add_node(node, color=c)
                    break

        g.add_edges_from(self.graph.edges())
        return g

    def solve(self):

        status = self.solver.solve(self.model)
        G = self.make_colored_graph()
        self.graph = G
        return self.solver.ObjectiveValue()
