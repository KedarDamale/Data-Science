# =============================================================================
# 🐼 PANDAS INTRODUCTORY NOTES WITH IN-DEPTH COMMENTS
# =============================================================================
# ✅ Author: Kedar Damale
# ✅ Format: Python script with detailed inline comments
# ✅ Purpose: Learn Pandas step-by-step with deep understanding
# =============================================================================

# -----------------------------------------------------------------------------
# 1. What is Pandas?
# -----------------------------------------------------------------------------
# → Pandas is an open-source data manipulation and analysis library for Python.
# → It was created in 2008 by Wes McKinney to solve the need for flexible and
#   powerful data structures suitable for working with relational and labeled data.

# → The name 'pandas' is derived from "panel data", a term used in econometrics.

# -----------------------------------------------------------------------------
# 2. Why use Pandas?
# -----------------------------------------------------------------------------
# - Provides high-performance data structures: Series (1D), DataFrame (2D)
# - Simplifies data loading, processing, analysis, filtering, reshaping, etc.
# - Built on top of NumPy → benefits from vectorization (fast computation)
# - Easily integrates with:
#       → Matplotlib & Seaborn (for plotting)
#       → scikit-learn (for ML)
#       → SQL databases, Excel, CSV, HTML, JSON, and more

# -----------------------------------------------------------------------------
# 3. Installing and Importing Pandas
# -----------------------------------------------------------------------------

# You install pandas using pip if it's not already installed:
# pip install pandas

import pandas as pd  # Standard alias for pandas

# -----------------------------------------------------------------------------
# 4. Core Data Structures in Pandas
# -----------------------------------------------------------------------------
# Pandas provides two essential classes:
# (a) pd.Series    → One-dimensional labeled array (like a single column)
# (b) pd.DataFrame → Two-dimensional labeled table (like an Excel sheet)

# -----------------------------------------------------------------------------
# 4.1 Series
# -----------------------------------------------------------------------------
# → A Series is similar to a NumPy array but with labels (index) for each value.
# → It can store any data type: int, float, str, bool, Python objects, etc.

series = pd.Series([10, 20, 30, 40])  # Default integer index will be used
print("Series with default index:\n", series)

# Custom index can also be used
series_custom = pd.Series([3.14, 2.71, 1.62], index=["pi", "e", "phi"])
print("\nSeries with custom labels:\n", series_custom)

# -----------------------------------------------------------------------------
# 4.2 DataFrame
# -----------------------------------------------------------------------------
# → A DataFrame is a collection of Series objects that share the same index.
# → Think of it as an in-memory table (rows + columns).

# Creating a DataFrame manually using a Python dictionary:
data = {
    "Names": ["Kedar", "Pravin", "Priya", "Kanchan"],
    "Age": [21, 53, 50, 27],
    "Profession": ["Student", "Engineer", "Homemaker", "Financial-Advisor"],
    "Education": ["Graduate-student", "ITI", "10th", "Masters"]
}

df = pd.DataFrame(data)
print("\nConstructed DataFrame:\n", df)

# -----------------------------------------------------------------------------
# 5. Reading Data from External Files
# -----------------------------------------------------------------------------

# 5.1 CSV (Comma Separated Values) File
# CSV is a plain text format with comma-separated values on each line

# Read a CSV file (basic)
# df = pd.read_csv("filename.csv")

# Handling encoding issues (e.g., UnicodeDecodeError)
# UTF-8 is the most common, but if it fails, try 'latin-1', 'ISO-8859-1'
# df = pd.read_csv("filename.csv", encoding="utf-8")
# df = pd.read_csv("filename.csv", encoding="latin-1")

# Note: File extension like '.csv' is mandatory

# 5.2 Excel Files
# Requires openpyxl or xlrd installed
# df = pd.read_excel("filename.xlsx")

# -----------------------------------------------------------------------------
# 6. Pandas Can Read Multiple Formats
# -----------------------------------------------------------------------------
# - pd.read_csv()        → for CSV files
# - pd.read_excel()      → for Excel files (.xls, .xlsx)
# - pd.read_html()       → tables from HTML pages
# - pd.read_json()       → for JSON format
# - pd.read_sql()        → for SQL databases (needs DBAPI connection)
# - pd.read_parquet()    → fast columnar format used in big data

# Similarly, there are `to_<format>()` functions to save/export data

# -----------------------------------------------------------------------------
# 7. Saving/Exporting Data to Files
# -----------------------------------------------------------------------------

# Exporting the created DataFrame to a CSV file (includes index by default)
df.to_csv("family_with_index.csv")  # Adds a new column for index

# Output:
# ,Names,Age,Profession,Education
# 0,Kedar,21,Student,Graduate-student
# 1,Pravin,53,Engineer,ITI
# ...

# To prevent saving the index, set `index=False`
df.to_csv("family.csv", index=False)

# Output:
# Names,Age,Profession,Education
# Kedar,21,Student,Graduate-student
# Pravin,53,Engineer,ITI
# Priya,50,Homemaker,10th
# Kanchan,27,Financial-Advisor,Masters

# Export to other formats
df.to_excel("family.xlsx", index=False)   # Save as Excel file
df.to_json("family.json")                 # Save as JSON
df.to_html("family.html")                 # Save as HTML table



