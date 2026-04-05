"""Tests for dijkstra.py."""
from collections import defaultdict
from dijkstra import dijkstra


def _graph(n, weighted_edges, directed=False):
    g = defaultdict(list)
    for i in range(n):
        g[i]
    for u, v, w in weighted_edges:
        g[u].append((v, w))
        if not directed:
            g[v].append((u, w))
    return g


class TestDijkstra:
    def test_simple_chain(self):
        # 0--(1)--1--(2)--2--(1)--3
        g = _graph(4, [(0, 1, 1), (1, 2, 2), (2, 3, 1)])
        dist = dijkstra(g, 0, 4)
        assert dist == [0, 1, 3, 4]

    def test_start_node_is_zero(self):
        g = _graph(3, [(0, 1, 5), (0, 2, 10)])
        dist = dijkstra(g, 0, 3)
        assert dist[0] == 0

    def test_unreachable_node_is_inf(self):
        g = _graph(3, [(0, 1, 1)])
        # node 2 is isolated
        dist = dijkstra(g, 0, 3)
        assert dist[2] == float('inf')

    def test_shorter_alternative_path(self):
        # 0--10--1--1--2  vs  0--2--2
        g = _graph(3, [(0, 1, 10), (1, 2, 1), (0, 2, 2)])
        dist = dijkstra(g, 0, 3)
        assert dist[2] == 2  # direct path is shorter

    def test_directed_graph_one_way(self):
        # 0->1->2, no way back
        g = _graph(3, [(0, 1, 3), (1, 2, 4)], directed=True)
        dist = dijkstra(g, 0, 3)
        assert dist == [0, 3, 7]

    def test_single_node_graph(self):
        g = _graph(1, [])
        dist = dijkstra(g, 0, 1)
        assert dist == [0]

    def test_star_graph(self):
        # All edges from node 0
        g = _graph(5, [(0, 1, 1), (0, 2, 2), (0, 3, 3), (0, 4, 4)])
        dist = dijkstra(g, 0, 5)
        assert dist == [0, 1, 2, 3, 4]

    def test_stale_heap_entries_do_not_corrupt(self):
        # Graph where relaxation updates a node multiple times
        g = _graph(4, [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1)])
        dist = dijkstra(g, 0, 4)
        # 0->2->1 = 3, 0->1 = 4 → shortest to 1 is 3
        assert dist[1] == 3
        # 0->2->1->3 = 4
        assert dist[3] == 4
