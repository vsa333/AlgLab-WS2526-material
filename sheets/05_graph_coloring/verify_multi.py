from _alglab_utils import CHECK, main, mandatory_testcase
from _gclib import GCGraphInstance
from heuristics.multi_start_greedy import GCMultiStartGreedy


@mandatory_testcase(max_runtime_s=30)
def myciel3():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel3"]
    ng = GCMultiStartGreedy(graph)
    solution = ng.solve()
    CHECK(solution >= 4, "The solution is better than the optimum")
    CHECK((ng.best_graph.nodes[node]["color"] != ng.best_graph.nodes[neighbor]["color"] for node in ng.best_graph.nodes for neighbor in ng.best_graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def myciel4():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel4"]
    ng = GCMultiStartGreedy(graph)
    solution = ng.solve()

    CHECK(solution >= 5, "The solution is better than the optimum")
    CHECK((ng.best_graph.nodes[node]["color"] != ng.best_graph.nodes[neighbor]["color"] for node in ng.best_graph.nodes for neighbor in ng.best_graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def myciel5():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel5"]
    ng = GCMultiStartGreedy(graph)
    solution = ng.solve()

    CHECK(solution >= 6, "The solution is better than the optimum")
    CHECK((ng.best_graph.nodes[node]["color"] != ng.best_graph.nodes[neighbor]["color"] for node in ng.best_graph.nodes for neighbor in ng.best_graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def myciel6():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel6"]
    ng = GCMultiStartGreedy(graph)
    solution = ng.solve()

    CHECK(solution >= 7, "The solution is better than the optimum")
    CHECK((ng.best_graph.nodes[node]["color"] != ng.best_graph.nodes[neighbor]["color"] for node in ng.best_graph.nodes for neighbor in ng.best_graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def queen11_11():
    gc = GCGraphInstance()
    graph = gc.graphs["queen11_11"]
    ng = GCMultiStartGreedy(graph)
    solution = ng.solve()

    CHECK(solution >= 8, "The solution is better than the optimum")
    CHECK((ng.best_graph.nodes[node]["color"] != ng.best_graph.nodes[neighbor]["color"] for node in ng.best_graph.nodes for neighbor in ng.best_graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def le450_15b():
    gc = GCGraphInstance()
    graph = gc.graphs["le450_15b"]
    ng = GCMultiStartGreedy(graph)
    solution = ng.solve()

    CHECK(solution >= 8, "The solution is better than the optimum")
    CHECK((ng.best_graph.nodes[node]["color"] != ng.best_graph.nodes[neighbor]["color"] for node in ng.best_graph.nodes for neighbor in ng.best_graph.neighbors(node)), "There are adjacent nodes with the same color")










if __name__ == "__main__":
    main()
