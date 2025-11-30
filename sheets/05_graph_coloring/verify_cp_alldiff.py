from _alglab_utils import CHECK, main, mandatory_testcase
from _gclib import GCGraphInstance
from models.cp_sat.cp_alldiff import CP_ALLDIFF


@mandatory_testcase(max_runtime_s=30)
def myciel3():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel3"]
    ng = CP_ALLDIFF(graph)
    solution = ng.solve()
    CHECK(solution == 4, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def myciel4():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel4"]
    ng = CP_ALLDIFF(graph)
    solution = ng.solve()

    CHECK(solution == 5, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def queen5_5():
    gc = GCGraphInstance()
    graph = gc.graphs["queen5_5"]
    ng = CP_ALLDIFF(graph)
    solution = ng.solve()

    CHECK(solution == 5, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")

@mandatory_testcase(max_runtime_s=30)
def queen6_6():
    gc = GCGraphInstance()
    graph = gc.graphs["queen6_6"]
    ng = CP_ALLDIFF(graph)
    solution = ng.solve()

    CHECK(solution == 7, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


if __name__ == "__main__":
    main()
