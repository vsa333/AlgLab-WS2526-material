from _alglab_utils import CHECK, main, mandatory_testcase
from _gclib import GCGraphInstance
from models.cp_sat.ass_cp import ASSCP
from models.cp_sat.ass_s_cp import ASS_SCP



@mandatory_testcase(max_runtime_s=30)
def myciel3_ass():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel3"]
    ng = ASSCP(graph)
    solution = ng.solve()

    CHECK(solution == 4, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def myciel4_ass():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel4"]
    ng = ASSCP(graph)
    solution = ng.solve()

    CHECK(solution == 5, f"Not the optimal solution: {solution} != 5")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=90)
def myciel5_ass():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel5"]
    ng = ASSCP(graph)
    solution = ng.solve()

    CHECK(solution == 6, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")





@mandatory_testcase(max_runtime_s=30)
def myciel3_ass_s():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel3"]
    ng = ASS_SCP(graph)
    solution = ng.solve()

    CHECK(solution == 4, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def myciel4_ass_s():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel4"]
    ng = ASS_SCP(graph)
    solution = ng.solve()

    CHECK(solution == 5, f"Not the optimal solution: {solution} != 5")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=90)
def myciel5_ass_s():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel5"]
    ng = ASS_SCP(graph)
    solution = ng.solve()

    CHECK(solution == 6, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


if __name__ == "__main__":
    main()