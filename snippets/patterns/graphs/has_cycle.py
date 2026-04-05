# States: 0=unvisited, 1=in-stack, 2=done
def has_cycle(graph, node, state):
    state[node] = 1
    for neighbor in graph[node]:
        if state[neighbor] == 1: return True      # back edge = cycle
        if state[neighbor] == 0:
            if has_cycle(graph, neighbor, state): return True
    state[node] = 2
    return False