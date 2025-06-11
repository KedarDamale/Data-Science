"""
NumPy Arrays: Core Concept of Numerical Computing
==================================================

Arrays in NumPy are the fundamental data structure that allow:
- Efficient storage
- Fast computation
- High-dimensional data representation
"""

# ------------------------------------------------
# Getting Started with NumPy
# ------------------------------------------------

# Importing NumPy module
import numpy as np  # 'np' is a common alias; you can use any name

# Check NumPy version
print("NumPy Version:", np.__version__)

# ------------------------------------------------
# Creating NumPy Arrays (ndarray)
# ------------------------------------------------

# The array object in NumPy is called: ndarray (n-dimensional array)
a = np.array([1, 2, 3])
print("Array a:", a)           # Output: [1 2 3] → No commas
print("Type:", type(a))        # <class 'numpy.ndarray'>

"""
Notice: Output is space-separated because NumPy prints compactly for performance and visualization.
This also indicates the elements are stored in a contiguous memory block (not as individual Python objects).
"""

# You can create ndarray from:
a_list = np.array([1, 2, 3])           # From list
a_tuple = np.array((1, 2, 3))          # From tuple

# ------------------------------------------------
# Comparison: Python List vs NumPy Array
# ------------------------------------------------

"""
| Feature               | Python List                | NumPy Array                     |
|----------------------|----------------------------|----------------------------------|
| Data Type            | Can be mixed               | Homogeneous (one data type)     |
| Speed                | Slower                     | Faster (C-optimized)            |
| Memory               | Scattered (pointers)       | Contiguous                      |
| Operations           | Manual loops required      | Vectorized (element-wise ops)   |
| Broadcasting         | Not supported              | Supported                       |
| Multi-dimensional    | Difficult to manage        | Easy with .ndim and .shape      |
| Library Support      | Not used in SciPy stack    | Base of scientific Python stack |
"""

# ------------------------------------------------
# Array Dimensions
# ------------------------------------------------

"""
Each dimension in an array represents a level of nesting:

0D → Scalar (single number)
1D → Vector (line of elements)
2D → Matrix (table)
3D+ → Tensor (data cube, or higher)

A dimension = level of array nesting
"""

# 0D array (Scalar)
d0 = np.array(43)
print("0D array:", d0)
print("d0.ndim:", d0.ndim)

# 1D array (Vector)
d1 = np.array([43, 45, 62])
print("1D array:", d1)
print("d1.ndim:", d1.ndim)

# 2D array (Matrix)
d2 = np.array([
    [12, 23, 45, 12],
    [12, 34, 23, 12],
    [12, 34, 23, 12]
])
print("2D array:\n", d2)
print("d2.ndim:", d2.ndim)

# 3D array (Tensor)
"""
Visualize as:
[
  [ [1,2,3], [4,5,6] ],
  [ [1,2,3], [4,5,6] ]
]

It is 3D because:
- Contains 2 blocks
- Each block has 2 rows
- Each row has 3 columns
"""
d3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])
print("3D array:\n", d3)
print("d3.ndim:", d3.ndim)#ndim method returns the number of dimensions in that array

# Beyond 3D → Human imagination breaks, but machine doesn't!
d5 = np.array([1, 2, 3, 4], ndmin=5)#ndim as an argument used to define the number of dimensions in an array
print("Array with ndmin=5:\n", d5)
print("d5.ndim:", d5.ndim)

"""
ndmin forces NumPy to create a minimum of n dimensions, wrapping the array until the required depth is achieved.

You can think of it as putting the array in n-1 additional layers of brackets ([]), one for each dimension.


What ndim is doing that we are supplying it with a 1d array i.e [1,2,3,4] it is just creating nestings around 1d array till it reaches 5 dimensions 
np.array([1, 2, 3, 4])                   # ndim = 1, shape = (4,)
np.array([[1, 2, 3, 4]])                 # ndim = 2, shape = (1, 4)
np.array([[[1, 2, 3, 4]]])               # ndim = 3, shape = (1, 1, 4)
np.array([[[[1, 2, 3, 4]]]])             # ndim = 4, shape = (1, 1, 1, 4)
np.array([[[[[1, 2, 3, 4]]]]])           # ndim = 5, shape = (1, 1, 1, 1, 4)

Shape is a tuple where each entry represents the number of elements along a specific axis, starting from the outermost dimension.

arr = np.array([[[[[1, 2, 3, 4]]]]])
print(arr.shape)  # Output: (1, 1, 1, 1, 4)

Meaning:

Axis 0: 1 item → a 4D array

Axis 1: 1 item → a 3D array

Axis 2: 1 item → a 2D array

Axis 3: 1 item → a 1D array

Axis 4: 4 items → actual scalar values: 1, 2, 3, 4


"""
# 📌 Summary:

# | Term      | Meaning                                                         |
# | --------- | --------------------------------------------------------------- |
# | `ndim`    | Number of dimensions (or depth of nesting)                      |
# | `shape`   | Tuple showing size along each axis                              |
# | `ndmin`   | Minimum number of dimensions to enforce when creating the array |
# | `ndarray` | Core NumPy object that supports N-dimensional arrays            |

