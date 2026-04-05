directions = [(0,1),(0,-1),(1,0),(-1,0)]

def boundary_dfs(board):
    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols): return
        if board[r][c] != 'O': return
        board[r][c] = 'S'  # mark as boundary-reachable (safe)
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # Step 1: flood fill from every boundary cell
    for r in range(rows):
        for c in range(cols):
            if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == 'O':
                dfs(r, c)

    # Step 2: remaining 'O' = surrounded; 'S' = safe → restore
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':   board[r][c] = 'X'
            elif board[r][c] == 'S': board[r][c] = 'O'
