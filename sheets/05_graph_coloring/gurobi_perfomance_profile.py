from models.gurobi.ass_grb import ASSGRB
from models.gurobi.ass_s_grb import ASS_SGRB
from models.gurobi.rep_grb import REP_GRB
from models.preprocessor import GCPreprocessor

from _gclib import GCGraphInstance
from benchmarking import plot_performance_profile as ppp

import pandas as pd
import matplotlib
matplotlib.use("Agg")

GRAPH_TYPE = "erdos_renyi"


instances = []
strategies = []
metrics = []

gc = GCGraphInstance()


for i in range(10):
    graph_ = gc.graphs[f"{GRAPH_TYPE}_graph{i}"]


    pp = GCPreprocessor(graph_)
    graph = pp.preprocess()

    ng = ASSGRB(graph)
    sol_ng = ng.solve(60)
    instances.append(i)
    strategies.append("ASS_GRB")
    metrics.append(sol_ng)

    ms = ASS_SGRB(graph)
    sol_ms = ms.solve(60)
    instances.append(i)
    strategies.append("ASS_S_GRB")
    metrics.append(sol_ms)


    ds = REP_GRB(graph)
    sol_ds = ds.solve(60)
    instances.append(i)
    strategies.append("REP_GRB")
    metrics.append(sol_ds)


with open(f"datasets/grb_{GRAPH_TYPE}_dataset_obj_preprocessed.txt", "w", encoding="utf-8") as file:
    file.write(f"[{', '.join(map(str, instances))}]\n")
    file.write(f'''["{'", "'.join(strategies)}"]\n''')
    file.write(f"[{', '.join(map(str, metrics))}]\n")


data = pd.DataFrame({
    "instance": instances,
    "strategy": strategies,
    "metric": metrics,
})
