"""Tests for build_graph.py and get_neighbors.py."""
from collections import defaultdict
from build_graph import build_graph
from get_neighbors import get_neighbors


class TestBuildGraph:
    def test_undirected_single_edge(self):
        edges = [(0, 1, 1)]
        g = build_graph(edges)
        assert (1, 1) in g[0]
        assert (0, 1) in g[1]

    def test_undirected_multiple_edges(self):
        edges = [(0, 1, 2), (1, 2, 3), (0, 2, 5)]
        g = build_graph(edges)
        assert (1, 2) in g[0]
        assert (2, 5) in g[0]
        assert (0, 2) in g[1]
        assert (2, 3) in g[1]
        assert (1, 3) in g[2]
        assert (0, 5) in g[2]

    def test_directed_edge_not_reversed(self):
        edges = [(0, 1, 10)]
        g = build_graph(edges, directed=True)
        assert (1, 10) in g[0]
        assert 0 not in g[1]  # no back-edge

    def test_directed_multiple_edges(self):
        edges = [(0, 1, 1), (1, 2, 2), (2, 0, 3)]
        g = build_graph(edges, directed=True)
        assert (1, 1) in g[0]
        assert (2, 2) in g[1]
        assert (0, 3) in g[2]
        # reverse directions must not appear
        assert (0, 1) not in g[1]

    def test_returns_defaultdict(self):
        g = build_graph([])
        # accessing a missing key should return an empty list, not raise
        assert g[99] == []

    def test_zero_weight(self):
        edges = [(0, 1, 0)]
        g = build_graph(edges)
        assert (1, 0) in g[0]
        assert (0, 0) in g[1]


class TestGetNeighbors:
    def _grid(self, rows, cols):
        return [[0] * cols for _ in range(rows)]

    def test_centre_cell_has_four_neighbors(self):
        grid = self._grid(3, 3)
        neighbors = list(get_neighbors(1, 1, grid))
        assert len(neighbors) == 4
        assert (1, 2) in neighbors
        assert (1, 0) in neighbors
        assert (0, 1) in neighbors
        assert (2, 1) in neighbors

    def test_corner_cell_has_two_neighbors(self):
        grid = self._grid(3, 3)
        neighbors = list(get_neighbors(0, 0, grid))
        assert len(neighbors) == 2
        assert (0, 1) in neighbors
        assert (1, 0) in neighbors

    def test_edge_cell_has_three_neighbors(self):
        grid = self._grid(3, 3)
        neighbors = list(get_neighbors(0, 1, grid))
        assert len(neighbors) == 3

    def test_single_cell_grid_has_no_neighbors(self):
        grid = self._grid(1, 1)
        neighbors = list(get_neighbors(0, 0, grid))
        assert neighbors == []

    def test_single_row_grid(self):
        grid = self._grid(1, 5)
        neighbors = list(get_neighbors(0, 2, grid))
        # only left/right valid (no up/down rows)
        assert (0, 1) in neighbors
        assert (0, 3) in neighbors
        assert len(neighbors) == 2
