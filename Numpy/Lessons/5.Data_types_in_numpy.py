"""
NumPy Data Types (dtype) - Complete Notes with Examples
========================================================

In NumPy, arrays are *homogeneous* — all elements must be of the same type.
The `dtype` defines the type of data elements the array holds.

You can check, specify, and convert the data type using:
    - `array.dtype`       → check type
    - `dtype='type_code'` → specify type
    - `astype()`          → convert type (not in-place)

Basic Type Codes:
-----------------
| Code | Data Type           |
|------|---------------------|
| 'i'  | signed integer      |
| 'u'  | unsigned integer    |
| 'f'  | floating point      |
| 'c'  | complex floating pt |
| 'b'  | boolean             |
| 'S'  | byte string         |
| 'U'  | Unicode string      |
| 'M'  | datetime            |
| 'm'  | timedelta           |
| 'O'  | Python object       |
| 'V'  | raw data (void)     |
"""

import numpy as np

# -----------------------------------------------------------------------------
# 1. Check default data type (implicit inference)
# -----------------------------------------------------------------------------

arr_default = np.array([1, 2, 3])
print("Default dtype (int inferred):", arr_default.dtype)  # int32 or int64 depending on system

# -----------------------------------------------------------------------------
# 2. Creating arrays with explicit dtype
# -----------------------------------------------------------------------------

arr_str = np.array([1, 2, 3], dtype='S')  # Byte string  #or ("string") or even (str) also works 
print("Byte string array:", arr_str, "| dtype:", arr_str.dtype)

arr_unicode = np.array([1, 2, 3], dtype='U')  # Unicode string
print("Unicode string array:", arr_unicode, "| dtype:", arr_unicode.dtype)

arr_float = np.array([1, 2, 3], dtype='f')  # Float32 (default)
print("Float array:", arr_float, "| dtype:", arr_float.dtype)

arr_int32 = np.array([1, 2, 3], dtype='i4')  # 4-byte integer
print("Int32 array:", arr_int32, "| dtype:", arr_int32.dtype)

arr_unsigned = np.array([1, 2, 3], dtype='u1')  # Unsigned 1-byte integer
print("Unsigned int array:", arr_unsigned, "| dtype:", arr_unsigned.dtype)

arr_bool = np.array([0, 1, 3], dtype='b')  # Boolean
print("Boolean array:", arr_bool, "| dtype:", arr_bool.dtype)

arr_complex = np.array([1, 2, 3], dtype='c8')  # Complex numbers
print("Complex array:", arr_complex, "| dtype:", arr_complex.dtype)

arr_obj = np.array([1, "apple", 3.14], dtype='O')  # Python object array
print("Object array:", arr_obj, "| dtype:", arr_obj.dtype)

# -----------------------------------------------------------------------------
# 3. Memory Specification (e.g., S100 = string of 100 bytes per element)
# -----------------------------------------------------------------------------

arr_str100 = np.array(['apple', 'banana'], dtype='S100')
print("Fixed size byte string:", arr_str100, "| dtype:", arr_str100.dtype)

# -----------------------------------------------------------------------------
# 4. Implicit Upcasting to maintain homogeneity
# -----------------------------------------------------------------------------

arr_mixed = np.array([1, 2.5, 3])  # Mixed int and float → upcast to float
print("Implicit upcast:", arr_mixed, "| dtype:", arr_mixed.dtype)

arr_mixed2 = np.array([1, "2", 3])  # Upcast to Unicode string
print("Upcast to string:", arr_mixed2, "| dtype:", arr_mixed2.dtype)

# -----------------------------------------------------------------------------
# 5. Type Conversion using astype()
# -----------------------------------------------------------------------------

arr = np.array([1.1, 2.2, 3.3])
print("Original float array:", arr)

arr_int = arr.astype('i')  # or 'int', or int
print("Converted to int:", arr_int)

arr_str = arr.astype(str)  # to Python string
print("Converted to Python string:", arr_str)

arr_bytes = arr.astype('S')
print("Converted to byte strings:", arr_bytes)

# -----------------------------------------------------------------------------
# 6. Invalid Conversion (Raises Error)
# -----------------------------------------------------------------------------

try:
    arr_error = np.array(['a', '5', '10'], dtype='i')
except ValueError as e:
    print("Error on invalid conversion:", e)

# -----------------------------------------------------------------------------
# 7. Conversion Summary Table (Supported)
# -----------------------------------------------------------------------------

"""
| From \ To | int | float | str | bool |
|-----------|-----|-------|-----|------|
| int       | ✓   | ✓     | ✓   | ✓    |
| float     | ✓   | ✓     | ✓   | ✓    |
| str       | ✗   | ✗     | ✓   | ✗    |
| bool      | ✓   | ✓     | ✓   | ✓    |
"""

# -----------------------------------------------------------------------------
# 8. Special Types (Datetime and Timedelta)
# -----------------------------------------------------------------------------

date_arr = np.array(['2024-01-01', '2025-06-11'], dtype='M')  # datetime64
print("Datetime array:", date_arr, "| dtype:", date_arr.dtype)

delta_arr = np.array([1, 2, 3], dtype='m')  # timedelta64
print("Timedelta array:", delta_arr, "| dtype:", delta_arr.dtype)
