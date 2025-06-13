# numpy_filtering_notes.py

"""
==============================
Filtering Arrays in NumPy 🧪🔍
==============================

✅ Definition:
Filtering means **extracting a subset** of elements from an existing array based on **certain conditions**.

In NumPy, filtering is **boolean indexing**:
- You provide a boolean array (same length as input array).
- Where the value is `True`, the element is included.
- Where the value is `False`, the element is excluded.

This is a very powerful method to **select values that satisfy a condition** or a combination of conditions (like all even numbers, values > 30, etc).

"""

import numpy as np

# ------------------------------------------------------------------------------
# 1. Manual Boolean Filtering (Boolean Mask)
# ------------------------------------------------------------------------------

print("\n--- Basic Filtering with Manual Boolean Mask ---")

arr = np.array([41, 42, 43, 44])
mask = [True, False, True, False]

filtered = arr[mask]  # Picks index 0 and 2
print("Filtered manually with boolean list:", filtered)  # Output: [41 43]

"""
Note:
- The mask must be the same length as the array.
- If not, you will get a ValueError.
- This is how filtering works at the lowest level.
"""

# ------------------------------------------------------------------------------
# 2. Filtering Using a Loop (Manual Boolean Construction)
# ------------------------------------------------------------------------------

print("\n--- Filtering Even Numbers with Loop ---")

arr = np.array([22, 34, 55, 78, 98, 79, 57, 21, 14, 25, 39])
bool_mask = []

for i in np.nditer(arr):
    if i % 2 == 0:
        bool_mask.append(True)
    else:
        bool_mask.append(False)

print("Boolean mask:", bool_mask)
print("Filtered even numbers:", arr[bool_mask])  # Output: [22 34 78 98 14]

"""
- You build a boolean mask using a loop
- Then apply that mask to the array
- This is a slower method but useful to understand what's going on under the hood
"""

# ------------------------------------------------------------------------------
# 3. Filtering Using NumPy Condition (Vectorized)
# ------------------------------------------------------------------------------

print("\n--- Filtering Using NumPy Conditions ---")

arr = np.array([41, 42, 43, 44])

condition = arr > 42  # You can replace this with any logical condition
print("Condition result (boolean mask):", condition)  # [False False  True  True]

filtered_arr = arr[condition]
print("Filtered result:", filtered_arr)  # [43 44]

"""
✔️ This is the preferred method — vectorized (no loop needed).
✔️ Very fast — uses NumPy's internal optimized C loops.
✔️ Highly readable and expressive.

You can use all standard comparison operators:
    ==   !=   >   <   >=   <=

And also combine them:
    arr[(arr > 10) & (arr < 50)]   ← AND condition
    arr[(arr < 20) | (arr > 80)]   ← OR condition
    ~condition                     ← NOT
"""

# ------------------------------------------------------------------------------
# 4. Summary Table
# ------------------------------------------------------------------------------

"""
| Technique                       | Description                                     |
|---------------------------------|-------------------------------------------------|
| arr[boolean_list]              | Manual filtering using predefined mask          |
| arr[condition]                 | Fast vectorized filtering                       |
| np.nditer + loop               | Slow, manual way to construct a filter          |
| Multiple conditions            | Combine using &, |, ~ with parentheses          |
"""

# ------------------------------------------------------------------------------
# 5. Notes
# ------------------------------------------------------------------------------

"""
- The boolean mask must match the shape of the array being filtered.
- Broadcasting rules apply for more complex cases (like multidimensional filters).
- This technique is used heavily in data preprocessing, ML pipelines, etc.
- Advanced filtering can use np.where() or np.extract() for conditional control.

Examples:
----------
1. arr[arr % 2 == 0]         → Filter all even numbers
2. arr[arr > 50]             → Filter all numbers greater than 50
3. arr[(arr > 10) & (arr < 30)] → Filter numbers between 10 and 30
"""

# ------------------------------------------------------------------------------
# 6. Bonus: Filtering with np.where() (returns indices)
# ------------------------------------------------------------------------------

arr = np.array([10, 25, 34, 45, 50])
print("\nIndices where arr > 30:", np.where(arr > 30))  # Output: (array([2, 3, 4]),)

"""
- np.where returns the **indices** of elements that satisfy a condition.
- arr[condition] returns the **values**.
- Both are useful depending on whether you want indexes or data.
"""

# ------------------------------------------------------------------------------
# Conclusion
# ------------------------------------------------------------------------------
"""
Filtering is one of the most powerful features in NumPy.
Use boolean indexing and conditions to extract exactly the data you want.

Highly optimized → Vectorized filtering is 100x+ faster than Python loops.
"""
