# Benchmarking the Heuristics

In this chapter, we will benchmark the three different heuristics `naive_greedy`, `multi_start_greedy` and `dsatur` by runnning them on different kinds of generated graphs and plotting their performance profile, relative to each other.

## Erdos-Renyi Graphs
All the generated graphs had above 100 nodes with an edge creation probability of 0.5. The sample size was 100 graphs.

Running the heuristics resulted in the following plot:
![image](./plots/heuristics/heuristics_performance_profile_erdos.png)

We can see that:
- DSATUR showed the best results, returning the best known solution for ~98% of instances. For all instances, it returned a solution within 5% of the best.
- multi_start_greedy returned the best  known solution for only ~16% of instances. A solution within 5% of the known best was found only for 59% of instances. For 99% of instances, it returned a solution within 13% of the best. For all instances, if found a solution within 18% of the best.
- naive_greedy returned the best known solution for no instance. For 3% of instances, it found a solution within 5% of the best. For all instances, it returned a solution 27% of the best known.

It is evident that `DSATUR` offers the best solution most of the time, clearly outperforming the other heuristics. `multi_start_greedy` shows the second best performance, with a big gap compared to `DSATUR`. It catches up in a moderate fashion. `naive_greedy` performs the worst, not finding a best solution and scaling up the slowest.

## Barabasi-Albert Graphs
All the generated graphs had above 100 nodes with 12 edges attaching from now to existing nodes. The sample size was 100 graphs.

Running the heuristics resulted in the following plot:
![image](./plots/heuristics/heuristics_performance_profile_barabasi.png)

We can see that `DSATUR` still outperforms the other heuristics by a large margin. Both `multi_start_greedy` and `naive_greedy` show similar performance, with `multi_start_greedy` closing the gap to the best known solution in greater jumps.


## Kneser Graphs
All the generated graphs had above 10 nodes with a growing subset size above 3. The sample size was 20 graphs.

Running the heuristics resulted in the following plot:
![image](./plots/heuristics/heuristics_performance_profile_kneser.png)

While `DSATUR` completely outperformed the the other algorithms in the previous instances, it falls behind for Kneser graphs. Both `multi_start_greedy` and `naive_greedy` find the best known solution for all instances, but `DSATUR` only finds them for 20%. The performance grows continuously but ultimately for all instances, `DSATUR` only returns a solution within 40% of the best known solution.

### Honorable Mention

DSATUR usually is the better heuristic in these cases. For Cycle and Wheel graphs DSATUR is even optimal and will outperform the other heuristics even more clearly