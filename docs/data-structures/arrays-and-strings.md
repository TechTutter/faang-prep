## Arrays

Contiguous block of memory. Fixed-size in most low-level languages; dynamic arrays (Python list, Java ArrayList) resize automatically.

**Key operations:**
| Operation | Time |
|-----------|------|
| Access by index | O(1) |
| Search (unsorted) | O(n) |
| Search (sorted) | O(log n) |
| Insert/delete at end | O(1) amortized |
| Insert/delete at middle | O(n) |

**Common patterns:** two pointers, sliding window, prefix sums.

## Strings

In most languages, strings are immutable arrays of characters. Watch out for:

- **Concatenation in a loop** → O(n²) if language creates a new string each time. Use a buffer/list and join at the end → O(n).
- **Character frequency** → `Counter` or `dict` in O(n) time, O(1) space (bounded alphabet).

## Key Tricks

- Sort first to simplify comparisons (`O(n log n)` often acceptable)
- Use a hash map to trade space for time on lookup problems
- Two-pointer technique for sorted arrays to avoid O(n²) nested loops
