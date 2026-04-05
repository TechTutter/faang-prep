"""Tests for bipartite.py."""
from collections import defaultdict
from bipartite import is_bipartite


def _graph(n, edges):
    g = defaultdict(list)
    for i in range(n):
        g[i]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g


class TestIsBipartite:
    def test_even_cycle_is_bipartite(self):
        # Square: 0-1-2-3-0 — even cycle
        g = _graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
        assert is_bipartite(g, 4) is True

    def test_odd_cycle_not_bipartite(self):
        # Triangle: 0-1-2-0 — odd cycle
        g = _graph(3, [(0, 1), (1, 2), (2, 0)])
        assert is_bipartite(g, 3) is False

    def test_tree_is_always_bipartite(self):
        # Star tree: 0 connected to 1,2,3
        g = _graph(4, [(0, 1), (0, 2), (0, 3)])
        assert is_bipartite(g, 4) is True

    def test_single_node_is_bipartite(self):
        g = _graph(1, [])
        assert is_bipartite(g, 1) is True

    def test_two_nodes_connected_is_bipartite(self):
        g = _graph(2, [(0, 1)])
        assert is_bipartite(g, 2) is True

    def test_disconnected_bipartite_components(self):
        # Two separate even cycles
        g = _graph(8, [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4)])
        assert is_bipartite(g, 8) is True

    def test_disconnected_one_odd_component(self):
        # One even cycle + one triangle
        g = _graph(7, [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 4)])
        assert is_bipartite(g, 7) is False

    def test_complete_bipartite_k33(self):
        # K3,3: {0,1,2} fully connected to {3,4,5}
        edges = [(u, v) for u in range(3) for v in range(3, 6)]
        g = _graph(6, edges)
        assert is_bipartite(g, 6) is True
