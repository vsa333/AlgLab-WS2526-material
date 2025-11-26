## Task C

We see that:
- The linear relaxation offers a lower bound for the minimization problem, usually within 98% of the optimal possible solution (except sample 11), making it a tight bound.
- In every sample, using k = 1 for the linear program gives a smaller objective value, and so a looser lower bound than using k = 2 (usually a 4-5% difference). From the overlap with the optimal solution, we can see that k = 2 results in a greater overlap with the actual solution, resulting in a tighter lower bound and faster pruning in a branch and bound algorithm.