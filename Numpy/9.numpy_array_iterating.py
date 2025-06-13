# ============================================
#         NumPy Array Iteration – Deep Dive
# ============================================

import numpy as np

# --------------------------------------------
# WHY ITERATE OVER ARRAYS?
# --------------------------------------------
# ➤ Iteration = Visiting every element one-by-one.
# ➤ Useful when:
#     → You want to print or display every element.
#     → Apply a function to each value (e.g., square, filter).
#     → Analyze or transform values element-wise.
# ➤ While vectorized operations (like arr * 2) are preferred for speed,
#   iteration is necessary when operations are too complex or conditional.

# --------------------------------------------
# 1D ARRAY ITERATION (SIMPLE)
# --------------------------------------------

a = np.array([1, 2, 3, 4, 5, 6])

for i in a:
    print(i, end=" ")
print()

# ➤ 1D arrays behave like Python lists.
# ➤ Direct iteration gives each scalar element.
# ➤ Easy and readable – preferred for simple element access.

# --------------------------------------------
# 2D ARRAY ITERATION (NESTED)
# --------------------------------------------

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for row in b:          # row is a 1D array
    for col in row:    # col is a scalar element
        print(col, end=" ")
    print()

# ➤ A 2D array is an array of arrays.
# ➤ So outer loop iterates over rows (axis 0), inner loop over columns (axis 1).

# --------------------------------------------
# HIGHER-DIM ITERATION: np.nditer()
# --------------------------------------------

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Number of dimensions:", arr.ndim)  # Output: 3

for val in np.nditer(arr):
    print(val, end=" ")
print()

# ➤ `np.nditer()` flattens N-dimensional arrays for easy iteration.
# ➤ It’s especially useful when nesting loops would be hard to read or maintain.
# ➤ Internally, it’s an efficient iterator and respects memory layout.

# --------------------------------------------
# ITERATION WITH SLICING
# --------------------------------------------

# Select every second column in 2D sub-arrays (axis 1)
for val in np.nditer(arr[:, ::2]):
    print(val, end=" ")
print()

# ➤ arr[:, ::2] means:
#     - ":" = all outermost elements (axis=0),
#     - "::2" = step of 2 along columns (axis=1).
# ➤ Only the first and last columns are included.

# --------------------------------------------
# CHANGING DATA TYPES WHILE ITERATING
# --------------------------------------------

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x, end=" ")
print()

# ➤ op_dtypes=['S'] = treat elements as strings (e.g., b'1')
# ➤ buffered flag = ensures temporary safe conversion
# ➤ Useful when printing, saving, or type conversion is needed during iteration.

# --------------------------------------------
# ENUMERATING WITH INDEXES (Python enumerate)
# --------------------------------------------

arr = [23, 45, 67, 89]

for i, val in enumerate(arr):
    print(f"Index {i}: Value {val}", end=" ")
print()

# ➤ Standard Python `enumerate()` gives index + value.
# ➤ Works with lists or 1D arrays.

# --------------------------------------------
# ENUMERATION IN NUMPY: np.ndenumerate()
# --------------------------------------------

a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("Dimensions:", np.ndim(a))  # 3D array

for idx, val in np.ndenumerate(a):
    print(f"Index: {idx}, Value: {val}")
print()

# ➤ `np.ndenumerate()` = full version of enumerate for N-D arrays.
# ➤ Gives index as a tuple → e.g., (0, 1, 2)
# ➤ Useful for precise tracking of where each value is located in a multi-dimensional array.

"""
Understanding np.ndenumerate() with structure:

Index: (0, 0, 0), Value: 1  → 1st 2D array → 1st row → 1st column
Index: (0, 0, 1), Value: 2  → 1st 2D array → 1st row → 2nd column
...
Index: (1, 1, 2), Value: 6  → 2nd 2D array → 2nd row → 3rd column
"""

# --------------------------------------------
# BONUS: VECTORIZED LOOP AVOIDANCE
# --------------------------------------------

# ➤ Avoid loops when possible! NumPy allows vectorized operations for speed.
arr = np.array([1, 2, 3])
print(arr * 2)  # [2 4 6]

# ➤ Fast, efficient, and takes advantage of NumPy’s internal C-optimizations.

# --------------------------------------------
# COMMON ERRORS & WARNINGS
# --------------------------------------------

# Iterating over mismatched shape slices
try:
    a = np.array([[1, 2], [3, 4]])
    for val in np.nditer(a, flags=['buffered'], op_dtypes=['U']):  # U = Unicode string
        print(val, end=" ")
except Exception as e:
    print("Error:", e)

# ➤ Always ensure the dtype you're converting to is compatible with operation.

# =============================================
#       SUMMARY OF ITERATION METHODS
# =============================================

"""
Loop Types:

1. Regular `for` loop       → 1D or nested for N-D arrays
2. `np.nditer()`            → Flat iteration across all dimensions
3. `np.ndenumerate()`       → Flat iteration with index tracking
4. `enumerate()`            → Pythonic way for simple 1D loops
5. Vectorized ops (arr+1)   → Preferred for performance over manual looping
"""

# NumPy favors **vectorization** over **explicit iteration**
# But iteration is important when dealing with conditions, strings, or custom logic.

