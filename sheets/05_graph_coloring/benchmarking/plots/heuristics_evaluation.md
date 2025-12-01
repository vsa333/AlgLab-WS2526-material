# Benchmarking the Heuristics

In this chapter, we will benchmark the three different heuristics `naive_greedy`, `multi_start_greedy` and `dsatur` by runnning them on different kinds of generated graphs and plotting their performance profile, relative to each other.

## Erdos-Renyi Graphs
All the generated graphs had above 100 nodes with an edge creation probability of 0.5. The sample size was 100 graphs.

Running the heuristics resulted in the following plot:
![image](/benchmarking/plots/heuristics_performance_profile_erdos.png)
