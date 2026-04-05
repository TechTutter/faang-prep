"""Tests for has_cycle.py (DFS-based cycle detection in directed graphs)."""
from collections import defaultdict
from has_cycle import has_cycle


def _graph(edges, n):
    g = defaultdict(list)
    for i in range(n):
        g[i]  # ensure all nodes present
    for u, v in edges:
        g[u].append(v)
    return g


def _detect(edges, n):
    g = _graph(edges, n)
    state = [0] * n
    for node in range(n):
        if state[node] == 0:
            if has_cycle(g, node, state):
                return True
    return False


class TestHasCycle:
    def test_simple_cycle(self):
        # 0->1->2->0
        assert _detect([(0, 1), (1, 2), (2, 0)], 3) is True

    def test_no_cycle_in_dag(self):
        # 0->1->2->3
        assert _detect([(0, 1), (1, 2), (2, 3)], 4) is False

    def test_self_loop_is_cycle(self):
        assert _detect([(0, 0)], 1) is True

    def test_single_node_no_cycle(self):
        assert _detect([], 1) is False

    def test_back_edge_in_tree_is_cycle(self):
        # tree 0->1, 0->2, 1->3, plus back edge 3->0
        assert _detect([(0, 1), (0, 2), (1, 3), (3, 0)], 4) is True

    def test_cross_edge_not_cycle(self):
        # 0->1, 0->2, 1->3, 2->3  — DAG, no cycle
        assert _detect([(0, 1), (0, 2), (1, 3), (2, 3)], 4) is False

    def test_fully_connected_dag(self):
        # 0->1->2->3, 0->2, 0->3 — all forward edges
        assert _detect([(0, 1), (1, 2), (2, 3), (0, 2), (0, 3)], 4) is False

    def test_multiple_components_one_with_cycle(self):
        # Component 1: 0->1 (no cycle). Component 2: 2->3->2 (cycle).
        assert _detect([(0, 1), (2, 3), (3, 2)], 4) is True
