from collections import defaultdict, deque

def topo_sort(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:          # u depends on v  →  edge: v → u
        graph[v].append(u)
        in_degree[u] += 1

    queue = deque(i for i in range(n) if in_degree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    return order if len(order) == n else []  # [] = cycle exists
