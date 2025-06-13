# numpy_sorting_notes.py

"""
==================================
Sorting in NumPy – Deep Explanation
==================================

Sorting means arranging the elements of an array in a defined order:
- **Ascending** (default)
- Can be used on numeric, string, or boolean arrays

NumPy provides the `.sort()` function:
- Works element-wise
- Returns a **sorted copy** of the array
- Original array remains unchanged (non in-place)

Function Signature:
-------------------
np.sort(array, axis=-1, kind=None)

Default behavior:
- Axis: -1 → last axis (innermost dimension)
- Kind: 'quicksort', 'mergesort', 'heapsort', 'stable' (defaults to quicksort)

🧠 Use `.sort()` instead of Python's `sorted()` because:
- `.sort()` supports multi-dimensional arrays
- Works on NumPy arrays (not plain Python lists)
- Much faster for large datasets
"""

import numpy as np

# ------------------------------------------------------------------------------
# 1. Sorting a 1D Numeric Array
# ------------------------------------------------------------------------------

print("\n--- Sorting a Numeric 1D Array ---")

arr = np.array([3, 2, 0, 1])
sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)  # Output: [0 1 2 3]

# ------------------------------------------------------------------------------
# 2. Sorting a 1D String Array (Alphabetical)
# ------------------------------------------------------------------------------

print("\n--- Sorting a String Array Alphabetically ---")

arr = np.array(['banana', 'cherry', 'apple'])
sorted_arr = np.sort(arr)
print("Sorted string array:", sorted_arr)  # Output: ['apple' 'banana' 'cherry']

"""
Strings are sorted lexicographically (dictionary order):
- Based on Unicode code points
- Case-sensitive by default (capital letters come before lowercase)
"""

# ------------------------------------------------------------------------------
# 3. Sorting a Boolean Array
# ------------------------------------------------------------------------------

print("\n--- Sorting a Boolean Array ---")

arr = np.array([True, False, True])
sorted_arr = np.sort(arr)
print("Sorted boolean array:", sorted_arr)  # Output: [False  True  True]

"""
Why? Because:
- False = 0
- True = 1
→ Hence sorted like [0, 1, 1]
"""

# ------------------------------------------------------------------------------
# 4. Sorting a 2D Array
# ------------------------------------------------------------------------------

print("\n--- Sorting a 2D Array ---")

arr = np.array([[3, 2, 4],
                [5, 0, 1]])

sorted_2d = np.sort(arr)
print("Sorted 2D array:\n", sorted_2d)

"""
Output:
[[2 3 4]
 [0 1 5]]

Explanation:
- NumPy sorts each row independently (axis = -1 by default = columns within each row)
- Does not sort entire matrix as a flat 1D structure

To sort across rows instead of columns, explicitly use `axis=0`
"""

# ------------------------------------------------------------------------------
# 5. Sorting by Axis (Row-wise or Column-wise)
# ------------------------------------------------------------------------------

print("\n--- Axis-Based Sorting ---")

arr = np.array([[5, 1, 7],
                [2, 9, 4]])

# Sort column-wise (axis=0)
sorted_axis0 = np.sort(arr, axis=0)
print("Sorted column-wise:\n", sorted_axis0)

# Sort row-wise (axis=1)
sorted_axis1 = np.sort(arr, axis=1)
print("Sorted row-wise:\n", sorted_axis1)

"""
axis=0 → sort each column → elements in each vertical slice sorted independently
axis=1 → sort each row    → elements in each row sorted independently
"""

# ------------------------------------------------------------------------------
# 6. Advanced Sorting with Kind (Algorithm Control)
# ------------------------------------------------------------------------------

print("\n--- Using Different Sort Algorithms ---")

arr = np.array([3, 1, 2])

# Stable sort: maintains the order of equal elements
stable_sort = np.sort(arr, kind='stable')
print("Stable Sort:", stable_sort)

"""
Sorting Algorithms:
-------------------
- 'quicksort' : Default, fast but not stable
- 'mergesort' : Stable, good for sorting complex objects
- 'heapsort'  : Less commonly used
- 'stable'    : Stable sort, typically uses timsort (like Python)

Use 'stable' when relative order matters, especially in structured arrays
"""

# ------------------------------------------------------------------------------
# 7. Summary Table
# ------------------------------------------------------------------------------

"""
| Operation                  | Description                                  |
|---------------------------|----------------------------------------------|
| np.sort(arr)              | Sorts array along last axis                  |
| np.sort(arr, axis=0)      | Sorts along columns (row-wise comparison)    |
| np.sort(arr, axis=1)      | Sorts along rows (column-wise comparison)    |
| np.sort(arr, kind='stable')| Use stable sort (preserves equal order)     |
| Sorting Strings            | Sorted lexicographically (dictionary order) |
| Sorting Booleans           | False (0) comes before True (1)             |
"""

# ------------------------------------------------------------------------------
# Notes
# ------------------------------------------------------------------------------

"""
- np.sort() returns a **new array** – it does not change the original array
- For in-place sorting, use `arr.sort()` (only for 1D/row-wise)
- Works on nD arrays, sorting happens along axis you specify
- Not suitable for sorting with custom keys – use structured arrays or pandas for that
"""
