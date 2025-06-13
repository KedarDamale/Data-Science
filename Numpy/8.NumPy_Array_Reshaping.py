# numpy_reshape_notes.py

"""
================================================================================
                   NumPy Array Reshaping – Deep Dive
================================================================================

Reshaping is the process of changing the **structure** (shape) of an array 
**without altering its data or content**.

================================================================================
Why Reshaping is Useful:
------------------------
✔ Converts flat arrays into structured matrices for ML, image processing, etc.
✔ Prepares data for matrix operations (e.g., dot product, broadcasting).
✔ Allows flattening for serialization, storage, or ML model input.
✔ Enables slicing and advanced indexing after shape adjustment.

================================================================================
Important Rules:
----------------
- The **total number of elements must remain constant** during reshape.
- Shape mismatch leads to `ValueError`.
- You can use `-1` for one dimension – NumPy auto-computes its size.
- Reshape tries to return a **view** (no data copied), but may return a copy.

================================================================================
"""

import numpy as np

# -----------------------------------------------------------------------------
# 1. Original 1D array with 12 elements
# -----------------------------------------------------------------------------

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original Array (1D):\n", arr)
print("Shape:", arr.shape)  # (12,)
print("Dimensionality:", arr.ndim)  # 1

# -----------------------------------------------------------------------------
# 2. Reshaping to 2D (4 rows, 3 columns)
# -----------------------------------------------------------------------------

d2 = arr.reshape(4, 3)  # 4 × 3 = 12 elements → valid
print("\nReshaped to 2D (4x3):\n", d2)
print("Shape:", d2.shape)  # (4, 3)
print("Dimensions:", d2.ndim)  # 2

# -----------------------------------------------------------------------------
# 3. Reshaping to 3D (2 blocks, 3 rows, 2 columns)
# -----------------------------------------------------------------------------

d3 = arr.reshape(2, 3, 2)  # 2 × 3 × 2 = 12 → valid
print("\nReshaped to 3D (2x3x2):\n", d3)
print("Shape:", d3.shape)
print("Dimensions:", d3.ndim)  # 3

# -----------------------------------------------------------------------------
# 4. Invalid Reshape Examples (These will raise ValueError)
# -----------------------------------------------------------------------------

"""
❌ Example 1:
Trying to reshape array of 8 elements into (3,3) → INVALID
arr_invalid = np.array([1,2,3,4,5,6,7,8])
invalid_reshape = arr_invalid.reshape(3, 3)  # ValueError → 3×3 = 9 ≠ 8

❌ Example 2:
Reshaping 9 elements into (2,2) → INVALID
ar = np.array([1,2,3,4,5,6,7,8,9])
bad_reshape = ar.reshape(2, 2)  # ValueError → 2×2 = 4 ≠ 9
"""

# -----------------------------------------------------------------------------
# 5. Unknown Dimension (-1) Example
# -----------------------------------------------------------------------------

print("\n--- Unknown Dimension (-1) Example ---")
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped_auto = a.reshape(3, -1)  # NumPy calculates 9 ÷ 3 = 3 → shape becomes (3,3)
print(reshaped_auto)

# ✔️ Auto-calculation: One `-1` is allowed per reshape
# ❌ Multiple `-1`s = ambiguous → ValueError
"""
Ex: a.reshape(-1, -1) → ValueError: can only specify one unknown dimension
"""

# -----------------------------------------------------------------------------
# 6. Flattening a Multi-dimensional Array to 1D
# -----------------------------------------------------------------------------

print("\n--- Flattening Multi-Dimensional Array to 1D ---")
multi_arr = np.array([[2, 3, 4], [5, 6, 7]])
print("Original Array:\n", multi_arr)
print("Original Shape:", multi_arr.shape)
print("Original Dimensionality:", multi_arr.ndim)

flat = multi_arr.reshape(-1)
print("Flattened Array:", flat)
print("New Dimensionality:", flat.ndim)  # 1

# NOTE:
# - `.reshape(-1)` = quick way to flatten ANY array, regardless of dimension
# - Alternative: `.flatten()` → Always returns a copy, `.ravel()` → returns a view if possible

# -----------------------------------------------------------------------------
# 7. Memory Behavior of reshape()
# -----------------------------------------------------------------------------

print("\n--- Reshape Memory Behavior (View vs Copy) ---")
original = np.array([1, 2, 3, 4, 5, 6])
reshaped = original.reshape(2, 3)

# Let's mutate reshaped and see if it affects original
reshaped[0, 0] = 99
print("Original after modification:\n", original)
# ➤ If memory layout allows, reshape gives a view → both reflect changes
# ➤ If not, a copy is made → changes won't affect the original

# To check if they share memory:
print("Shares memory:", np.shares_memory(original, reshaped))  # True or False

# -----------------------------------------------------------------------------
# Summary Table (for quick revision)
# -----------------------------------------------------------------------------

"""
| Operation                | Purpose                                        | Notes                             |
|--------------------------|------------------------------------------------|-----------------------------------|
| reshape(a, x, y)         | Reshape to 2D                                  | x*y must equal total elements     |
| reshape(x, y, z)         | Reshape to 3D                                  | x*y*z must equal total elements   |
| reshape(x, -1)           | Auto-compute second dimension                  | Only one -1 allowed               |
| reshape(-1)              | Flatten to 1D                                  | Shortcut                          |
| flatten()                | 1D copy                                        | Always returns new array          |
| ravel()                  | 1D view                                        | View if possible, else copy       |
| invalid reshape          | Shape mismatch throws ValueError               | Must match element count          |
"""

# -----------------------------------------------------------------------------
# Additional Notes
# -----------------------------------------------------------------------------

"""
✔ `.reshape()` is **non-destructive** – original array stays intact unless view is edited.
✔ Very useful in data preprocessing pipelines (especially with ML models).
✔ Memory layout (C-style vs Fortran-style) affects view vs copy behavior.
✔ For advanced reshaping, NumPy also provides `.swapaxes()`, `.transpose()`, etc.
"""
