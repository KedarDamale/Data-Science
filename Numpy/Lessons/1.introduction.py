""""
NumPy Introduction – Cleaned and Expanded Notes
"""

# --------------------------------------------
# 🧠 Who Created NumPy?
# --------------------------------------------
# NumPy was created by Travis Oliphant in 2005.
# It was developed by combining the functionality of two older Python libraries: Numeric and Numarray.
# The goal was to create a standardized, high-performance foundation for numerical computations in Python.

# --------------------------------------------
# 🔍 Why Was NumPy Developed?
# --------------------------------------------
# Python is an interpreted language, which makes it slower compared to compiled languages like C/C++ or Java,
# especially when processing large volumes of numerical data.

# NumPy bridges this gap by:
# - Providing a C-based backend for array operations.
# - Running performance-critical operations in compiled C/Fortran code under the hood.
# - Allowing Python developers to write high-performance numerical code with simple, readable syntax.

# This combination gives Python the speed of C and the simplicity of Python,
# making NumPy a core tool in fields like:
# - Data Science
# - Machine Learning
# - Scientific Computing
# - Engineering Simulations

# --------------------------------------------
# 📦 Libraries That Depend on NumPy
# --------------------------------------------
# NumPy is a foundational package and a **core dependency** for many major Python libraries:
# - SciPy      → scientific computations
# - Pandas     → data analysis and manipulation
# - scikit-learn → machine learning
# - TensorFlow / PyTorch → deep learning frameworks

# --------------------------------------------
# ✅ Importing NumPy
# --------------------------------------------
import numpy as np

# --------------------------------------------
# 🆚 Python Lists vs. NumPy Arrays
# --------------------------------------------
# Python lists:
# - Are heterogeneous: can store elements of different types (e.g., int, str, float).
# - Are not optimized for numerical operations.
# - Do not support element-wise operations out of the box.
# - Are flexible but not fast for large-scale computations.

# NumPy arrays:
# - Are homogeneous: all elements must be of the same data type.
# - Are stored in contiguous memory blocks, making them much faster.
# - Support vectorized operations (e.g., element-wise addition, multiplication).
# - Can perform complex operations like matrix multiplication, dot product, broadcasting.

# --------------------------------------------
# 🧮 Example: Average Temperature (Vanilla Python vs NumPy)
# --------------------------------------------

# Using vanilla Python with loop:
temp = [12, 34, 12, 34, 56, 78, 90, 34, 23]
temp_total = 0
for t in temp:
    temp_total += t

print(f"(Python) Average temperature: {temp_total / len(temp):.2f}")

# Using NumPy:
print(f"(NumPy) Average temperature: {np.mean(temp):.2f}")

# --------------------------------------------
# ⚡ Performance Boost in NumPy
# --------------------------------------------
# Why NumPy is faster:
# - NumPy internally uses C and Fortran libraries.
# - Operations are vectorized (executed in bulk at once instead of looping).
# - Avoids Python-level for loops and uses compiled routines instead.

# Real-world benchmark studies show NumPy can be 10x to 100x faster for numerical workloads.

# --------------------------------------------
# 📐 NumPy Arrays = Real Arrays (Unlike Python Lists)
# --------------------------------------------
# In C/C++, arrays are contiguous blocks of memory storing elements of the same data type.
# NumPy replicates this behavior in Python using the ndarray object.
# This allows support for:
# - Vector algebra (addition, dot product)
# - Matrix operations
# - Broadcasting (automatically expanding array shapes)

# Note:
# If you want actual arrays in Python (not NumPy), you can use the 'array' module:
import array
arr = array.array('i', [1, 2, 3])  # Only integer type ('i') allowed

# But this array module is limited compared to NumPy.

# --------------------------------------------
# 📚 Summary
# --------------------------------------------
# - NumPy was built to solve the performance limitations of Python for numerical work.
# - It is built on C/Fortran, enabling massive speed boosts for numerical tasks.
# - Provides true arrays with powerful operations like broadcasting, matrix math.
# - It’s a core building block of the entire Python data science ecosystem.
