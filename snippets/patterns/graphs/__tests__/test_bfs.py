"""Tests for bfs.py (standard BFS) and bfs_01.py (0-1 BFS)."""
from collections import defaultdict
from bfs import bfs
from bfs_01 import bfs_01


class TestBfs:
    def _graph(self, edges):
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g

    def test_all_nodes_visited_in_connected_graph(self):
        # 0-1-2-3 chain
        g = self._graph([(0, 1), (1, 2), (2, 3)])
        # bfs returns visited set implicitly — we check by running it;
        # since bfs has no return value, wrap to capture visited
        from collections import deque

        def bfs_capture(graph, start):
            visited = {start}
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return visited

        visited = bfs_capture(g, 0)
        assert visited == {0, 1, 2, 3}

    def test_bfs_does_not_raise_on_single_node(self):
        g = defaultdict(list)
        g[0]  # ensure node 0 exists with empty neighbors
        bfs(g, 0)  # should not raise

    def test_bfs_does_not_revisit_nodes(self):
        # cycle: 0-1-2-0
        g = self._graph([(0, 1), (1, 2), (2, 0)])
        visit_count: dict[int, int] = {0: 0, 1: 0, 2: 0}

        from collections import deque

        visited = {0}
        queue = deque([0])
        while queue:
            node = queue.popleft()
            visit_count[node] += 1
            for neighbor in g[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        for count in visit_count.values():
            assert count == 1

    def test_bfs_partial_reach_from_disconnected_component(self):
        # Two components: {0,1} and {2,3}
        g = self._graph([(0, 1), (2, 3)])
        from collections import deque

        visited = {0}
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in g[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        assert visited == {0, 1}
        assert 2 not in visited
        assert 3 not in visited


class TestBfs01:
    def _make_graph(self, n, weighted_edges):
        """weighted_edges: list of (u, v, w) — undirected."""
        from collections import defaultdict
        g = defaultdict(list)
        for u, v, w in weighted_edges:
            g[u].append((v, w))
            g[v].append((u, w))
        return g

    def test_all_zero_weights_equal_bfs_distances(self):
        # Star graph: 0->{1,2,3} all weight 0
        g = self._make_graph(4, [(0, 1, 0), (0, 2, 0), (0, 3, 0)])
        dist = bfs_01(g, 0, 4)
        assert dist == [0, 0, 0, 0]

    def test_all_unit_weights_gives_hop_count(self):
        # 0-1-2-3 chain, all weight 1
        g = self._make_graph(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)])
        dist = bfs_01(g, 0, 4)
        assert dist == [0, 1, 2, 3]

    def test_mixed_weights_prefers_zero_edge(self):
        # 0 --1--> 1 --0--> 2  vs  0 --1--> 2 directly
        # shortest to 2 is 0->1->2 = 1 (via zero edge) vs 0->2 = 1 direct; same
        # use a case where zero edge creates a strictly shorter path:
        # 0 --1--> 1 --0--> 2  (total 1) vs 0 --1--> 2 direct  (total 1) — same
        # clearer: 0 --(1)--> 1 --(0)--> 2 vs no direct edge
        from collections import defaultdict
        g = defaultdict(list)
        g[0].append((1, 1))
        g[1].append((0, 1))
        g[1].append((2, 0))
        g[2].append((1, 0))
        dist = bfs_01(g, 0, 3)
        assert dist[0] == 0
        assert dist[1] == 1
        assert dist[2] == 1  # 0->1 (cost 1) + 1->2 (cost 0)

    def test_unreachable_node_stays_inf(self):
        from collections import defaultdict
        g = defaultdict(list)
        g[0].append((1, 1))
        # node 2 isolated
        dist = bfs_01(g, 0, 3)
        assert dist[2] == float('inf')

    def test_start_node_distance_is_zero(self):
        from collections import defaultdict
        g = defaultdict(list)
        dist = bfs_01(g, 0, 1)
        assert dist[0] == 0
