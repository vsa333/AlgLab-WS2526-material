from models.gurobi.ass_grb import ASSGRB
from models.gurobi.ass_s_grb import ASS_SGRB
from models.gurobi.rep_grb import REP_GRB

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




instances = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
strategies = ["GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "GCSATSolver", "ASS_CP", "ASS_SCP", "REP_CP", "CP_NEQ", "CP_ALLDIFF", "ASS_GRB", "ASS_SGRB", "REP_GRB", "ASS_GRB", "ASS_SGRB", "REP_GRB", "ASS_GRB", "ASS_SGRB", "REP_GRB", "ASS_GRB", "ASS_SGRB", "REP_GRB", "ASS_GRB", "ASS_SGRB", "REP_GRB", "ASS_GRB", "ASS_SGRB", "REP_GRB", "ASS_GRB", "ASS_SGRB", "REP_GRB", "ASS_GRB", "ASS_SGRB", "REP_GRB", "ASS_GRB", "ASS_SGRB", "REP_GRB", "ASS_GRB", "ASS_SGRB", "REP_GRB"]
metrics = [12, 9.0, 9.0, 10.0, 10.0, 10.0, 13, 9.0, 9.0, 10.0, 10.0, 10.0, 13, 10.0, 10.0, 10.0, 10.0, 10.0, 12, 9.0, 9.0, 10.0, 10.0, 10.0, 13, 9.0, 9.0, 10.0, 10.0, 10.0, 12, 9.0, 9.0, 10.0, 10.0, 10.0, 12, 10.0, 10.0, 11.0, 10.0, 10.0, 12, 9.0, 10.0, 10.0, 10.0, 10.0, 13, 9.0, 9.0, 10.0, 10.0, 10.0, 13, 9.0, 9.0, 10.0, 10.0, 10.0, 11.0, 11.0, 12.0, 12.0, 12.0, 14.0, 13.0, 11.0, 14.0, 11.0, 10.0, 12.0, 12.0, 11.0, 14.0, 11.0, 11.0, 13.0, 11.0, 10.0, 13.0, 11.0, 10.0, 14.0, 12.0, 10.0, 12.0, 13.0, 12.0, 13.0]




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

ax.figure.savefig("benchmarking/plots/all_performance_profile_test.png", dpi=300, bbox_inches="tight")

