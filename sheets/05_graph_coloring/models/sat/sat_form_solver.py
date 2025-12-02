import networkx as nx
from models.sat.sat_form_decision_variant import GCSATDecisionVariant
from heuristics.multi_start_greedy import GCMultiStartGreedy
import time
import math
import time
import typing

class GCSATSolver:


    def __init__(self, G: nx.Graph):
        self.graph = G
        self.nodes = self.graph.nodes()
        self.k = GCMultiStartGreedy(self.graph).solve()
        self.colors = [i+1 for i in range(self.k)]


    def solve(self, time_limit: float = 60):
        self.solution = self.k
        self.status = None

        self.timer = Timer(time_limit)
    
        while True:
            split_idx = len(self.colors) // 2
            left_side = [color for color in self.colors if color <= self.colors[split_idx-1]]
            right_side = [color for color in self.colors if color > self.colors[split_idx-1]]

            if self.timer.is_out_of_time(): break
                        
            gc_solver = GCSATDecisionVariant(self.graph, self.colors[split_idx-1], self.timer.remaining())
            coloring, status = gc_solver.solve()
            
            if status is None: break

            if coloring is None:
                self.colors = right_side
            else:
                self.solution = coloring
                self.colors = left_side
            
            if len(self.colors) <= 1:
                gc_solver = GCSATDecisionVariant(self.graph, self.colors[0])
                coloring, status = gc_solver.solve()
                if status is None: break
                self.graph = gc_solver.graph
                self.solution = coloring

                return self.solution
        
        print("Solver timed out")
        return self.solution

            
""" 
class Timer:
    def __init__(self, time_limit):
        self.start = time.time()
        self.end = self.start
        self.timelimit = time_limit


    def check(self):
        self.end = time.time()
        if round(self.end-self.start) >= self.timelimit:
            return 1
        else:
            return 0
        
    def time_remaining(self):
        self.end = time.time()
        return self.timelimit-(self.end-self.start)
    
 """
class Timer:
    """
    A simple timer for measuring time.
    """

    def __init__(self, runtime: float = 0.0):
        self.runtime = runtime
        self.start = time.time()
        self.saved_times = []

    def remaining(self) -> float:
        """
        The remaining time.
        """
        return self.runtime - self.time()

    def time(self) -> float:
        """
        Time since the creation of the timer.
        """
        return time.time() - self.start

    def reset(self, runtime: typing.Optional[float] = None):
        if runtime is not None:
            self.runtime = runtime
        self.start = time.time()
        self.saved_times = []

    def __bool__(self):
        """
        Returns true if there is still time remaining.
        """
        return not self.is_out_of_time()

    def is_out_of_time(self) -> bool:
        return self.remaining() < 0

    def lap(self, label):
        self.saved_times.append((self.time(), label))

    def get_laps(self):
        return list(self.saved_times)

    def check(self):
        if not bool(self):
            raise TimeoutError()