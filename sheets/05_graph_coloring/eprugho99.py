# from models.gurobi.ass_grb import ASSGRB
# from models.gurobi.ass_s_grb import ASS_SGRB
# from models.gurobi.rep_grb import REP_GRB
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




instances = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]






strategies = ["ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB", "ASS_GRB", "ASS_S_GRB", "REP_GRB"]





metrics = [9.00000000000091, 9.00000000000091, 9.00000000000091, 10.0, 10.0, 10.0, 9.000000000000021, 9.000000000000021, 9.000000000000021, 10.0, 10.0, 10.0, 9.000000000000014, 9.000000000000014, 9.000000000000014, 10.0, 10.0, 10.0, 9.000000000000004, 9.000000000000004, 9.000000000000004, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 9.000000000000009, 9.000000000000009, 9.000000000000009]






all_graphs = GCGraphInstance()
for i in range(10):
    graph = all_graphs.graphs[f"barabasi_albert_graph{i}"]
    """ 
    with open(f"instances/erdos_renyi_graph{name}.col", "w", encoding="utf-8") as file:
        for u, v in graph.edges():
            file.write(f"e {u} {v}\n")
    """

    sat = GCSATSolver(graph)
    sol_sat = sat.solve(60)
    instances.append(i)
    strategies.append("GCSATSolver")
    metrics.append(sat.lb)

    """
    ng = ASSGRB(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("ASS_GRB")
    metrics.append(ng.lb)


    ms = ASS_SGRB(graph)
    sol_ms = ms.solve(60)
    instances.append(i)
    strategies.append("ASS_SGRB")
    metrics.append(ms.lb)


    ds = REP_GRB(graph)
    sol_ds = ds.solve(60)
    instances.append(i)
    strategies.append("REP_GRB")
    metrics.append(ds.lb)
    """
    
    ng = ASSCP(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("ASS_CP")
    metrics.append(ng.lb)
    
    ng = ASS_SCP(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("ASS_SCP")
    metrics.append(ng.lb)

    ng = REP_CP(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("REP_CP")
    metrics.append(ng.lb)

    ng = CP_NEQ(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("CP_NEQ")
    metrics.append(ng.lb)

    ng = CP_ALLDIFF(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("CP_ALLDIFF")
    metrics.append(ng.lb) 

with open("all_dataset_barabasi_albert_lb.txt", "w", encoding="utf-8") as file:
    file.write(f"[{', '.join(map(str, instances))}]\n")
    file.write(f'''["{'", "'.join(strategies)}"]\n''')
    file.write(f"[{', '.join(map(str, metrics))}]\n")


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
    title="Performance Profile Lower Bound (All Models)",
    highlight_best=True,
)

#plt.show()

ax.figure.savefig("benchmarking/plots/all_performance_barabasi_albert_lb_test.png", dpi=300, bbox_inches="tight")

