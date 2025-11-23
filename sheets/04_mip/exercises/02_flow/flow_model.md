**Parameters**:
- Edges (tunnels) $e \in E$ with costs $c_e \in \mathbb{R}$ and troughput $u_e \in \mathbb{N}$
- Nodes (mines) $m \in M \subset V$ with output $o_m$
- Node (central facility) $f \in V$
- Budget $b \in \mathbb{R}$

**Variables**:
- $x_{e_1}, x_{e_2} \in \{0,1\} \text{ with } e \in E$. Boolean Variables for every Edge and both directions in the Graph. 1 means the edge is included in the flow, 0 means it is not, where

**Constraints**:
- Every Edge 