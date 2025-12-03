import logging

import gurobipy as gp
import networkx as nx
from data_schema import Instance, Solution
from gurobipy import GRB



class MiningRoutingSolver:
    def __init__(self, instance: Instance) -> None:
        self.instance = instance
        self.budget = instance.budget
        logging.info("Creating model ...")
        logging.info(
            "Instance has %d locations, %d mines, %d tunnels, and a budget of %.2f",
            len(instance.locations),
            len(instance.mines),
            len(instance.tunnels),
            instance.budget,
        )
        # TODO: Implement me!
        self.model = gp.Model()
        self.graph = self.make_graph()

        self.edges = self.graph.edges(data=True)
        self.vars = {(edge[0], edge[1]): self.model.addVar(vtype=GRB.BINARY) for edge in self.edges}
        self.maintained_tunnels = {frozenset((edge[0], edge[1])): self.model.addVar(vtype=GRB.BINARY) for edge in self.edges}
        self.flows = {}
        self.define_flows()


        for edge in self.edges:
            self.model.addConstr(self.flows[(edge[0], edge[1])] <= self.vars[(edge[0], edge[1])] * edge[2]["thrpt"])


        self.add_directional_constraint()
        self.add_include_central_constraint()
        self.add_flow_conservation_constraint()
        self.add_budget_constraint()
        self.specify_objective()


    def add_flow_conservation_constraint(self):
        for node in self.graph.nodes: 
            if node == self.instance.elevator_location:
                continue
            ore_per_hour = self.get_prod(node)
            in_nodes = self.graph.predecessors(node)
            out_nodes = self.graph.successors(node)
            self.model.addConstr(gp.quicksum(self.flows[(in_node, node)]*self.vars[(in_node, node)] for in_node in in_nodes) + ore_per_hour >= gp.quicksum(self.flows[(node, out_node)]*self.vars[(node, out_node)] for out_node in out_nodes))

        elevator = self.instance.elevator_location
        self.model.addConstr(gp.quicksum(self.flows[elevator, out_node] for out_node in self.graph.predecessors(elevator)) == 0)


    def define_flows(self):
        for edge in self.edges:
            self.flows[(edge[0], edge[1])] = self.model.addVar(vtype=GRB.INTEGER, lb=0, ub=edge[2]["thrpt"])


    def specify_objective(self):
        #self.model.setObjective(gp.quicksum(self.vars[(edge[0], edge[1])] * edge[2]["thrpt"] for edge in self.edges), GRB.MAXIMIZE)
        elevator = self.instance.elevator_location
        self.model.setObjective(gp.quicksum(self.flows[(in_node, elevator)]*self.vars[(in_node, elevator)] for in_node in self.graph.predecessors(elevator)), GRB.MAXIMIZE)



    def add_budget_constraint(self):
        self.model.addConstr(gp.quicksum(self.vars[(edge[0], edge[1])] * edge[2]["cost"] for edge in self.edges) <= self.budget)

    def add_include_central_constraint(self):
        elevator = self.instance.elevator_location
        src_edges = []
        for edge in self.edges:
            if edge[1] == elevator:
                src_edges.append(edge)

        self.model.addConstr(gp.quicksum(self.vars[(edge[0], edge[1])] for edge in src_edges) >= 1)


    def add_directional_constraint(self):
        for t in self.instance.tunnels:
            source, target = t.source, t.target
            s_t = self.vars[(source, target)]
            t_s = self.vars[(target, source)]
            self.model.addConstr(s_t + t_s <= 1) 
            

    def make_graph(self):
        G = nx.DiGraph()
        G.add_nodes_from(self.instance.locations)
        for t in self.instance.tunnels:
            source = t.source
            target = t.target
            G.add_edge(source, target, thrpt=t.throughput_per_hour, cost=t.reinforcement_costs)
            G.add_edge(target, source, thrpt=t.throughput_per_hour, cost=t.reinforcement_costs)

        return G

    def get_prod(self, location):
        mine_troughput = 0
        for mine in self.instance.mines.values():
            if mine.location == location:
                mine_troughput = mine.ore_per_hour
        
        return mine_troughput
    

    def get_selection(self):
        selection = []
        for edge in self.edges:
            util = round(self.vars[(edge[0], edge[1])].X)
            if util == 1:
                selection.append(((edge[0], edge[1]), self.flows[(edge[0], edge[1])].X))
        return selection


    def solve(self) -> Solution:
        """
        Calculate the optimal solution to the problem.
        Returns the "flow" as a list of tuples, each tuple with two entries:
            - The *directed* edge tuple. Both entries in the edge should be ints, representing the ids of locations.
            - The throughput/utilization of the edge, in goods per hour
        """
        # TODO: implement me!
        logging.info("Solving model...")

        self.model.optimize()
        
        if self.model.Status == GRB.OPTIMAL or self.model.SolCount > 0:
            if self.model.Status == GRB.OPTIMAL:
                logging.info("Optimal solution found.")
                logging.info("Objective value: %f", self.model.ObjVal)
            else:
                logging.info("Feasible solution found, but not proven optimal.")
                logging.info("Objective value: %f", self.model.ObjVal)

            selection = self.get_selection()

            return Solution(flow=selection)

        logging.warning("No feasible solution found within the time limit.")
        return None
