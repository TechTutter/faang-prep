How much time - or space - does this algorithm need to finish? To standardize the way we describe it, computer scientists invented the **big-O notation**. The big-O notation gives an upper bound of the complexity in the **worst** case, helping to quantify performance as the input size becomes **arbitrarily large**.

**Complexities ordered from smallest to largest**

_Given n - The size of the input_

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array index access, hash lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop over array |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Nested loops |
| O(n³) | Cubic | Triple nested loops |
| O(2ⁿ) | Exponential | Recursive subsets |
| O(n!) | Factorial | Permutation generation |


**Main big-O Properties are the following**

| Property | Simplification |
| -------- | -------------- |
| O(n+c) = O(n) | Drop constant additions |
| O(cn) = O(n), c>0 | Drop constant multiplications |

To compute the big-O complexity you can write a function f that describes the running time of that particular algorithm for an input of size n.

$f(n)=3n*(40+n^3)=120n+3n^4$
$O(f(n))=n^4$

Value assignments ( `x = 2` ) and basic operations ( `if`, `else`, etc. ) are not considered in the complexity analysis, but in general when there are nested loops you have to multiply their complexity, whilst if they are in the same “level” you have to sum them.
