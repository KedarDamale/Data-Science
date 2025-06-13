# =======================================
#           JOINING NUMPY ARRAYS
# =======================================

# In normal Python (without NumPy), we work with lists
a = [1, 2, 3]
b = [2, 3, 4]

print(a + b)
# Output: [1, 2, 3, 2, 3, 4]
# ➤ In pure Python, using the + operator on lists performs *concatenation* (joins them end-to-end).
# ➤ This is because lists are not mathematical arrays, but containers of elements.

# =======================================
#           ENTER NUMPY ARRAYS
# =======================================

import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

print(a + b)
# Output: [3 5 7]
# ➤ In NumPy, the + operator performs **element-wise addition**, not concatenation.
# ➤ NumPy arrays are numerical data structures, designed to behave like mathematical vectors/matrices.
# ➤ So `a + b` adds corresponding elements: [1+2, 2+3, 3+4] = [3 5 7]

# =======================================
#       CONCATENATION USING NumPy
# =======================================

# To actually **join** arrays in NumPy like we do with lists, we use:
# ➤ `np.concatenate()`

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

print(np.concatenate((a, b)))
# Output: [1 2 3 2 3 4]
# ➤ concatenate() takes a **tuple of arrays**, so we pass (a, b)
# ➤ If `axis` is not specified, it defaults to `axis=0` (1D here, so it's fine)

# =======================================
#         CONCATENATING 2D ARRAYS
# =======================================

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# axis=0 → concatenate rows (row-wise stacking)
print(np.concatenate((arr1, arr2), axis=0))
"""
Output:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
➤ Rows from arr2 are appended below rows of arr1.
"""

# axis=1 → concatenate columns (column-wise stacking)
print(np.concatenate((arr1, arr2), axis=1))
"""
Output:
[[1 2 5 6]
 [3 4 7 8]]
➤ Columns from arr2 are appended to the right of arr1.
"""

# NOTE:
# ➤ axis=0 means: Stack arrays vertically (add more rows)
# ➤ axis=1 means: Stack arrays horizontally (add more columns)
# ➤ Think of axis=0 as row dimension (axis along down), and axis=1 as column dimension (axis along right)

# =======================================
#        DIFFERENCE: STACK vs CONCAT
# =======================================

# ➤ `np.stack()` is **similar** to concatenate but it introduces a **new dimension**
# ➤ Useful when you want to combine arrays and preserve structure in higher dimensions

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stack along new axis=1 (second dimension)
print(np.stack((arr1, arr2), axis=1))
"""
Output:
[[1 4]
 [2 5]
 [3 6]]
Explanation:
- arr1 = [1, 2, 3]
- arr2 = [4, 5, 6]
- stacked along axis=1 means each pair of elements becomes a row: [[1,4], [2,5], [3,6]]
"""

# Stack along new axis=0 (first dimension)
print(np.stack((arr1, arr2), axis=0))
"""
Output:
[[1 2 3]
 [4 5 6]]
➤ Adds a new 0th axis and stacks both arrays on top of each other
"""

# =======================================
#   SPECIAL STACKING FUNCTIONS IN NUMPY
# =======================================

# 1. Horizontal Stack (hstack)
print(np.hstack((arr1, arr2)))
"""
Output: [1 2 3 4 5 6]
➤ hstack stacks in a single row (axis=1 for 2D), flattens into a horizontal sequence
"""

# 2. Vertical Stack (vstack)
print(np.vstack((arr1, arr2)))
"""
Output:
[[1 2 3]
 [4 5 6]]
➤ vstack stacks arrays row-wise (axis=0 for 2D) like adding more rows
"""

# 3. Depth Stack (dstack)
print(np.dstack((arr1, arr2)))
"""
Output:
[[[1 4]
  [2 5]
  [3 6]]]
➤ dstack stacks arrays along a third dimension (depth), adds depth to the structure
"""

# =======================================
#          VISUALIZING AXES
# =======================================
# For 2D arrays:
# ➤ axis=0 → down (rows)
# ➤ axis=1 → right (columns)

# For 3D arrays:
# ➤ axis=2 → depth (layers)

# =======================================
#       BONUS: r_, c_, and column_stack
# =======================================

# np.r_ is a convenient row-wise concatenation shortcut:
print(np.r_[arr1, arr2])
# Same as: np.concatenate((arr1, arr2))

# np.c_ stacks 1D arrays as columns:
print(np.c_[arr1, arr2])
"""
Output:
[[1 4]
 [2 5]
 [3 6]]
➤ Similar to stack with axis=1
"""

# np.column_stack() is also useful for column-wise stacking of 1D arrays:
print(np.column_stack((arr1, arr2)))
"""
Output:
[[1 4]
 [2 5]
 [3 6]]
"""

# =======================================
#       COMMON ERROR HANDLING
# =======================================
# Mismatched shapes will raise ValueErrors during concatenation/stacking:
try:
    np.concatenate(([1, 2], [3, 4, 5]))
except Exception as e:
    print("Error:", e)
# Output: all input arrays must have the same shape, except in the concatenation axis

