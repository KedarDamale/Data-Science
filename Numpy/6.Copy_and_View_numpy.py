"""
Copy vs View in NumPy – Detailed Explanation with Examples
==========================================================

When working with NumPy arrays, it's essential to understand the **difference between a copy and a view**:

1. **Copy**:
   - Completely independent array
   - Allocated new memory (owns its data)
   - Changes in the copy DO NOT affect the original array, and vice versa
   - Created using `copy()` method

2. **View**:
   - A shallow replica (shares memory with original array) A view shares the same underlying data buffer in memory as the original array 
   — but it is a separate Python object. means its id() will be different
   - Does NOT own its data
   - Changes in either array AFFECT both
   - Created using `view()` method
"""

import numpy as np

# -----------------------------------------------------------------------------
# Example 1: Using copy() – changes do not reflect in original
# -----------------------------------------------------------------------------

print("\n--- COPY EXAMPLE ---")
arr1 = np.array([1, 2, 3, 4, 5])
copy_arr = arr1.copy()

arr1[0] = 99

print("Original array:", arr1)      # [99  2  3  4  5]
print("Copy of array:", copy_arr)   # [1  2  3  4  5]
print("Are they the same object in memory?", id(arr1) == id(copy_arr))  # False

# -----------------------------------------------------------------------------
# Example 2: Using view() – changes reflect in both
# -----------------------------------------------------------------------------

print("\n--- VIEW EXAMPLE ---")
arr2 = np.array([10, 20, 30, 40, 50])
view_arr = arr2.view()

arr2[1] = 222

print("Original array:", arr2)      # [10 222 30 40 50]
print("View of array:", view_arr)   # [10 222 30 40 50]
print("Are they the same object in memory?", id(arr2) == id(view_arr))  # False
print(f"arr2 memory id: {id(arr2)}")
print(f"view_arr memory id: {id(view_arr)}")

# -----------------------------------------------------------------------------
# Example 3: Ownership – checking using `.base` attribute
# -----------------------------------------------------------------------------

print("\n--- OWNERSHIP TEST ---")

original = np.array([7, 8, 9])

copy_obj = original.copy()
view_obj = original.view()

# .base tells whether an array is a view of another
print("copy_obj.base:", copy_obj.base)  # None (owns its data)
print("view_obj.base:", view_obj.base)  # original array (doesn't own data)

# -----------------------------------------------------------------------------
# Bonus: Modifying the view affects the original, and vice versa
# -----------------------------------------------------------------------------

print("\n--- MUTUAL MODIFICATION (VIEW) ---")

original2 = np.array([100, 200, 300])
linked_view = original2.view()

linked_view[0] = -1
print("Original array after modifying view:", original2)   # [-1 200 300]

original2[1] = -2
print("View array after modifying original:", linked_view) # [-1 -2 300]

# -----------------------------------------------------------------------------
# Summary Table:
# -----------------------------------------------------------------------------

"""
| Operation     | Independent? | Shares Memory? | Changes Propagate? |
|---------------|--------------|----------------|---------------------|
| copy()        | Yes          | No             | No                  |
| view()        | No           | Yes            | Yes                 |
"""

# -----------------------------------------------------------------------------
# Important Notes:
# -----------------------------------------------------------------------------
# - `copy()` is deep: memory is fully cloned.
# - `view()` is shallow: data buffer is shared.
# - `x.base is None` → x owns its data
# - `x.base is not None` → x is a view into another array

# Use copy() when:
# - You want to preserve original data
# - You want to perform independent processing
# Use view() when:
# - You want memory efficiency
# - You want to reflect changes across arrays

"""
| Concept               | `copy()`                  | `view()`                        |
| --------------------- | ------------------------- | ------------------------------- |
| Owns its memory?      | ✅ Yes                     | ❌ No                            |
| Shares memory?        | ❌ No (has its own buffer) | ✅ Yes (same buffer as original) |
| Data change reflects? | ❌ No                      | ✅ Yes                           |
| `id()`                | Different from original   | Different from original         |
| `.base` attribute     | `None`                    | Reference to original array     |

"""