from _alglab_utils import CHECK, main, mandatory_testcase
from _gclib import GCGraphInstance
# from heuristics.naive_greedy import GCNaiveGreedy#
from models.cp_sat.ass_cp import ASSCP
from models.preprocessor import GCPreprocessor


@mandatory_testcase(max_runtime_s=30)
def queen6_6_ass():
    gc = GCGraphInstance()
    graph = gc.graphs["erdos_renyi_graph0"]
    pp = GCPreprocessor(graph)
    rdc_graph = pp.preprocess()
    ng = ASSCP(rdc_graph)
    solution = ng.solve()
    ng.graph = pp.postprocess(ng.graph, solution)

    print(len(graph.nodes))
    print(len(rdc_graph.nodes))
    print(len(ng.graph.nodes))

    CHECK(solution == 7, f"Not the optimal solution: {solution} != 7")
    CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


if __name__ == "__main__":
    main()