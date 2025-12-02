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




instances = []
strategies = []
metrics = []

gc = GCGraphInstance("kneser", gen=0)
gc2 = GCGraphInstance("barabasi", gen=0)
gc3 = GCGraphInstance("erdos", gen=1)



all_graphs = {}
i = 0
for k in gc.graphs.values():
    all_graphs[i] = k
    i += 1

for b in gc2.graphs.values():
    all_graphs[i] = b
    i += 1

for e in gc3.graphs.values():
    all_graphs[i] = e
    i += 1


for name in all_graphs.keys():
    graph = all_graphs[name]

    with open(f"instances/erdos_renyi_graph{name}.col", "w", encoding="utf-8") as file:
        for u, v in graph.edges():
            file.write(f"e {u} {v}\n")

    sat = GCSATSolver(graph)
    sol_sat = sat.solve(60)
    instances.append(name)
    strategies.append("GCSATSolver")
    metrics.append(sol_sat)

    """ 
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
    """    
    """     
    ng = ASSCP(graph)
    sol_ng = ng.solve(60)
    instances.append(name)
    strategies.append("ASSCP")
    metrics.append(sol_ng)
    
    ng = ASS_SCP(graph)
    sol_ng = ng.solve(60)
    instances.append(name)
    strategies.append("ASS_CP")
    metrics.append(sol_ng)

    ng = REP_CP(graph)
    sol_ng = ng.solve(60)
    instances.append(name)
    strategies.append("REP_CP")
    metrics.append(sol_ng)

    ng = CP_NEQ(graph)
    sol_ng = ng.solve(60)
    instances.append(name)
    strategies.append("CP_NEQ")
    metrics.append(sol_ng)

    ng = CP_ALLDIFF(graph)
    sol_ng = ng.solve(60)
    instances.append(name)
    strategies.append("CP_ALLDIFF")
    metrics.append(sol_ng) 
    """



with open("all_1.txt", "w", encoding="utf-8") as file:
    file.write(f"[{', '.join(map(str, instances))}]\n")
    file.write(f"[{', '.join(strategies)}]\n")
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
    direction="min",        # "min" wenn kleiner besser ist
    comparison="relative",  # oder "absolute"
    title="Performance Profile (All Models)",
    highlight_best=True,
)

#plt.show()

ax.figure.savefig("benchmarking/plots/all_performance_profile.png", dpi=300, bbox_inches="tight")

