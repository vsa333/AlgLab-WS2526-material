from _gclib import GCGraphInstance

gc = GCGraphInstance("barabasi", gen=10)
all_graphs = {}
i = 0
for k in gc.graphs.values():
    all_graphs[i] = k
    i += 1


for name in all_graphs.keys():
    graph = all_graphs[name]

    with open(f"instances/barabasi_albert_graph{name}.col", "w", encoding="utf-8") as file:
        for u, v in graph.edges():
            file.write(f"e {u} {v}\n")
    
