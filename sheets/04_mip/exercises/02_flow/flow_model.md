# Mathematical model

**Parameters**:
- Locations $L$
- Mines $m \in M \subset{L}$ with ore production (per hour) $o_m \in \mathbb{N}$
- Elevator $x$
- Tunnels $t \in T$ with $t = (u,v)$ and $u,v \in L$. Each tunnel has a throuput $u_e \in \mathbb{N}$ and maintaining costs $c_e \in \mathbb{R}$
- Budget $b \in \mathbb{R}$

We construct a directed graph $G = (V,E)$ with:
- Edges (tunnels) $e \in E$ with costs $c_e \in \mathbb{R}$ and troughput $u_e \in \mathbb{N}$. For every $t = (u,v) \in T$, there is $e_1 = (u,v)$ and $e_2 = (v,u)$ in $E$.
- Nodes (mines) $m \in M \subset V$ with output $o_m$
- Node (central elevator) $x \in V$. 
- $V = M \cup \{x\}$

**Variables**:
- $x_e \in \{0,1 \}$  for every $e \in E$. The boolean variable is 1 if the edge in included in the flow and 0 else.
- $f_{u,v} \in \mathbb{N}_{\leq u_e}$ for every $(u,v) = e \in E$. The flow variable of an edge indicates the throughput of ores in the flow.

**Constraints**:
- Every Tunnel can only be used in one direction (only one directed edge connecting the same two nodes can be taken):

```math
x_e + x_f \leq 1 \:,\text{ where } e=(u,v), \: f=(v,u) \in E
```

- The elevator has to be included in the flow as the destination:
```math
\sum_{e=(u,v) \in E;v=x} x_e \geq 1
```

- Flow has to be conserved. For every mine, there can not be more ore leaving it than ore entering and produced:
```math
\forall u \in M: (\sum_{e=(v,u) \in E} x_e f_{v,u}) \: + o_u\geq \sum_{g=(u,w) \in E} x_g f_{u,w}
```

- There can be no flow going out of the elevator $x$:
```math
\sum_{e=(x,u) \in E} x_e f_{x,u}
```

- The budget has to be respected:
```math
\sum_{e \in E} x_e c_e \leq b 
```

**Objective**:

Maximize the flow coming into the elevator $x$:
```math
\text{max} \: \sum_{e=(u,x) \in E} x_e f_{u,x}
```

## 2.
The problem can be solved in CP-SAT, since the solver also accepts integer variables and linear constraints on them. The flow variables are all bounded, so there is no issue in using them.

Card-Solvers could, in theory, also solve this problem. The integer variables would have to be encoded as boolean variables, i. e. with a binary encoding and a boolean variable for every digit. The model would have to be adjusted to the encoding, meaning the one above could not be reused.



# Part 3

Running `instance_500` gives the following output:

