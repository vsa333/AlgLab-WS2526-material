from heuristics.dsatur import GCDsatur
from heuristics.multi_start_greedy import GCMultiStartGreedy
from heuristics.naive_greedy import GCNaiveGreedy
from _gclib import GCGraphInstance
from benchmarking import plot_performance_profile as ppp

import pandas as pd
import matplotlib
matplotlib.use("Agg")


instances = []
strategies = []
metrics = []

gc = GCGraphInstance("wheel", gen=100)
for name in gc.graphs.keys():
    graph = gc.graphs[name]

    ng = GCNaiveGreedy(graph)
    sol_ng = ng.solve()
    instances.append(name)
    strategies.append("naive_greedy")
    metrics.append(sol_ng)


    ms = GCMultiStartGreedy(graph)
    sol_ms = ms.solve()
    instances.append(name)
    strategies.append("multi_start_greedy")
    metrics.append(sol_ms)


    ds = GCDsatur(graph)
    sol_ds = ds.solve()
    instances.append(name)
    strategies.append("DSATUR")
    metrics.append(sol_ds)


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
    title="Performance Profile (Heuristics)",
    highlight_best=True,
)

#plt.show()

ax.figure.savefig("benchmarking/plots/heuristics/heuristics_performance_profile_wheel.png", dpi=300, bbox_inches="tight")

