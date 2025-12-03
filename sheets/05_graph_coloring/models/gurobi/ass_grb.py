import networkx as nx
from heuristics.multi_start_greedy import GCMultiStartGreedy

import gurobipy as gp

class ASSGRB:

    def __init__(self, G: nx.Graph):
        self.graph = G
        self.nodes = self.graph.nodes()
        self.model = gp.Model()

        # self.colors = [i for i in range(max(dict(self.graph.degree()).values())+1)]
        self.colors = [i for i in range(GCMultiStartGreedy(self.graph).solve())]

        self.x = {(node, color): self.model.addVar(vtype=gp.GRB.BINARY, name=f"{node}_{color}") for color in self.colors for node in self.nodes}
        self.y = {color: self.model.addVar(vtype=gp.GRB.BINARY, name=f"{color}") for color in self.colors}

        self.add_assign_color_constraint()
        self.add_coloring_constraint()
        self.add_color_variable_constraint()
        self.add_objective()


    def add_assign_color_constraint(self):
        for node in self.graph.nodes():
            self.model.addConstr(gp.quicksum(self.x[(node, color)] for color in self.colors) == 1)

    def add_coloring_constraint(self):
        for edge in self.graph.edges:
            for color in self.colors:
                self.model.addConstr(self.x[(edge[0], color)] + self.x[(edge[1], color)] <= 1)

    def add_color_variable_constraint(self):
        for node in self.nodes:
            for color in self.colors:
                self.model.addConstr(self.x[(node, color)] <= self.y[color])

    def add_objective(self):
        self.model.setObjective(gp.quicksum(self.y[color] for color in self.colors), gp.GRB.MINIMIZE)

    def make_colored_graph(self):
        g = nx.Graph()
        for node in self.graph.nodes:
            for c in self.colors:
                if self.x[(node, c)].X >= 0.5:
                    g.add_node(node, color=c)
                    break

        g.add_edges_from(self.graph.edges())
        return g

    def solve(self, time_limit):

        #self.model.Params.LogToConsole = 1
        self.model.Params.TimeLimit = time_limit
        #self._model.Params.LazyConstraints = 1
        #self._model.Params.MIPGap = (opt_tol  # https://www.gurobi.com/documentation/11.0/refman/mipgap.html)
        
        self.model.optimize()
        self.graph = self.make_colored_graph()
        self.lb = self.model.ObjBound
        return self.model.ObjVal

