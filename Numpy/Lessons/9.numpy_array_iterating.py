# NumPy Array Iteration – Detailed Notes and Explanations

import numpy as np

# WHY: Iteration is the process of visiting every element of an array.
# This is necessary when we want to apply some operation to each item, 
# such as printing, transforming, or conditional checking.

# --------------------------
# 1D Array Iteration
# --------------------------

a = np.array([1, 2, 3, 4, 5, 6])

for i in a:
    print(i, end=" ")
print()

# WHY: Simple for-loops work well on 1D arrays because there's only one level of elements to iterate over.

# --------------------------
# 2D Array Iteration
# --------------------------

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for row in b:
    for col in row:
        print(col, end=" ")
    print()

# WHY: With 2D arrays, each row is itself an array, so we need a nested loop.
# First loop gets each row (1D array), second loop gets each element in that row.

# --------------------------
# Higher-Dimensional Iteration using np.nditer()
# --------------------------

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Number of dimensions:", arr.ndim)  # 3

for val in np.nditer(arr):
    print(val, end=" ")
print()

# WHY: Iterating higher-dimensional arrays (like 3D or more) with nested loops becomes messy.
# np.nditer() simplifies this by abstracting away all dimensions into a single iterator.

# --------------------------
# Slicing + Iteration
# --------------------------

for val in np.nditer(arr[:, ::2]):
    print(val, end=" ")
print()

# WHY: Here, slicing selects only every 2nd column (axis 1), then np.nditer() iterates only over that selection.

# --------------------------
# Changing Data Type During Iteration using nditer
# --------------------------

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x, end=" ")
print()

# WHY: `op_dtypes=['S']` tells NumPy to treat each element as a string inside the loop.
# `flags=['buffered']` ensures that conversion happens safely in a temporary buffer.

# --------------------------
# Enumerating Indices and Elements using enumerate()
# --------------------------

arr = [23, 45, 67, 89]

for i, val in enumerate(arr):
    print(f"{i}: {val}", end=" ")
print()

# WHY: enumerate() is a Python feature that keeps track of index while iterating.
# Very useful when you need both value and its position.

# --------------------------
# Enumerating in NumPy using ndenumerate()
# --------------------------

a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("Dimensions:", np.ndim(a))

for idx, val in np.ndenumerate(a):
    print(f"Index:{idx}, Value:{val}")
print()

# WHY: np.ndenumerate() does the same job as enumerate(), but for N-dimensional NumPy arrays.
# Returns (index_tuple, value) for every scalar value, regardless of how deeply nested it is.=

"""
id:(0, 0, 0),element:1 #0th outermost array i.e 1st 2d array , 0th element in 2d arrays that is 1st id array and oth element in that 1d array i.r 1 , it return a tuple of indeices
id:(0, 0, 1),element:2
id:(0, 0, 2),element:3
id:(0, 1, 0),element:4
id:(0, 1, 1),element:5
id:(0, 1, 2),element:6
id:(1, 0, 0),element:1
id:(1, 0, 1),element:2
id:(1, 0, 2),element:3
id:(1, 1, 0),element:4
id:(1, 1, 1),element:5
id:(1, 1, 2),element:6
"""