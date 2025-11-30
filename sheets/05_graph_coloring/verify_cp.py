from _alglab_utils import CHECK, main, mandatory_testcase
from _gclib import GCGraphInstance
from models.cp_sat.ass_cp import ASSCP
from models.cp_sat.ass_s_cp import ASS_SCP
from models.cp_sat.rep_cp import REP_CP
from models.cp_sat.cp_neq import CP_NEQ




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



@mandatory_testcase(max_runtime_s=30)
def queen6_6_ass():
    gc = GCGraphInstance()
    graph = gc.graphs["queen6_6"]
    ng = ASSCP(graph)
    solution = ng.solve()

    CHECK(solution == 7, f"Not the optimal solution: {solution} != 7")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


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


@mandatory_testcase(max_runtime_s=30)
def queen6_6_ass_s():
    gc = GCGraphInstance()
    graph = gc.graphs["queen6_6"]
    ng = ASSCP(graph)
    solution = ng.solve()

    CHECK(solution == 7, f"Not the optimal solution: {solution} != 7")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


def myciel5_ass_s():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel5"]
    ng = ASS_SCP(graph)
    solution = ng.solve()

    CHECK(solution == 6, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def myciel3_rep_cp():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel3"]
    ng = REP_CP(graph)
    solution = ng.solve()

    CHECK(solution == 4, "Not the optimal solution")


@mandatory_testcase(max_runtime_s=30)
def myciel4_rep_cp():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel4"]
    ng = REP_CP(graph)
    solution = ng.solve()

    CHECK(solution == 5, f"Not the optimal solution: {solution} != 5")


@mandatory_testcase(max_runtime_s=30)
def queen6_6_rep_cp():
    gc = GCGraphInstance()
    graph = gc.graphs["queen6_6"]
    ng = REP_CP(graph)
    solution = ng.solve()

    CHECK(solution == 7, f"Not the optimal solution: {solution} != 7")


#@mandatory_testcase(max_runtime_s=180)
def myciel5_rep_cp():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel5"]
    ng = REP_CP(graph)
    solution = ng.solve()

    CHECK(solution == 6, "Not the optimal solution")





@mandatory_testcase(max_runtime_s=30)
def myciel3_cp_neq():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel3"]
    ng = CP_NEQ(graph)
    solution = ng.solve()
    CHECK(solution == 4, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def myciel4_cp_neq():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel4"]
    ng = CP_NEQ(graph)
    solution = ng.solve()

    CHECK(solution == 5, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def queen5_5_cp_neq():
    gc = GCGraphInstance()
    graph = gc.graphs["queen5_5"]
    ng = CP_NEQ(graph)
    solution = ng.solve()

    CHECK(solution == 5, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


@mandatory_testcase(max_runtime_s=30)
def queen6_6_cp_neq():
    gc = GCGraphInstance()
    graph = gc.graphs["queen6_6"]
    ng = CP_NEQ(graph)
    solution = ng.solve()

    CHECK(solution == 7, "Not the optimal solution")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")




if __name__ == "__main__":
    main()