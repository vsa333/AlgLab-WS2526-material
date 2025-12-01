import networkx as nx
from ortools.sat.python.cp_model import FEASIBLE, OPTIMAL, CpModel, CpSolver
import math


class REP_CP:

    def __init__(self, G: nx.Graph):
        self.graph = G
        self.nodes = list(self.graph.nodes())
        self.model = CpModel()
        self.solver = CpSolver()
        self.solver.parameters.log_search_progress = True

        for i, node in enumerate(self.nodes):
            self.graph.nodes[node]["idx"] = i


        self.x = {}
        for v in self.nodes:
            for w in self.nodes:
                if w in self.graph.neighbors(v):
                    continue
                if self.graph.nodes[w]["idx"] <= self.graph.nodes[v]["idx"]:
                    self.x[(v, w)] = self.model.new_bool_var(f"{v}_{w}")
                else:
                    self.x[(v, w)] = 0

        self.add_one_rep_constraint()
        self.add_consistency_constraint()

        self.add_objective()


    def add_consistency_constraint(self):
        for w in self.nodes:

            closed_neighborhood = list(self.graph.neighbors(w))
            closed_neighborhood.append(w)

            n_cn = [node for node in self.nodes if node not in closed_neighborhood]

            for u in n_cn:
                for v in n_cn:

                    if (u, w) not in self.x or (v, w) not in self.x:
                        continue

                    if not self.graph.has_edge(u, v):
                        continue

                    self.model.add(self.x[(u, w)] + self.x[(v, w)] <= self.x[(w, w)])

    def add_one_rep_constraint(self):
        for v in self.nodes:
            self.model.add(sum(self.x[(v, w)] for w in self.nodes if w not in self.graph.neighbors(v) and (v, w) in self.x) == 1)


    def add_objective(self):
        self.model.minimize(sum(self.x[(w, w)] for w in self.nodes))


    def make_colored_graph(self):
        color = 1
        for w in self.nodes:
            if self.solver.Value(self.x[(w, w)]) == 1:
                self.graph.nodes[w]["color"] = color
                color += 1
        
        for (v, w), x in self.x.items():
            if self.solver.Value(x):
                self.graph.nodes[v]["color"] = self.graph.nodes[w]["color"]


    def solve(self, time_limit: float =  math.inf):

        if time_limit is not None:
            self.solver.parameters.max_time_in_seconds = time_limit

        status = self.solver.solve(self.model)
        self.make_colored_graph()
        return self.solver.ObjectiveValue()






























""" 
class REP_CP:

    def __init__(self, G: nx.Graph):
        self.graph = G
        self.nodes = list(self.graph.nodes())
        self.model = CpModel()
        self.solver = CpSolver()
        self.solver.parameters.log_search_progress = True

        self.x = {(i, j): self.model.new_bool_var(f"{self.nodes[i]}_{self.nodes[j]}") for i in range(len(self.nodes)) for j in range(len(self.nodes)) if j <= i and self.nodes[j] not in self.graph.neighbors(self.nodes[i])}
        print(self.x)
        self.add_one_rep_constraint()
        self.add_consistency_constraint()

        self.add_objective()


    def add_consistency_constraint(self):
        for i in range(len(self.nodes)):
            w = self.nodes[i]
            closed_neighborhood = list(self.graph.neighbors(w))
            closed_neighborhood.append(w)
            for j in range(len(self.nodes)):
                if i > j:
                    continue
                for k in range(len(self.nodes)):
                    u, v = self.nodes[j], self.nodes[k]

                    if i > k:
                        continue

                    if u in closed_neighborhood or v in closed_neighborhood:
                        continue

                    self.model.add(self.x[(j, i)] + self.x[(k, i)] <= self.x[(i, i)])

    def add_one_rep_constraint(self):
        for i in range(len(self.nodes)):
            self.model.add(sum(self.x[(i, j)] for j in range(len(self.nodes)) if j <= i and self.nodes[j] not in self.graph.neighbors(self.nodes[i]) and (i, j) in self.x) == 1)


    def add_objective(self):
        self.model.minimize(sum(self.x[(i, i)] for i in range(len(self.nodes))))


    def solve(self):
        status = self.solver.solve(self.model)

        for i, node in enumerate(self.nodes):
            print(i, node)
        
        return self.solver.ObjectiveValue()
 """