```
Optimize a model with 876 rows, 5238 columns and 3992 nonzeros (Max)
Model fingerprint: 0x341213fc
Model has 0 linear objective coefficients
Model has 250 quadratic objective terms
Model has 499 quadratic constraints
Variable types: 0 continuous, 5238 integer (3492 binary)
Coefficient statistics:
  Matrix range     [5e-01, 2e+01]
  QMatrix range    [1e+00, 1e+00]
  Objective range  [0e+00, 0e+00]
  QObjective range [2e+00, 2e+00]
  Bounds range     [1e+00, 2e+01]
  RHS range        [1e+00, 4e+03]
  QRHS range       [1e+00, 1e+01]
Presolve removed 251 rows and 2247 columns
Presolve time: 0.01s
Presolved: 5582 rows, 4486 columns, 16165 nonzeros
Variable types: 0 continuous, 4486 integer (1628 binary)
Found heuristic solution: objective 1.0000000
Found heuristic solution: objective 5.0000000
Found heuristic solution: objective 36.0000000

Root relaxation: objective 2.243000e+03, 1245 iterations, 0.01 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 2243.00000    0  127   36.00000 2243.00000  6131%     -    0s
H    0     0                      39.0000000 2243.00000  5651%     -    0s
H    0     0                    1944.0000000 2243.00000  15.4%     -    0s
H    0     0                    1946.0000000 2243.00000  15.3%     -    0s
H    0     0                    1957.0000000 2243.00000  14.6%     -    0s
H    0     0                    1959.0000000 2243.00000  14.5%     -    0s
H    0     0                    1971.0000000 2243.00000  13.8%     -    0s
H    0     0                    1980.0000000 2243.00000  13.3%     -    0s
H    0     0                    1981.0000000 2243.00000  13.2%     -    0s
H    0     0                    1992.0000000 2243.00000  12.6%     -    0s
H    0     0                    1993.0000000 2243.00000  12.5%     -    0s
H    0     0                    2003.0000000 2243.00000  12.0%     -    0s
H    0     0                    2004.0000000 2243.00000  11.9%     -    0s
H    0     0                    2008.0000000 2243.00000  11.7%     -    0s
H    0     0                    2011.0000000 2243.00000  11.5%     -    0s
     0     0 2243.00000    0  275 2011.00000 2243.00000  11.5%     -    0s
     0     0 2243.00000    0  265 2011.00000 2243.00000  11.5%     -    0s
H    0     0                    2016.0000000 2243.00000  11.3%     -    0s
H    0     0                    2026.0000000 2243.00000  10.7%     -    0s
H    0     0                    2027.0000000 2243.00000  10.7%     -    0s
H    0     0                    2029.0000000 2243.00000  10.5%     -    0s
H    0     0                    2030.0000000 2243.00000  10.5%     -    0s
H    0     0                    2031.0000000 2243.00000  10.4%     -    0s
H    0     0                    2035.0000000 2243.00000  10.2%     -    0s
H    0     0                    2056.0000000 2243.00000  9.10%     -    0s
H    0     0                    2066.0000000 2243.00000  8.57%     -    0s
H    0     0                    2067.0000000 2243.00000  8.51%     -    0s
H    0     0                    2071.0000000 2243.00000  8.31%     -    0s
H    0     0                    2072.0000000 2243.00000  8.25%     -    0s
H    0     0                    2073.0000000 2243.00000  8.20%     -    0s
H    0     0                    2074.0000000 2243.00000  8.15%     -    0s
H    0     0                    2075.0000000 2229.07862  7.43%     -    0s
H    0     0                    2079.0000000 2229.07862  7.22%     -    0s
H    0     0                    2081.0000000 2229.07862  7.12%     -    0s
     0     0 2229.07862    0  585 2081.00000 2229.07862  7.12%     -    0s
     0     0 2229.07862    0  583 2081.00000 2229.07862  7.12%     -    0s
H    0     0                    2082.0000000 2220.48944  6.65%     -    0s
H    0     0                    2083.0000000 2220.48944  6.60%     -    0s
H    0     0                    2084.0000000 2220.48944  6.55%     -    0s
     0     0 2220.48944    0  533 2084.00000 2220.48944  6.55%     -    0s
     0     0 2219.87031    0  559 2084.00000 2219.87031  6.52%     -    0s
     0     0 2219.81223    0  560 2084.00000 2219.81223  6.52%     -    0s
H    0     0                    2098.0000000 2219.81223  5.81%     -    0s
H    0     0                    2112.0000000 2219.81223  5.10%     -    0s
H    0     0                    2116.0000000 2219.81223  4.91%     -    0s
H    0     0                    2131.0000000 2219.81223  4.17%     -    0s
H    0     0                    2137.0000000 2219.81223  3.88%     -    0s
H    0     0                    2138.0000000 2219.81223  3.83%     -    0s
H    0     0                    2140.0000000 2219.81223  3.73%     -    0s
H    0     0                    2141.0000000 2219.81223  3.68%     -    0s
H    0     0                    2142.0000000 2219.81223  3.63%     -    0s
H    0     0                    2143.0000000 2219.81223  3.58%     -    0s
H    0     0                    2144.0000000 2207.33788  2.95%     -    0s
H    0     0                    2145.0000000 2207.33788  2.91%     -    0s
H    0     0                    2146.0000000 2207.33788  2.86%     -    0s
H    0     0                    2147.0000000 2207.33788  2.81%     -    0s
H    0     0                    2148.0000000 2207.33788  2.76%     -    0s
     0     0 2207.33788    0  486 2148.00000 2207.33788  2.76%     -    0s
H    0     0                    2149.0000000 2207.28743  2.71%     -    0s
H    0     0                    2150.0000000 2207.28743  2.66%     -    0s
H    0     0                    2151.0000000 2207.28743  2.62%     -    0s
H    0     0                    2157.0000000 2207.28743  2.33%     -    0s
H    0     0                    2159.0000000 2207.28743  2.24%     -    0s
H    0     0                    2160.0000000 2207.28743  2.19%     -    0s
H    0     0                    2161.0000000 2207.28743  2.14%     -    0s
H    0     0                    2163.0000000 2207.28743  2.05%     -    0s
H    0     0                    2164.0000000 2207.28743  2.00%     -    0s
H    0     0                    2165.0000000 2207.28743  1.95%     -    0s
H    0     0                    2166.0000000 2207.28743  1.91%     -    0s
H    0     0                    2167.0000000 2207.28743  1.86%     -    0s
     0     0 2205.68030    0  590 2167.00000 2205.68030  1.78%     -    0s
H    0     0                    2169.0000000 2205.68030  1.69%     -    1s
H    0     0                    2174.0000000 2205.68030  1.46%     -    1s
H    0     0                    2175.0000000 2205.68030  1.41%     -    1s
H    0     0                    2176.0000000 2205.68030  1.36%     -    1s
H    0     0                    2178.0000000 2205.68030  1.27%     -    1s
H    0     0                    2180.0000000 2205.68030  1.18%     -    1s
H    0     0                    2181.0000000 2205.68030  1.13%     -    1s
     0     0 2202.29884    0  549 2181.00000 2202.29884  0.98%     -    1s
     0     0 2202.26995    0  549 2181.00000 2202.26995  0.98%     -    1s
     0     0 2202.26995    0  544 2181.00000 2202.26995  0.98%     -    1s
H    0     0                    2186.0000000 2202.25899  0.74%     -    1s
H    0     0                    2191.0000000 2202.25899  0.51%     -    1s
H    0     0                    2192.0000000 2202.25899  0.47%     -    1s
     0     2 2202.25899    0  544 2192.00000 2202.25899  0.47%     -    1s
H  735   592                    2193.0000000 2199.94518  0.32%  37.8    2s
  1727  1366 2194.69369   37  574 2193.00000 2198.98849  0.27%  28.8    5s
  1786  1406 2194.74837   37  260 2193.00000 2195.40568  0.11%  27.9   10s
  1807  1421 2194.53919   71  166 2193.00000 2195.34948  0.11%  34.6   15s
  2922  1126 2194.31124   46  129 2193.00000 2194.59092  0.07%  39.1   20s

Cutting planes:
  Gomory: 89
  Cover: 4
  Implied bound: 16
  MIR: 237
  StrongCG: 10
  Flow cover: 429
  Flow path: 6
  Zero half: 47
  RLT: 6
  Relax-and-lift: 76

Explored 3173 nodes (130034 simplex iterations) in 20.42 seconds (10.42 work units)
Thread count was 16 (of 16 available processors)

Solution count 10: 2193 2193 2192 ... 2178

Optimal solution found (tolerance 1.00e-04)
Best objective 2.193000000000e+03, best bound 2.193000000000e+03, gap 0.0000%
```

We can see that:

- We reach a solution that is within 5% of the optimal solution (gap ~5%) within the first second of solve time, being effectively instantaneous
- We reach a solution that is within 1% of the optimal solution (gap ~1%) after one second of solve time, taking longer, but still being very fast.
- We reach an optimal solution (gap ~0%) after 20 seconds of solve time, taking 20x longer (2000%) for a solution that is 1% better.