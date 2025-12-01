import networkx as nx

import gurobipy as gp


class REP_GRB:

    def __init__(self, G: nx.Graph):
        self.graph = G
        self.nodes = list(self.graph.nodes())
        self.model = gp.Model()

        for i, node in enumerate(self.nodes):
            self.graph.nodes[node]["idx"] = i


        self.x = {}
        for v in self.nodes:
            for w in self.nodes:
                if w in self.graph.neighbors(v):
                    continue
                if self.graph.nodes[w]["idx"] <= self.graph.nodes[v]["idx"]:
                    self.x[(v, w)] = self.model.addVar(vtype=gp.GRB.BINARY, name=f"{v}_{w}")
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

                    self.model.addConstr(self.x[(u, w)] + self.x[(v, w)] <= self.x[(w, w)])

    def add_one_rep_constraint(self):
        for v in self.nodes:
            self.model.addConstr(gp.quicksum(self.x[(v, w)] for w in self.nodes if w not in self.graph.neighbors(v) and (v, w) in self.x) == 1)


    def add_objective(self):
        self.model.setObjective(gp.quicksum(self.x[(w, w)] for w in self.nodes))



    def make_colored_graph(self):
        color = 1
        for w in self.nodes:
            if self.x[(w, w)].X >= 0.5:
                self.graph.nodes[w]["color"] = color
                color += 1
        
        for (v, w), x in self.x.items():
            if type(x) is int: continue
            if x.X >= 0.5:
                self.graph.nodes[v]["color"] = self.graph.nodes[w]["color"]



    def solve(self, time_limit):
        
        self.model.Params.LogToConsole = 1
        self.model.Params.TimeLimit = time_limit

        status = self.model.optimize()
        self.make_colored_graph()
        return self.model.ObjVal