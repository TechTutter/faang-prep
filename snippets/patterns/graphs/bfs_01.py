from collections import deque

# Edge weights must be 0 or 1 only. O(V+E) vs Dijkstra's O((V+E) log V).
def bfs_01(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    dq = deque([start])
    while dq:
        node = dq.popleft()
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                if weight == 0:
                    dq.appendleft(neighbor)  # free edge → front of deque
                else:
                    dq.append(neighbor)      # cost edge → back of deque
    return dist
