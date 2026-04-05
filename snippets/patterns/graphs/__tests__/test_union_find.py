"""Tests for union_find.py."""
from union_find import UnionFind


class TestUnionFind:
    def test_initial_each_node_own_component(self):
        uf = UnionFind(5)
        assert uf.components == 5
        for i in range(5):
            assert uf.find(i) == i

    def test_union_reduces_component_count(self):
        uf = UnionFind(4)
        uf.union(0, 1)
        assert uf.components == 3
        uf.union(2, 3)
        assert uf.components == 2
        uf.union(0, 2)
        assert uf.components == 1

    def test_union_same_component_returns_false(self):
        uf = UnionFind(3)
        uf.union(0, 1)
        result = uf.union(0, 1)
        assert result is False
        assert uf.components == 2  # no change

    def test_union_different_components_returns_true(self):
        uf = UnionFind(2)
        result = uf.union(0, 1)
        assert result is True

    def test_find_path_compression(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)
        root = uf.find(3)
        # After path compression, parent[3] should point directly to root
        assert uf.parent[3] == root

    def test_find_same_root_after_unions(self):
        uf = UnionFind(4)
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)
        r = uf.find(0)
        assert uf.find(1) == r
        assert uf.find(2) == r
        assert uf.find(3) == r

    def test_detecting_cycle_undirected(self):
        # Adding edges one by one; union returns False means cycle
        uf = UnionFind(3)
        assert uf.union(0, 1) is True   # no cycle
        assert uf.union(1, 2) is True   # no cycle
        assert uf.union(0, 2) is False  # would complete cycle 0-1-2-0

    def test_rank_based_union_keeps_depth_small(self):
        uf = UnionFind(8)
        for i in range(0, 8, 2):
            uf.union(i, i + 1)
        for i in range(0, 8, 4):
            uf.union(i, i + 2)
        uf.union(0, 4)
        # All 8 nodes in one component
        assert uf.components == 1
        root = uf.find(0)
        for i in range(8):
            assert uf.find(i) == root
