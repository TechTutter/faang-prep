from collections import deque

# State = (node, extra_context) — must be hashable
def bfs_state(start, target, get_next_states):
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        state, steps = queue.popleft()
        if state == target: return steps
        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))
    return -1

# Word Ladder: generate neighbors on the fly — avoids O(N²·L) edge precomputation
def get_next_words(word, word_set):
    for i in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            candidate = word[:i] + c + word[i+1:]
            if candidate in word_set:
                yield candidate
