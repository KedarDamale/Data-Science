"""
NumPy: Numerical Python
========================

NumPy is a powerful Python library primarily used for:
- Numerical computing
- Working with arrays and matrices
- Performing mathematical and logical operations on arrays
- Supporting operations in domains like linear algebra, statistics, Fourier transforms, and more
"""

# -------------------------------
# History and Origin of NumPy
# -------------------------------
"""
- NumPy stands for Numerical Python.
- Created in 2005 by Travis Oliphant.
- It is the successor of an older package called Numeric and also merged features from Numarray.
- NumPy was developed to provide efficient array operations and be a foundation for scientific computing in Python.
"""

# -------------------------------
# Why NumPy?
# -------------------------------
"""
Python has built-in lists, but they have several limitations when it comes to numerical computing:
1. Lists are general-purpose containers. Each element is an object reference.
2. Python lists are stored as a list of pointers to memory locations (non-contiguous).
3. Hence, operations on them involve:
    - Type checking at runtime
    - Pointer dereferencing
    - Dynamic type dispatch
    => All of this adds overhead and makes them slower for heavy numerical computation.

In contrast, NumPy arrays:
- Are homogeneous (same data type)
- Use contiguous memory blocks (which enables fast computation and vectorization)
- Avoid type-checking during operations
- Are implemented in C/C++, allowing low-level memory and processor optimizations
- Support SIMD (Single Instruction, Multiple Data) and broadcasting, enabling much faster execution
"""

# Demonstrating speed difference
import numpy as np
import time

list1 = list(range(1000000))
array1 = np.array(list1)

# Timing Python list
start = time.time()
list_squared = [x ** 2 for x in list1]
end = time.time()
print("Time with list:", end - start)

# Timing NumPy array
start = time.time()
array_squared = array1 ** 2
end = time.time()
print("Time with NumPy:", end - start)

"""
Output: NumPy is usually 10x–50x faster depending on the operation.
"""

# -------------------------------
# Locality of Reference
# -------------------------------
"""
- In computer architecture, "locality of reference" means accessing memory locations that are close to each other.
- NumPy stores its arrays in contiguous memory locations, improving cache performance.
- CPUs fetch memory in chunks (cache lines), so accessing one element will load nearby elements too.
- This leads to fewer cache misses and drastically faster execution for array-wide operations.
"""

# -------------------------------
# Under-the-Hood: Why NumPy is Fast
# -------------------------------
"""
1. NumPy uses a C-based implementation of arrays for speed.
2. Operations are implemented as compiled C loops instead of interpreted Python loops.
3. Internally uses:
   - Vectorized instructions (SIMD)
   - Loop unrolling
   - Memory prefetching
4. Broadcasting avoids unnecessary copies of data and handles operations on mismatched shapes.
5. Interfaces with libraries like BLAS and LAPACK for linear algebra.

Result: NumPy offers high-level syntax with low-level performance.
"""
