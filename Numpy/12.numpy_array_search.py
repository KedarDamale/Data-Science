# numpy_searching_notes.py

"""
===============================================
Searching in NumPy Arrays – Detailed Explanation
===============================================

Searching is a fundamental operation where you want to:
- Find **where a value (or condition)** occurs in the array
- Retrieve the **index/indices** of those values
- Or figure out **where to insert** a value in a sorted array (binary search)

NumPy provides powerful tools for this:
1. np.where()          → Conditional matching, returns indices
2. np.searchsorted()   → Binary search for insertion index in sorted array
"""

import numpy as np

# ------------------------------------------------------------------------------
# 1. Standard Python Search (for comparison)
# ------------------------------------------------------------------------------

print("\n--- Native Python Search using .index() ---")

a = [1, 2, 3, 4, 5]
print("Index of 5:", a.index(5))  # Output: 4

# Why not use this in NumPy?
# - It returns only first match
# - Doesn't support vectorized conditions (e.g., find all even numbers)
# - Can't work efficiently on large, multi-dimensional data

# ------------------------------------------------------------------------------
# 2. NumPy where(): Search using conditions
# ------------------------------------------------------------------------------

print("\n--- np.where(): Searching with conditions ---")

arr = np.array([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5])

# Example 1: Find index of all values equal to 5
result = np.where(arr == 5)
print("Indices where arr == 5:", result)

"""
Output: (array([ 4,  5,  6,  7,  8,  9, 10, 11]),)

Why a tuple? Because:
- np.where() can return multiple arrays if used with 2D or 3D arrays
- For 1D arrays, it's just a single array inside the tuple

This result tells us: 5 is found at indexes 4 through 11
"""

# Example 2: Find indexes of even numbers
even_indices = np.where(arr % 2 == 0)
print("Indices of even numbers:", even_indices)

# Output: (array([1, 3], dtype=int64),)

# ------------------------------------------------------------------------------
# 3. np.where() with Multi-Dimensional Arrays
# ------------------------------------------------------------------------------

print("\n--- np.where() on 2D arrays ---")

arr2d = np.array([[10, 20, 30],
                  [15, 25, 35]])

idxs = np.where(arr2d > 20)
print("Indices where element > 20:", idxs)

"""
This gives:
(array([0, 1, 1]), array([2, 1, 2]))

Which means:
- Value 30 is at (0,2)
- Value 25 is at (1,1)
- Value 35 is at (1,2)
You can zip() these to get coordinates:
"""

coordinates = list(zip(*idxs))
print("Coordinates of elements > 20:", coordinates)

# ------------------------------------------------------------------------------
# 4. np.searchsorted(): Binary search for insertion
# ------------------------------------------------------------------------------

print("\n--- np.searchsorted(): Sorted insert location ---")

arr_sorted = np.array([6, 7, 8, 9])

# Find where value 7 should be inserted to maintain sort order
x = np.searchsorted(arr_sorted, 7)
print("Index to insert 7:", x)  # Output: 1 (between 6 and 7)

# Find insertion indexes for multiple values
vals = [2, 3, 34, 55]
x_multi = np.searchsorted(arr_sorted, vals)
print("Insertion indexes for [2, 3, 34, 55]:", x_multi)  # Output: [0 0 4 4]

"""
What it does:
-------------
- Uses **binary search** to find the index position at which the value(s) should be inserted
- Maintains the sorted order of the array

So here:
- 2 and 3 < 6 → insert at index 0
- 34 and 55 > 9 → insert at index 4 (end)
"""

# ------------------------------------------------------------------------------
# 5. Summary Table
# ------------------------------------------------------------------------------

"""
| Function             | Use Case                                         | Returns                              |
|----------------------|--------------------------------------------------|--------------------------------------|
| np.where(arr==val)   | Find positions where a condition is True         | Tuple of index arrays                |
| np.where(arr % 2==0) | Get even number indexes                          | Tuple with array of matching indices |
| np.searchsorted(x,v) | Get insert position to keep array sorted         | Index (or array of indexes)          |
"""

# ------------------------------------------------------------------------------
# 6. Edge Case – What if no match is found?
# ------------------------------------------------------------------------------

print("\n--- Edge Case: No match ---")

arr = np.array([1, 2, 3])
result = np.where(arr == 99)
print("Searching for 99:", result)  # Output: (array([], dtype=int64),)

# It returns an empty array, NOT an error

# ------------------------------------------------------------------------------
# 7. Optional: Specify side for insertion
# ------------------------------------------------------------------------------

print("\n--- searchsorted with side='right' ---")

arr_sorted = np.array([1, 3, 3, 3, 5])
x_left = np.searchsorted(arr_sorted, 3, side='left')   # Output: 1
x_right = np.searchsorted(arr_sorted, 3, side='right') # Output: 4

print(f"Left insert index for 3: {x_left}, Right insert index: {x_right}")

"""
Why useful?
-----------
- side='left': insert before all existing entries of 3
- side='right': insert after all existing entries of 3
"""

# ------------------------------------------------------------------------------
# Notes
# ------------------------------------------------------------------------------

"""
- np.where() is ideal when matching values or applying vectorized conditions
- np.searchsorted() is ideal when working with sorted arrays and you want insertion points

Both functions are optimized and very fast even on large arrays
"""
