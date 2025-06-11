"""
NumPy Array Indexing - Complete Notes
======================================

Indexing allows access to individual elements or subsets of elements in NumPy arrays.
It works similarly to Python lists but supports efficient operations on multi-dimensional arrays.
"""

import numpy as np

# --------------------------
# 1. Indexing in 1D Arrays
# --------------------------

a = np.array([1, 2, 3, 4])

print("1D Array:", a)
print("a[2]:", a[2])  # Accessing the 3rd element → 3
print("a[2] + a[3]:", a[2] + a[3])  # 3 + 4 = 7

# --------------------------
# 2. Indexing in 2D Arrays
# --------------------------

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:\n", b)
print("b[1][2]:", b[1][2])    # Access row 1, column 2 → 6
print("b[1, 2]:", b[1, 2])    # Same as above (recommended syntax)

"""
Note:
- b[1][2] uses nested indexing like lists.
- b[1, 2] uses NumPy's preferred syntax which is more readable and optimized.
"""

# --------------------------
# 3. Indexing in 3D Arrays
# --------------------------

arr = np.array([
    [[1, 2, 3], [4, 5, 6]],       # arr[0]
    [[7, 8, 9], [10, 11, 12]]     # arr[1]
])

print("\n3D Array:\n", arr)
print("arr[0, 1, 2]:", arr[0, 1, 2])  
# arr[0] = [[1, 2, 3], [4, 5, 6]]
# arr[0, 1] = [4, 5, 6]
# arr[0, 1, 2] = 6

# --------------------------
# 4. Negative Indexing
# --------------------------

print("\nNegative Indexing:")
print("a[-1]:", a[-1])       # Last element in 1D array → 4
print("b[-1, -2]:", b[-1, -2])  # Second last element in last row of 2D array → 5
print("arr[-1, -1, -1]:", arr[-1, -1, -1])  # Last element in the 3D array → 12

"""
Negative indexing lets you access elements from the end:
- -1 means the last element
- -2 means the second-last element, and so on.
"""

