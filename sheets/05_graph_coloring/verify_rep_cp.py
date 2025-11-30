from _alglab_utils import CHECK, main, mandatory_testcase
from _gclib import GCGraphInstance
from models.cp_sat.rep_cp import REP_CP



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



if __name__ == "__main__":
    main()