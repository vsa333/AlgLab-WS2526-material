from _alglab_utils import CHECK, main, mandatory_testcase
from _gclib import GCGraphInstance
# from heuristics.naive_greedy import GCNaiveGreedy#
from models.cp_sat.ass_cp import ASSCP
from models.preprocessor import GCPreprocessor


@mandatory_testcase(max_runtime_s=60)
def queen6_6_ass():
    gc = GCGraphInstance()
    graph = gc.graphs["le450_15b"]
    pp = GCPreprocessor(graph)
    rdc_graph = pp.preprocess()

    len_b = len(graph.nodes)
    len_a = len(rdc_graph.nodes)

    print(f"\n\nReduced Graph from {len_b} nodes and {len(graph.edges())} to Graph with {len_a} nodes and {len(rdc_graph.edges())}\n\n")
    """ 
    ng = ASSCP(rdc_graph)
    solution = ng.solve()
    ng.graph = pp.postprocess(ng.graph, solution)

    len_p = len(ng.graph.nodes)
    """
    #CHECK((len_b == len_p), "Result graph has more/less nodes than original")
    #CHECK((ng.graph.nodes[node]["color"] != ng.graph.nodes[neighbor]["color"] for node in ng.graph.nodes for neighbor in ng.graph.neighbors(node)), "There are adjacent nodes with the same color")


if __name__ == "__main__":
    main()