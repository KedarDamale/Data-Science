# numpy_reshape_notes.py

"""
Reshaping Arrays in NumPy
==========================

Reshaping means changing the shape (structure) of an array without changing its data.

Key Points:
- The `.reshape()` function allows you to specify new dimensions.
- Total number of elements must remain the same.
- You can optionally leave one dimension as `-1` and NumPy will infer it.
- You can flatten multi-dimensional arrays back into 1D using `reshape(-1)`.
"""

import numpy as np

# -----------------------------------------------------------------------------
# 1. Original 1D array with 12 elements
# -----------------------------------------------------------------------------

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original Array (1D):\n", arr)

# -----------------------------------------------------------------------------
# 2. Reshaping to 2D (4 rows, 3 columns)
# -----------------------------------------------------------------------------

d2 = arr.reshape(4, 3)  # 4 rows × 3 columns = 12 elements
print("\nReshaped to 2D (4x3):\n", d2)

# -----------------------------------------------------------------------------
# 3. Reshaping to 3D (2 blocks, 3 rows, 2 columns)
# -----------------------------------------------------------------------------

d3 = arr.reshape(2, 3, 2)  # 2×3×2 = 12 elements
print("\nReshaped to 3D (2x3x2):\n", d3)

# -----------------------------------------------------------------------------
# 4. Invalid Reshape Examples (will raise ValueError)
# -----------------------------------------------------------------------------

"""
Example (commented out): Trying to reshape array of 8 elements into (3,3) is invalid.
→ 3x3 = 9 slots required, but only 8 elements present

arr_invalid = np.array([1,2,3,4,5,6,7,8])
invalid_reshape = arr_invalid.reshape(3, 3)  # ValueError
"""

"""
Another Example:
Trying to reshape 9 elements into (2,2) is invalid
→ 2x2 = 4 < 9, so overflow

ar = np.array([1,2,3,4,5,6,7,8,9])
bad_reshape = ar.reshape(2, 2)  # ValueError
"""

# -----------------------------------------------------------------------------
# 5. Unknown Dimension (-1) Example
# -----------------------------------------------------------------------------

print("\n--- Unknown Dimension Example ---")
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped_auto = a.reshape(3, -1)  # NumPy will auto-infer: 3×? = 9 → (3,3)
print(reshaped_auto)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Note: Only one dimension can be -1. If more than one is -1 → ValueError.

# -----------------------------------------------------------------------------
# 6. Flattening a Multi-dimensional Array to 1D
# -----------------------------------------------------------------------------

print("\n--- Flattening Array ---")
multi_arr = np.array([[2, 3, 4], [5, 6, 7]])
print("Original Dimensionality:", multi_arr.ndim)  # Output: 2

flat = multi_arr.reshape(-1)
print("Flattened Array:", flat)
print("New Dimensionality:", flat.ndim)  # Output: 1

# -----------------------------------------------------------------------------
# Summary Table
# -----------------------------------------------------------------------------

"""
| Operation          | Description                                      |
|--------------------|--------------------------------------------------|
| reshape(a, x, y)   | Reshapes to (x, y) if total elements match       |
| reshape(x, -1)     | Automatically infer dimension size               |
| reshape(-1)        | Flattens to 1D array                             |
| Invalid reshape    | If total elements don’t match shape → ValueError |
"""

# -----------------------------------------------------------------------------
# Note
# -----------------------------------------------------------------------------

"""
- Reshape does not modify the original array in-place.
- It returns a new view (if possible); otherwise, a copy.
- Flattening = 2D → 1D (or higher-D → 1D)
"""
