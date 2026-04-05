# Mental Model

Three questions before touching code:

**Nodes** — what does each node represent?  
Grid cell → use `get_neighbors`. Otherwise → build an adjacency list from the input.

**Edges** — directed or undirected? weighted?  
This narrows which patterns apply (see Complexity table at the bottom).

**Goal** — pick the pattern:
- Reachability / flood fill → BFS or DFS
- Shortest path (unweighted) → BFS
- Shortest path (0/1 weights) → 0-1 BFS
- Shortest path (weighted ≥ 0) → Dijkstra
- Dependencies / ordering → Topological Sort
- Cycle in directed graph → DFS 3-color or Kahn's
- Dynamic grouping → Union-Find
- Two-partition check → Bipartite
- Spread from many sources → Multi-source BFS
- All paths / enumerate solutions → Backtracking
- Find what can't reach a boundary → Boundary DFS/BFS

# Build Graph

**When**: Input is a list of edges — always the first step before any traversal.

[[/snippets/patterns/graphs/build_graph.py]]

# get_neighbors (Grid as Graph)

**When**: Grid / matrix problems — treat each cell as a node, neighbors are 4-directional (or 8).

> Mark visited by mutating the grid (`grid[r][c] = '#'`) or use a `visited` set.

[[/snippets/patterns/graphs/get_neighbors.py]]

# Traversal

## BFS

**When**: Shortest path in unweighted graphs, level-by-level traversal, reachability.

> Add to `visited` when *enqueuing*, not dequeuing — prevents the same node being processed multiple times.

[[/snippets/patterns/graphs/bfs.py]]

## DFS

**When**: Connected components, cycle detection, exploring all paths.

> Prefer iterative DFS for large inputs — recursive DFS hits Python's recursion limit.

[[/snippets/patterns/graphs/dfs.py]]

## Multi-Source BFS

**When**: Multiple starting points simultaneously — spread from all sources at once. Avoids running BFS N times.

> Initialize the queue with *all* sources at distance 0 → single O(V+E) pass instead of O(N·BFS).

[[/snippets/patterns/graphs/multi_source_bfs.py]]

## BFS with State

**When**: Position alone is not enough — state must encode additional context (keys held, steps taken, board configuration).

> State must be hashable. Shape it as `(node, extra_context)` and treat it like any other BFS node.
>
> **Implicit graph trick**: generate neighbor states on the fly instead of precomputing all edges (e.g. try all 26-character substitutions per position for word problems).

[[/snippets/patterns/graphs/bfs_with_state.py]]

## 0-1 BFS

**When**: Edge weights are only 0 or 1. O(V+E) vs Dijkstra's O((V+E) log V).

> Use a deque: free edges (weight=0) go to the *front*, cost edges (weight=1) go to the *back*.

[[/snippets/patterns/graphs/bfs_01.py]]

# Cycle Detection and Scheduling

## DFS 3-Color (Directed Graphs)

**When**: Pure cycle detection in a directed graph — simpler than Kahn's when you don't need the ordering.

[[/snippets/patterns/graphs/has_cycle.py]]

## Topological Sort — Kahn's Algorithm

**When**: Ordering nodes with dependencies (DAG). Naturally detects cycles as a side effect.

> If `len(order) != n` after Kahn's, a cycle exists.

[[/snippets/patterns/graphs/topo_sort.py]]

# Bipartite Check

**When**: Check if a graph can be split into two groups with no intra-group edges — equivalent to checking for no odd-length cycles.

[[/snippets/patterns/graphs/bipartite.py]]

# Union-Find

**When**: Dynamic connectivity, grouping components, cycle detection in *undirected* graphs. Preferred over DFS when edges arrive one at a time.

> `union(x, y)` returns `False` if x and y are already connected — that edge creates a cycle.
> Path compression + union by rank gives near-O(1) amortized per operation.

[[/snippets/patterns/graphs/union_find.py]]

# Dijkstra

**When**: Shortest path with non-negative weights.

> Guard: `if d > dist[node]: continue` — skips stale heap entries without this the algorithm still works but does redundant work.

[[/snippets/patterns/graphs/dijkstra.py]]

# Backtracking on Graphs

**When**: Enumerate *all* paths or solutions — the visited state must be undone on the way out.

> Key distinction from DFS: DFS marks nodes permanently; backtracking *unmarks* on exit so other paths can revisit the same node.

[[/snippets/patterns/graphs/backtracking.py]]

# Boundary DFS/BFS

**When**: Find cells/nodes *not* reachable from a boundary — invert the problem instead of finding what's surrounded (hard), find what can reach the boundary (easy).

> Pattern: flood-fill from all boundary cells first, then everything unmarked is the answer.

[[/snippets/patterns/graphs/boundary_dfs.py]]

# Composability Reference

| Goal | Pattern |
|---|---|
| Reachability / connected components | DFS or BFS |
| Shortest path, unweighted | BFS |
| Shortest path, 0/1 weights | 0-1 BFS |
| Shortest path, weighted ≥ 0 | Dijkstra |
| Spread from multiple sources | Multi-source BFS |
| String / state transformation | BFS with State |
| Task ordering / dependencies | Topological Sort (Kahn's) |
| Cycle in directed graph | DFS 3-color or Kahn's |
| Cycle in undirected graph | Union-Find or DFS |
| Group membership / conflict | Bipartite Check |
| Dynamic / incremental connectivity | Union-Find |
| Enumerate all paths | Backtracking |
| Invert reachability problem | Boundary DFS/BFS |
| Grid problems | get_neighbors + any above |

# Complexity

| Pattern | Time | Space |
|---|---|---|
| BFS / DFS | O(V+E) | O(V) |
| Multi-source BFS | O(V+E) | O(V) |
| 0-1 BFS | O(V+E) | O(V) |
| Dijkstra | O((V+E) log V) | O(V) |
| Topological Sort | O(V+E) | O(V) |
| Union-Find (amortized) | O(α(N)) per op | O(V) |
| Bipartite Check | O(V+E) | O(V) |
| Backtracking | O(V!) worst | O(V) |
| Boundary DFS/BFS | O(V+E) | O(V) |

# Notes on A*

A* is essentially Dijkstra's with a heuristic to prioritize promising paths. It can be much faster than Dijkstra's when the heuristic is good, but in the worst case (bad heuristic) it degrades to O((V+E) log V). Use A* when you have domain-specific knowledge that can guide the search (e.g. Manhattan distance in grid problems), but generally Dijkstra's is more robust for interview problems unless the prompt hints at a useful heuristic.