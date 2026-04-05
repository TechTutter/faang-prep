import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (distance, node)
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]: continue  # stale heap entry — skip
        for neighbor, weight in graph[node]:
            nd = d + weight
            if nd < dist[neighbor]:
                dist[neighbor] = nd
                heapq.heappush(heap, (nd, neighbor))
    return dist
