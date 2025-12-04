#from models.gurobi.ass_grb import ASSGRB
#from models.gurobi.ass_s_grb import ASS_SGRB
#from models.gurobi.rep_grb import REP_GRB
from models.cp_sat.ass_cp import ASSCP
from models.cp_sat.ass_s_cp import ASS_SCP
from models.cp_sat.rep_cp import REP_CP
from models.cp_sat.cp_alldiff import CP_ALLDIFF
from models.cp_sat.cp_neq import CP_NEQ
from models.sat.sat_form_solver import GCSATSolver

import os
from _gclib import GCGraphInstance
from benchmarking import plot_performance_profile as ppp

import pandas as pd
import matplotlib
matplotlib.use("Agg")

""" 
# Beispiel-Daten (klein)
data = pd.DataFrame({
    "instance": ["i1","i1","i1"],
    "strategy": ["A","B","C"],
    "metric":   [1.3, 1.1, 1.2],
})
"""

GRAPH_TYPE = "barabasi_albert"

instances = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]

strategies = ["ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASSCP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF"]

metrics = [11.0, 10.0, 11.0, 10.0, 10.0, 11.0, 11.0, 10.0, 11.0, 10.0, 10.0, 11.0, 12.0, 10.0, 11.0, 10.0, 10.0, 11.0, 11.0, 10.0, 10.0, 10.0, 10.0, 11.0, 10.0, 10.0, 11.0, 11.0, 10.0, 11.0, 10, 10.0, 10.0, 10.0, 10.0, 10.0, 10, 10.0, 10.0, 10.0, 10.0, 10.0, 13, 10.0, 10.0, 10.0, 10.0, 10.0, 10, 10.0, 10.0, 10.0, 10.0, 10.0, 10, 10.0, 10.0, 10.0, 10.0, 10.0, 10, 10.0, 10.0, 10.0, 10.0, 10.0, 10, 10.0, 10.0, 10.0, 10.0, 10.0, 10, 10.0, 10.0, 10.0, 10.0, 10.0, 10, 10.0, 10.0, 10.0, 10.0, 10.0, 10, 10.0, 10.0, 10.0, 10.0, 10.0]


gc = GCGraphInstance()

for i in range(10):
    graph = gc.graphs[f"{GRAPH_TYPE}_graph{i}"]
    """ 
    with open(f"instances/erdos_renyi_graph{name}.col", "w", encoding="utf-8") as file:
        for u, v in graph.edges():
            file.write(f"e {u} {v}\n")
    
    sat = GCSATSolver(graph)
    sol_sat = sat.solve(60)
    instances.append(i)
    strategies.append("GCSATSolver")
    metrics.append(sol_sat)

    instances_lb.append(i)
    strategies_lb.append("GCSATSolver")
    metrics_lb.append(sat.lb)


    ng = ASSGRB(graph)
    sol_ng = ng.solve(60)
    instances.append(name)
    strategies.append("ASS")
    metrics.append(sol_ng)


    ms = ASS_SGRB(graph)
    sol_ms = ms.solve(60)
    instances.append(name)
    strategies.append("ASS_S")
    metrics.append(sol_ms)


    ds = REP_GRB(graph)
    sol_ds = ds.solve(60)
    instances.append(name)
    strategies.append("REP")
    metrics.append(sol_ds)

    ng = ASSCP(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("ASSCP")
    metrics.append(sol_ng)
    
    instances_lb.append(i)
    strategies_lb.append("ASSCP")
    metrics_lb.append(ng.lb)



    ng = ASS_SCP(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("ASS_SCP")
    metrics.append(sol_ng)

    instances_lb.append(i)
    strategies_lb.append("ASS_SCP")
    metrics_lb.append(ng.lb)



    ng = REP_CP(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("REP_CP")
    metrics.append(sol_ng)

    instances_lb.append(i)
    strategies_lb.append("REP_CP")
    metrics_lb.append(ng.lb)



    ng = CP_NEQ(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("CP_NEQ")
    metrics.append(sol_ng)

    instances_lb.append(i)
    strategies_lb.append("CP_NEQ")
    metrics_lb.append(ng.lb)



    ng = CP_ALLDIFF(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("CP_ALLDIFF")
    metrics.append(sol_ng) 

    instances_lb.append(i)
    strategies_lb.append("CP_ALLDIFF")
    metrics_lb.append(ng.lb)

    """

"""
with open(f"all_dataset_{GRAPH_TYPE}_lb.txt", "w", encoding="utf-8") as file:
    file.write(f"[{', '.join(map(str, instances))}]\n")
    file.write(f'''["{'", "'.join(strategies)}"]\n''')
    file.write(f"[{', '.join(map(str, metrics))}]\n")
"""


data = pd.DataFrame({
    "instance": instances,
    "strategy": strategies,
    "metric": metrics,
})


ax = ppp.plot_performance_profile(
    data=data,
    instance_column="instance",
    strategy_column="strategy",
    metric_column="metric",
    direction="max",        # "min" wenn kleiner besser ist
    comparison="relative",  # oder "absolute"
    title=f"Performance Profile Lower Bound (All Models, {GRAPH_TYPE})",
    highlight_best=True,
)

#plt.show()

ax.figure.savefig(f"benchmarking/plots/all_performance_profile_{GRAPH_TYPE}_lb.png", dpi=300, bbox_inches="tight")

