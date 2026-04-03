## Big-O Notation

Big-O describes the **upper bound** of an algorithm's growth rate as input size `n` grows. It ignores constants and lower-order terms — we care about asymptotic behavior.

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array index access, hash lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop over array |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive subsets |
| O(n!) | Factorial | Permutation generation |

## Space Complexity

Same notation, but measures **memory usage** relative to input size. Be explicit: does space grow with input? With recursion depth?

- In-place algorithms: O(1) space
- Recursion depth: each frame on the call stack counts

## Time vs Space Trade-off

Often you can trade one for the other. Example: caching results (memoization) costs O(n) space but can reduce time from O(2ⁿ) to O(n).

## Amortized Analysis

An operation that is occasionally expensive but **cheap on average** over a sequence of operations.

Example: dynamic array append is O(1) amortized — resizing happens once every n pushes, so the O(n) resize cost spreads to O(1) per operation.
