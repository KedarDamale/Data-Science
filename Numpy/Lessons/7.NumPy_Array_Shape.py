# numpy_shape_notes.py

"""
Understanding NumPy Array Shape
===============================

The `.shape` attribute in NumPy returns a tuple that describes the number of elements 
along each dimension (axis) of the array.

Each element in the tuple represents the size along that specific axis.

This is fundamental when working with multidimensional data in NumPy.
"""

import numpy as np

# ------------------------------------------------------
# 1. 2D Array Example
# ------------------------------------------------------

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("2D Array:\n", arr_2d)
print("Shape:", arr_2d.shape)  # Output: (2, 4)
# → This means: 2 rows, 4 columns (2 elements in 1st dim, 4 in 2nd dim)

# ------------------------------------------------------
# 2. 1D Array Example
# ------------------------------------------------------

arr_1d = np.array([1, 2, 3, 4])
print("\n1D Array:\n", arr_1d)
print("Shape:", arr_1d.shape)  # Output: (4,)
# → This is a flat array with 4 elements on one axis (1D)

# ------------------------------------------------------
# 3. 5D Array using ndmin
# ------------------------------------------------------

arr_5d = np.array([1, 2, 3, 4], ndmin=5)
print("\n5D Array (created with ndmin=5):\n", arr_5d)
print("Shape:", arr_5d.shape)  # Output: (1, 1, 1, 1, 4)
# → This means:
#    - First 4 dimensions have only 1 element (nesting layers)
#    - The 5th dimension contains the actual 4 data values
# → Visual representation: [[[[[1, 2, 3, 4]]]]]

# ------------------------------------------------------
# Summary of Shape and Dimensions
# ------------------------------------------------------

"""
| Array Type     | Example Code                             | Shape         | Interpretation                 |
|----------------|-------------------------------------------|----------------|----------------------------------|
| 1D array       | np.array([1, 2, 3])                       | (3,)           | 3 elements in 1 axis            |
| 2D array       | np.array([[1,2,3],[4,5,6]])              | (2, 3)         | 2 rows, 3 columns               |
| 3D array       | np.array([[[1, 2], [3, 4]]])             | (1, 2, 2)      | 1 block, 2 rows, 2 columns      |
| 5D array       | np.array([1,2,3,4], ndmin=5)             | (1, 1, 1, 1, 4)| 5D nesting, values at innermost|

Use `.shape` for understanding layout and structure of array,
and `.ndim` to know how many dimensions it has.
"""

# Check number of dimensions (extra info)
print("\nNumber of dimensions in 5D array:", arr_5d.ndim)  # Output: 5
