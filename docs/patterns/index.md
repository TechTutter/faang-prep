# Patterns for Problem Solving

These are reusable techniques that map to broad categories of problems. Recognizing the pattern is half the solution.

## Two Pointers

Use when: sorted array, palindrome check, pair with target sum, container with most water.

Two pointers move toward each other (or in the same direction). Reduces O(n²) brute force to O(n).

```
lo, hi = 0, len(arr) - 1
while lo < hi:
    if condition: lo += 1
    else: hi -= 1
```

## Sliding Window

Use when: contiguous subarray/substring with a constraint (max sum, at most K distinct, etc.).

```
left = 0
for right in range(len(arr)):
    # expand window: include arr[right]
    while window_invalid():
        # shrink: remove arr[left]
        left += 1
    # window [left..right] is valid — update answer
```

## Prefix Sum

Pre-compute cumulative sums to answer range sum queries in O(1).

```
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]
# sum of arr[l..r] = prefix[r+1] - prefix[l]
```

## Fast & Slow Pointers

Use when: linked list cycle detection, finding middle of list, detecting duplicate in array.

Slow pointer moves 1 step, fast moves 2. If they meet → cycle exists.

## Divide & Conquer

Split problem into independent subproblems, solve recursively, combine. Examples: merge sort, binary search, closest pair of points.

## Backtracking Patterns

Use when: all combinations/permutations/subsets, N-queens, Sudoku. Template: choose → explore → unchoose.

## Heap / Top-K

Use `heapq` (min-heap) to maintain the K largest elements in a stream → O(n log k). For K smallest, use max-heap of size K.

## Intervals

Sort by start time. Common operations: merge overlapping, find insertion point, check overlap.

Overlap condition: `a.start <= b.end and b.start <= a.end`

## Dynamic Programming — Core Patterns

1. **Top-down (memoization)**: recursive + cache. Easy to write, harder on stack.
2. **Bottom-up (tabulation)**: fill a table iteratively. Better space, clearer transitions.

**Common DP signatures:**
- `dp[i]` = answer for first i elements
- `dp[i][j]` = answer for subproblem on [i..j] or with two variables
- `dp[i][w]` = knapsack style (item i, remaining capacity w)

Identify: **state** → **transition** → **base case** → **answer location**.
