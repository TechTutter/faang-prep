"""Tests for boundary_dfs.py."""
from boundary_dfs import boundary_dfs


def _board(rows):
    """Convert a list of strings into a mutable list-of-lists."""
    return [list(row) for row in rows]


def _str(board):
    return ["".join(row) for row in board]


class TestBoundaryDfs:
    def test_interior_o_becomes_x(self):
        board = _board([
            "XXXX",
            "XOOX",
            "XXOX",
            "XOXX",
        ])
        boundary_dfs(board)
        result = _str(board)
        # Interior O's at (1,1),(1,2),(2,2) should become X
        assert result[1][1] == 'X'
        assert result[1][2] == 'X'
        assert result[2][2] == 'X'

    def test_boundary_o_preserved(self):
        board = _board([
            "OXXX",
            "XOOX",
            "XXOX",
            "XXXO",
        ])
        boundary_dfs(board)
        result = _str(board)
        # (0,0) and (3,3) are on the boundary — must stay O
        assert result[0][0] == 'O'
        assert result[3][3] == 'O'

    def test_o_connected_to_boundary_preserved(self):
        board = _board([
            "XXXX",
            "OOOX",
            "XXXX",
        ])
        boundary_dfs(board)
        result = _str(board)
        # (1,0) is on the boundary; (1,1),(1,2) connect to it → all preserved
        assert result[1][0] == 'O'
        assert result[1][1] == 'O'
        assert result[1][2] == 'O'

    def test_all_x_board_unchanged(self):
        board = _board([
            "XXXX",
            "XXXX",
            "XXXX",
        ])
        boundary_dfs(board)
        assert _str(board) == ["XXXX", "XXXX", "XXXX"]

    def test_all_o_board_preserves_boundary(self):
        board = _board([
            "OOO",
            "OOO",
            "OOO",
        ])
        boundary_dfs(board)
        result = _str(board)
        # All cells are reachable from boundary → all stay O
        assert result == ["OOO", "OOO", "OOO"]

    def test_single_cell_o(self):
        board = _board(["O"])
        boundary_dfs(board)
        # Single cell is both the entire board and on the boundary → O preserved
        assert board[0][0] == 'O'

    def test_single_cell_x(self):
        board = _board(["X"])
        boundary_dfs(board)
        assert board[0][0] == 'X'

    def test_classic_surrounded_example(self):
        board = _board([
            "XXXXX",
            "XOOOX",
            "XOXOX",
            "XOOOX",
            "XXXXX",
        ])
        boundary_dfs(board)
        result = _str(board)
        # All interior O's should be flipped
        assert result == [
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
        ]
