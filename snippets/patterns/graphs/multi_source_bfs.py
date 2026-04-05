from collections import deque

def multi_source_bfs(grid, sources):
    visited = set(sources)
    queue = deque([(r, c, 0) for r, c in sources])  # (row, col, dist)
    while queue:
        r, c, dist = queue.popleft()
        for nr, nc in get_neighbors(r, c, grid):
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
