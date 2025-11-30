from _alglab_utils import CHECK, main, mandatory_testcase
from _gclib import GCGraphInstance
from models.cp_sat.rep_cp import REP_CP


@mandatory_testcase(max_runtime_s=30)
def myciel3_ass_s():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel3"]
    ng = REP_CP(graph)
    solution = ng.solve()

    CHECK(solution == 4, "Not the optimal solution")


@mandatory_testcase(max_runtime_s=30)
def myciel4_ass_s():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel4"]
    ng = REP_CP(graph)
    solution = ng.solve()

    CHECK(solution == 5, f"Not the optimal solution: {solution} != 5")


@mandatory_testcase(max_runtime_s=90)
def myciel5_ass_s():
    gc = GCGraphInstance()
    graph = gc.graphs["myciel5"]
    ng = REP_CP(graph)
    solution = ng.solve()

    CHECK(solution == 6, "Not the optimal solution")


if __name__ == "__main__":
    main()