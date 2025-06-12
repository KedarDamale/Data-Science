# numpy_array_splitting_notes.py

"""
================================================================================
                      NumPy Array Splitting – In-Depth Guide
================================================================================

Splitting means breaking a large array into multiple **smaller sub-arrays**.

In NumPy, the core function for safe and flexible splitting is:
    ➤ np.array_split(array, num_splits[, axis])

Other specialized splitting functions:
    - np.split()      → Strict splitting (requires even splits only)
    - np.hsplit()     → Horizontal split (axis=1)
    - np.vsplit()     → Vertical split (axis=0)
    - np.dsplit()     → Depth split (axis=2 for 3D arrays)

================================================================================
1. Basic 1D Array Splitting using array_split()
================================================================================
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

split_3 = np.array_split(arr, 3)

print("\nSplit into 3 Parts:")
print(split_3[0])  # [1 2]
print(split_3[1])  # [3 4]
print(split_3[2])  # [5]

# ✅ array_split() returns a list of `ndarrays`
print(type(split_3))        # <class 'list'>
print(type(split_3[0]))     # <class 'numpy.ndarray'>

"""
🧠 Memory Insight:
- np.array_split() → Returns a Python list of numpy arrays.
- Each split is independent and can be modified separately.
"""

# --------------------------------------------------------------------------------
# 2. Irregular Split Handling
# --------------------------------------------------------------------------------

print("\nSplit 5 elements into 4 arrays:")
irregular_split = np.array_split(arr, 4)
for i, part in enumerate(irregular_split):
    print(f"Part {i+1}: {part}")

"""
Logic Behind Uneven Split:
--------------------------
Total elements = 5, splits = 4
→ First (5 % 4) = 1 splits get (5 // 4 + 1) = 2 elements
→ Remaining (3 splits) get 1 element each
→ Output: [1,2], [3], [4], [5]
"""
# --------------------------------------------------------------------------------
# 2.1 What Happens When Splits > Elements? (e.g., 3 elements → 4 splits)
# --------------------------------------------------------------------------------

print("\n--- Edge Case: Fewer Elements than Splits ---")
arr_small = np.array([10, 20, 30])
splits = np.array_split(arr_small, 4)

for i, s in enumerate(splits):
    print(f"Split {i+1}:", s)

"""
Explanation:
-------------
- We are trying to split 3 elements into 4 parts.
- Since we have **more splits than elements**, some resulting arrays will be empty.

Here's how NumPy handles it (via array_split):
- It tries to give at least one element per split, but that’s not always possible.
- Final output is a list of arrays like:
    [array([10]), array([20]), array([30]), array([])]

→ The last split has no data → it's an empty array: array([], dtype=int32)

✅ This behavior is *graceful* and avoids crashing. It’s why array_split() is preferred.

⚠ If you use np.split() instead of array_split() here, it will raise:
    ValueError: array split does not result in an equal division
"""

# --------------------------------------------------------------------------------
# 3. Strict Splitting with split() (fails if uneven)
# --------------------------------------------------------------------------------

"""
np.split() enforces **equal-size splits only**.
So, np.split([1,2,3,4,5], 3) → ❌ ValueError: can't split 5 into 3 equal parts.

Use split() only when you're absolutely sure the sizes divide evenly.
"""

# --------------------------------------------------------------------------------
# 4. Splitting a 2D Array
# --------------------------------------------------------------------------------

print("\n--- Splitting a 2D Array ---")

arr_2d = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

splits_2d = np.array_split(arr_2d, 3)

for i, s in enumerate(splits_2d):
    print(f"Block {i+1}:\n{s}")

"""
Each split is still a 2D array.
Dimensions are preserved unless forced to flatten.
"""

# --------------------------------------------------------------------------------
# 5. Splitting Over Axis (axis=1 → column-wise)
# --------------------------------------------------------------------------------

print("\n--- Column-wise Split (axis=1) ---")

arr_axis = np.array([
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

colwise_split = np.array_split(arr_axis, 3, axis=1)

for i, part in enumerate(colwise_split):
    print(f"Column Block {i+1}:\n{part}")

"""
Here:
- axis=1 → Split across columns (horizontal cut)
- Result = 3 sub-arrays, each containing a single column (but 6 rows)
"""

# --------------------------------------------------------------------------------
# 6. Specialized Functions: vsplit(), hsplit(), dsplit()
# --------------------------------------------------------------------------------

print("\n--- Using Specialized Split Functions ---")

# Vertical split → axis=0 → Split rows
vsplit_result = np.vsplit(arr_axis, 2)
print("\nVertical Split (2 row-wise chunks):")
for b in vsplit_result:
    print(b)

# Horizontal split → axis=1 → Split columns
hsplit_result = np.hsplit(arr_axis, 3)
print("\nHorizontal Split (3 column-wise chunks):")
for b in hsplit_result:
    print(b)

# NOTE: dsplit() works on 3D arrays (axis=2)
arr_3d = np.arange(27).reshape(3, 3, 3)
print("\nOriginal 3D Array Shape:", arr_3d.shape)

dsplit_result = np.dsplit(arr_3d, 3)
print("\nDepth Split on 3D Array:")
for i, slab in enumerate(dsplit_result):
    print(f"Slice {i+1}:\n{slab}")

# --------------------------------------------------------------------------------
# Summary Table for Quick Review
# --------------------------------------------------------------------------------

"""
| Function             | Axis         | Description                                      |
|----------------------|--------------|--------------------------------------------------|
| np.array_split()     | Any axis     | Safe splitting (adjusts size if uneven)          |
| np.split()           | Any axis     | Strict split (only works with exact division)    |
| np.hsplit()          | axis=1       | Splits columns (horizontal)                      |
| np.vsplit()          | axis=0       | Splits rows (vertical)                           |
| np.dsplit()          | axis=2       | Splits depth (for 3D arrays)                     |
"""

# --------------------------------------------------------------------------------
# Notes & Tips
# --------------------------------------------------------------------------------

"""
✔ Always use array_split() for safe operations.
✔******************************** Splitting 1D → returns 1D arrays, 2D → 2D arrays, nD → nD arrays.*****************************************
✔ Use len(result) to verify number of splits returned.
✔ Each split is an independent copy (or view, based on data).
✔ np.split() throws error if the shape doesn't divide evenly.
✔ Specialized split functions (vsplit/hsplit/dsplit) are semantically clearer.
"""
