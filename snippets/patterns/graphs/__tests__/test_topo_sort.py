"""Tests for topo_sort.py (Kahn's algorithm)."""
from topo_sort import topo_sort


def _is_valid_topo_order(order, edges):
    """Return True if `order` is a valid topological ordering.

    The snippet's edge convention: (u, v) means "u depends on v",
    which creates the internal graph edge v → u.
    In a valid order, v must therefore appear BEFORE u.
    """
    pos = {node: i for i, node in enumerate(order)}
    for u, v in edges:
        # v must come before u  →  pos[v] < pos[u]
        if pos[u] < pos[v]:  # u appears before v = INVALID
            return False
    return True


class TestTopoSort:
    def test_linear_chain(self):
        # edges (u,v) mean "u depends on v":
        # (0,1)→1 before 0, (1,2)→2 before 1, (2,3)→3 before 2
        # valid order: 3, 2, 1, 0
        edges = [(0, 1), (1, 2), (2, 3)]
        order = topo_sort(4, edges)
        assert len(order) == 4
        assert _is_valid_topo_order(order, edges)

    def test_single_node(self):
        order = topo_sort(1, [])
        assert order == [0]

    def test_no_edges_any_order_valid(self):
        order = topo_sort(3, [])
        assert sorted(order) == [0, 1, 2]

    def test_cycle_returns_empty(self):
        # 0->1->2->0 cycle
        edges = [(0, 1), (1, 2), (2, 0)]
        order = topo_sort(3, edges)
        assert order == []

    def test_diamond_dependency(self):
        # (0,1): 0 depends on 1; (0,2): 0 depends on 2
        # (1,3): 1 depends on 3; (2,3): 2 depends on 3
        # valid order: 3 first, 0 last
        edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
        order = topo_sort(4, edges)
        assert len(order) == 4
        assert _is_valid_topo_order(order, edges)

    def test_disjoint_subgraphs(self):
        # (0,1): 0 depends on 1; (2,3): 2 depends on 3
        edges = [(0, 1), (2, 3)]
        order = topo_sort(4, edges)
        assert len(order) == 4
        assert _is_valid_topo_order(order, edges)

    def test_all_depend_on_root(self):
        # (0,1),(0,2),(0,3): 0 depends on 1, 2, 3 → 0 must come LAST
        edges = [(0, 1), (0, 2), (0, 3)]
        order = topo_sort(4, edges)
        assert order[-1] == 0
        assert set(order[:-1]) == {1, 2, 3}
