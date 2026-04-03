# Algorithms

## Searching

### Binary Search

Requires a **sorted** input. Halves the search space each iteration → O(log n).

The key insight: maintain `lo` and `hi` pointers. The loop invariant tells you where the answer must be. Memorize the three variants (exact, lower bound, upper bound).

[[binary-search.py]]

## Sorting

- **Merge Sort** — O(n log n) stable. Divide array in half, sort each half, merge. O(n) extra space.
- **Quick Sort** — O(n log n) average, O(n²) worst. In-place. Pivot selection matters (random pivot avoids worst case).
- **Heap Sort** — O(n log n) in-place. Not stable.
- For interviews: know that Python's sort is Timsort (O(n log n), stable). Know when to use `key=`.

## Recursion

Every recursive solution has: **base case** + **recursive case**. Identify the state at each level. Watch for stack overflow with large n — consider iterative + explicit stack.

## Backtracking

Explore all possibilities, abandon (backtrack) when a constraint is violated. Pattern:

```
def backtrack(state):
    if is_solution(state): record(); return
    for choice in get_choices(state):
        make_choice(choice)
        backtrack(state)
        undo_choice(choice)
```

## Greedy

Make the locally optimal choice at each step. Works when the problem has **greedy choice property** and **optimal substructure**. Common: interval scheduling, Huffman coding, Dijkstra.

## Dynamic Programming

See [Patterns → DP patterns](/docs/patterns).

## Graph Traversal

See [Data Structures → Graphs](/docs/data-structures).
