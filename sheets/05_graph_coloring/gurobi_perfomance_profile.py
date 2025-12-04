from models.gurobi.ass_grb import ASSGRB
from models.gurobi.ass_s_grb import ASS_SGRB
from models.gurobi.rep_grb import REP_GRB


from _gclib import GCGraphInstance
from benchmarking import plot_performance_profile as ppp

import pandas as pd
import matplotlib
matplotlib.use("Agg")

GRAPH_TYPE = "barabasi_albert"


instances = []
strategies = []
metrics = []

instances_lb = []
strategies_lb = []
metrics_lb = []

gc = GCGraphInstance()


for i in range(10):
    graph = gc.graphs[f"{GRAPH_TYPE}_graph{i}"]

    ng = ASSGRB(graph)
    sol_ng = ng.solve(60)
    print(sol_ng)
    instances.append(i)
    strategies.append("ASS_GRB")
    metrics.append(sol_ng)

    instances_lb.append(i)
    strategies_lb.append("ASS_GRB")
    metrics_lb.append(ng.lb)


    ms = ASS_SGRB(graph)
    sol_ms = ms.solve(60)
    instances.append(i)
    strategies.append("ASS_S_GRB")
    metrics.append(sol_ms)

    instances_lb.append(i)
    strategies_lb.append("ASS_S_GRB")
    metrics_lb.append(ng.lb)


    ds = REP_GRB(graph)
    sol_ds = ds.solve(60)
    instances.append(i)
    strategies.append("REP_GRB")
    metrics.append(sol_ds)

    instances_lb.append(i)
    strategies_lb.append("REP_GRB")
    metrics_lb.append(ng.lb)


with open(f"grb_{GRAPH_TYPE}_dataset_obj.txt", "w", encoding="utf-8") as file:
    file.write(f"[{', '.join(map(str, instances))}]\n")
    file.write(f'''["{'", "'.join(strategies)}"]\n''')
    file.write(f"[{', '.join(map(str, metrics))}]\n")

with open(f"grb_{GRAPH_TYPE}_dataset_lb.txt", "w", encoding="utf-8") as file:
    file.write(f"[{', '.join(map(str, instances_lb))}]\n")
    file.write(f'''["{'", "'.join(strategies_lb)}"]\n''')
    file.write(f"[{', '.join(map(str, metrics_lb))}]\n")


data = pd.DataFrame({
    "instance": instances,
    "strategy": strategies,
    "metric": metrics,
})
