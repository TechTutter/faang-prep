from collections import defaultdict

def build_graph(edges, directed=False):
    """
    build adjacency list from edge list
    if not weighted just remove w and use graph[u].append(v) instead

    @example:
    
    edges = [(0, 1, 2), (1, 2, 3), (0, 2, 5)]
    graph = build_graph(edges) # {0: [(1, 2), (2, 5)], 1: [(2, 3)], 2: []} 
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))
    return graph
