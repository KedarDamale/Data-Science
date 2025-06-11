"""
NumPy Array Slicing - Complete Notes
=====================================

Slicing in NumPy allows extracting a subarray (a *view*, not a copy) using the format:
    array[start:end:step]

- `start`: Index to begin slice (inclusive).
- `end`: Index to stop slice (exclusive).
- `step`: Number of elements to skip (optional).
"""

import numpy as np

# -----------------------------------
# 1. Slicing in 1D Arrays
# -----------------------------------

arr_1d = np.array([1, 2, 3, 4, 5, 6, 7])

print("Original 1D Array:", arr_1d)

print("arr_1d[1:5]:", arr_1d[1:5])        # Elements from index 1 to 4 → [2 3 4 5]
print("arr_1d[1:5:2]:", arr_1d[1:5:2])    # Elements at index 1, 3 → [2 4]
print("arr_1d[:4]:", arr_1d[:4])          # Elements from start to index 3 → [1 2 3 4]
print("arr_1d[3:]:", arr_1d[3:])          # Elements from index 3 to end → [4 5 6 7]
print("arr_1d[::2]:", arr_1d[::2])        # Every 2nd element → [1 3 5 7]
print("arr_1d[::-1]:", arr_1d[::-1])      # Reverse array → [7 6 5 4 3 2 1]

# -----------------------------------
# 2. Slicing in 2D Arrays
# -----------------------------------

"""
Create a 2D array:
    Row 0 → [2, 3, 4, 5, 6, 7, 8, 9, 4, 2, 2, 4]
    Row 1 → [2,33, 4, 5, 6, 7, 8, 9, 4, 2, 2, 4]
"""

arr_2d = np.array([
    [2, 3, 4, 5, 6, 7, 8, 9, 4, 2, 2, 4],
    [2,33, 4, 5, 6, 7, 8, 9, 4, 2, 2, 4]
])

print("\nOriginal 2D Array:\n", arr_2d)

# Slice row 1 from column index 1 to 5 (i.e., elements 2 to 6)
print("arr_2d[1:, 1:6]:\n", arr_2d[1:, 1:6])  # Output: [[33  4  5  6  7]]

# Slice both rows, columns from index 1 to 5
print("arr_2d[0:, 1:6]:\n", arr_2d[0:, 1:6])  # Output:
# [[ 3  4  5  6  7]
#  [33  4  5  6  7]]

# Explanation:
# - First index slice selects rows
# - Second index slice selects columns within those rows

# -----------------------------------
# 3. General Notes on Slicing Syntax
# -----------------------------------

"""
Slice Patterns:

arr[start:]     → All elements from 'start' to end
arr[:end]       → All elements from beginning to 'end - 1'
arr[start:end]  → Elements from 'start' to 'end - 1'
arr[:]          → All elements (full array)
arr[::-1]       → Reversed array
arr[start:end:step] → Custom step slicing

2D array slicing:
    arr[row_start:row_end, col_start:col_end]
"""

