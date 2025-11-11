#### Parameters:

- $G=(V,E)$: A graph with vertices $V$ and undirected edges $E$.
- $k$: The maximum number of vertices that can be selected.
- $d_{vw} \in \mathbb{R}^+_0$: Weighted distance of vertex $v$ to $w$
- $c$: Objective Value. Maximum allowed distance in the decision vaiant
- $D_v: \{ w \in V | d_{vw} \leq c\}, v \in V$

#### Decision Variables:

- $x_v \in \mathbb{B} \quad \forall v \in V$: A boolean variable indicating if
  vertex $v$ is selected as a center.

#### Constraints:

1. **Cardinality Constraint**: At most $k$ vertices can be selected.
   - $\sum_{v \in V} x_v \leq k$
2. **Objective Value Constraint**: For every vertex, ensure that the maximum distance to any other vertex is at most $c$
   - $\forall v \in V: \quad \bigvee_{w \in D_v} x_w$