# Data Structures

## Arrays & Strings

[[arrays-and-strings.md]]

## Lists (Stack, Queue, Heap)

- **Stack** — LIFO. Use for: DFS, backtracking, balancing brackets, monotonic stack problems. O(1) push/pop.
- **Queue** — FIFO. Use for: BFS, sliding window with deque. O(1) enqueue/dequeue with a deque.
- **Heap (Priority Queue)** — Complete binary tree. Min-heap gives O(1) access to minimum. O(log n) push/pop. Use for: Top-K, Dijkstra, scheduling.

## Hash Maps / Sets

- O(1) average for insert, delete, lookup. O(n) worst case (hash collision).
- Use a set when you only need existence checks.
- Use a map when you need key → value (frequencies, caches, indices).

## Trees

- **Binary Tree** — each node has ≤ 2 children. Key traversals: inorder (sorted for BST), preorder, postorder, BFS level-order.
- **BST** — left child < node < right child. Search/insert/delete O(h) where h = height. Balanced BST → O(log n).

## Graphs

- Represented as adjacency list (sparse) or matrix (dense).
- Traversal: BFS (shortest path, unweighted), DFS (cycle detection, topological sort, connected components).
