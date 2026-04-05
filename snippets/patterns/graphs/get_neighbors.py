directions = [(0,1),(0,-1),(1,0),(-1,0)]

# Generator to yield valid neighboring coordinates in a grid
def get_neighbors(r, c, grid):
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            yield nr, nc