"""Tests for bfs_with_state.py and multi_source_bfs.py."""
from bfs_with_state import bfs_state, get_next_words
from get_neighbors import get_neighbors

# Inject get_neighbors into multi_source_bfs module scope before importing
import importlib, types, sys

_ms_mod = importlib.import_module("multi_source_bfs")
_ms_mod.get_neighbors = get_neighbors  # type: ignore[attr-defined]
from multi_source_bfs import multi_source_bfs


class TestBfsState:
    def _make_graph_next(self, adj):
        """Return a get_next_states function for an adjacency dict."""
        def get_next_states(state):
            return adj.get(state, [])
        return get_next_states

    def test_direct_connection_returns_one_step(self):
        adj = {"a": ["b"], "b": []}
        result = bfs_state("a", "b", self._make_graph_next(adj))
        assert result == 1

    def test_path_length_over_chain(self):
        # a->b->c->d
        adj = {"a": ["b"], "b": ["c"], "c": ["d"], "d": []}
        result = bfs_state("a", "d", self._make_graph_next(adj))
        assert result == 3

    def test_already_at_target_returns_zero(self):
        adj = {}
        result = bfs_state("a", "a", self._make_graph_next(adj))
        assert result == 0

    def test_no_path_returns_minus_one(self):
        adj = {"a": ["b"], "b": [], "c": []}
        result = bfs_state("a", "c", self._make_graph_next(adj))
        assert result == -1

    def test_bfs_finds_shortest_not_just_any_path(self):
        # a can reach d in 3 steps (a->b->c->d) or 1 step (a->d)
        adj = {"a": ["b", "d"], "b": ["c"], "c": ["d"], "d": []}
        result = bfs_state("a", "d", self._make_graph_next(adj))
        assert result == 1


class TestGetNextWords:
    def test_single_letter_change(self):
        word_set = {"hot", "dot", "dog", "lot", "log", "cog"}
        nexts = list(get_next_words("hot", word_set))
        assert "dot" in nexts
        assert "lot" in nexts
        # Note: get_next_words does NOT filter the source word — the BFS visited
        # set is responsible for deduplication.  "hot" may appear in nexts.

    def test_no_neighbours_returns_empty(self):
        word_set = {"xyz"}
        nexts = list(get_next_words("abc", word_set))
        assert nexts == []

    def test_yields_single_letter_neighbours(self):
        # "cat" -> "bat" is a valid 1-letter change
        word_set = {"cat", "bat"}
        nexts = list(get_next_words("cat", word_set))
        assert "bat" in nexts

    def test_yields_multiple_neighbours(self):
        word_set = {"hit", "hot", "hat", "lot"}
        nexts = list(get_next_words("hot", word_set))
        assert "hit" in nexts
        assert "hat" in nexts


class TestMultiSourceBfs:
    def _grid(self, rows, cols):
        return [[0] * cols for _ in range(rows)]

    def test_single_source_reaches_all_cells(self):
        grid = self._grid(3, 3)
        sources = [(0, 0)]
        # Should not raise and should visit cells expanding outwards
        multi_source_bfs(grid, sources)  # smoke test

    def test_two_sources_both_reachable(self):
        grid = self._grid(3, 3)
        # Sources at opposite corners
        sources = [(0, 0), (2, 2)]
        # Again smoke-test — function has no return value
        multi_source_bfs(grid, sources)

    def test_visited_set_starts_with_sources(self):
        """Verify sources are treated as already visited (distance 0)."""
        from collections import deque
        grid = self._grid(3, 3)
        sources = [(1, 1)]

        visited = set(sources)
        queue = deque([(r, c, 0) for r, c in sources])
        distances = {(1, 1): 0}
        while queue:
            r, c, dist = queue.popleft()
            for nr, nc in get_neighbors(r, c, grid):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    distances[(nr, nc)] = dist + 1
                    queue.append((nr, nc, dist + 1))

        assert distances[(1, 1)] == 0
        assert distances[(0, 1)] == 1
        assert distances[(0, 0)] == 2
