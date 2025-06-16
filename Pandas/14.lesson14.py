"""
Here's a **comprehensive list of important functions and attributes in `pandas`**, categorized by use-case. Every item includes an explanation and a use-case example.

---

## 🔹 1. **Data Creation & Basic Structures**

### ➤ `pd.Series()`

Creates a one-dimensional labeled array.

```python
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
```

### ➤ `pd.DataFrame()`

Creates a two-dimensional table (rows and columns).

```python
df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [25, 30]
})
```

---

## 🔹 2. **Attributes of DataFrame/Series**

These do **not** require parentheses `()` (they are not functions).

| Attribute    | Purpose                                              |
| ------------ | ---------------------------------------------------- |
| `df.shape`   | Returns a tuple (rows, columns)                      |
| `df.size`    | Total number of elements (rows × columns)            |
| `df.ndim`    | Number of dimensions (1 for Series, 2 for DataFrame) |
| `df.columns` | Column labels                                        |
| `df.index`   | Row labels (index)                                   |
| `df.dtypes`  | Data type of each column                             |
| `df.values`  | Numpy array of values                                |
| `df.T`       | Transpose rows and columns                           |

```python
print(df.shape)   # (2, 2)
print(df.columns) # Index(['Name', 'Age'])
```

---

## 🔹 3. **Data Selection and Filtering**

| Function/Method        | Description                    |
| ---------------------- | ------------------------------ |
| `df['col']`            | Access column as Series        |
| `df[['col1','col2']]`  | Access multiple columns        |
| `df.iloc[i]`           | Row by integer position        |
| `df.loc[index]`        | Row by label                   |
| `df.at[]` / `df.iat[]` | Faster access to scalar values |
| `df.query()`           | SQL-like filtering             |

```python
df.iloc[0]              # First row
df.loc[0]               # Row with label 0
df[df['Age'] > 25]      # Filter rows
```

---

## 🔹 4. **Viewing and Summarizing Data**

| Method              | Description                               |
| ------------------- | ----------------------------------------- |
| `df.head(n)`        | First n rows (default = 5)                |
| `df.tail(n)`        | Last n rows                               |
| `df.info()`         | Summary: index, dtype, nulls              |
| `df.describe()`     | Descriptive statistics (numeric columns)  |
| `df.value_counts()` | Frequency count of unique values (Series) |
| `df.nunique()`      | Number of unique values per column        |
| `df.isnull()`       | Boolean mask of missing values            |
| `df.notnull()`      | Opposite of `isnull()`                    |
| `df.memory_usage()` | Memory used by each column                |

```python
df.describe()
df.info()
df['Age'].value_counts()
```

---

## 🔹 5. **Modifying Data**

| Function           | Description                          |
| ------------------ | ------------------------------------ |
| `df.drop()`        | Drop rows/columns                    |
| `df.rename()`      | Rename columns or index              |
| `df.sort_values()` | Sort by values in column             |
| `df.sort_index()`  | Sort by index                        |
| `df.fillna()`      | Replace missing values               |
| `df.dropna()`      | Drop missing rows                    |
| `df.replace()`     | Replace specific values              |
| `df.astype()`      | Convert data type                    |
| `df.apply()`       | Apply a function across rows/columns |
| `df.map()`         | Apply a function to Series           |
| `df.round()`       | Round float values                   |

```python
df = df.drop("Age", axis=1)
df = df.rename(columns={"Name": "FullName"})
df['Salary'] = df['Salary'].fillna(0)
```

---

## 🔹 6. **Aggregation and Grouping**

| Method                      | Description                          |
| --------------------------- | ------------------------------------ |
| `df.groupby()`              | Group rows by values of columns      |
| `df.agg()` or `aggregate()` | Apply multiple aggregation functions |
| `df.mean()`, `sum()`, etc.  | Aggregation across axis              |
| `df.count()`                | Count non-null entries               |
| `df.min()`, `max()`         | Min, max values                      |
| `df.median()`               | Median                               |
| `df.std()`, `var()`         | Standard deviation, variance         |

```python
df.groupby('Department')['Salary'].mean()
df.agg({'Age': ['min', 'max'], 'Salary': 'mean'})
```

---

## 🔹 7. **Merging & Joining**

| Function      | Description                              |
| ------------- | ---------------------------------------- |
| `pd.concat()` | Stack DataFrames horizontally/vertically |
| `pd.merge()`  | SQL-like joins on keys                   |
| `df.join()`   | Join columns using index                 |

```python
pd.concat([df1, df2], axis=0)          # Row-wise
pd.merge(df1, df2, on="id", how="left")  # SQL join
```

---

## 🔹 8. **Date & Time Handling**

| Function/Property       | Description         |
| ----------------------- | ------------------- |
| `pd.to_datetime()`      | Convert to datetime |
| `df['date'].dt.year`    | Extract year        |
| `df['date'].dt.month`   | Extract month       |
| `df['date'].dt.day`     | Extract day         |
| `df['date'].dt.weekday` | Day of week         |

```python
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
```

---

## 🔹 9. **Input/Output (File I/O)**

| Function          | Description             |
| ----------------- | ----------------------- |
| `pd.read_csv()`   | Read CSV file           |
| `pd.to_csv()`     | Save DataFrame to CSV   |
| `pd.read_excel()` | Read Excel file         |
| `pd.read_json()`  | Read JSON file          |
| `df.to_excel()`   | Save DataFrame to Excel |

```python
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)
```

---

## 🔹 10. **Indexing and Reshaping**

| Method                     | Description                     |
| -------------------------- | ------------------------------- |
| `df.set_index()`           | Set column as index             |
| `df.reset_index()`         | Reset index to default          |
| `df.pivot()`               | Pivot table (reshaping)         |
| `df.pivot_table()`         | Pivot with aggregation          |
| `df.melt()`                | Unpivot columns into rows       |
| `df.stack()` / `unstack()` | Change from wide to long format |
| `df.transpose()`           | Transpose rows ↔ columns        |

```python
df.set_index("Name", inplace=True)
df.reset_index(inplace=True)
```

---

## 🔹 11. **Window Functions**

| Function                   | Description                   |
| -------------------------- | ----------------------------- |
| `df.rolling(window)`       | Moving window calculations    |
| `df.expanding()`           | Expanding window (cumulative) |
| `df.cumsum()`              | Cumulative sum                |
| `df.cumprod()`             | Cumulative product            |
| `df.cummax()` / `cummin()` | Cumulative max/min            |

```python
df['rolling_avg'] = df['Sales'].rolling(window=3).mean()
```

---

## 🔹 12. **Utilities**

| Function               | Purpose                          |
| ---------------------- | -------------------------------- |
| `df.duplicated()`      | Check for duplicate rows         |
| `df.drop_duplicates()` | Remove duplicate rows            |
| `df.sample()`          | Random sample from DataFrame     |
| `df.clip()`            | Limit values between min and max |
| `df.eq()`              | Compare element-wise equality    |

```python
df.drop_duplicates(inplace=True)
df.sample(5)
```

---

Let me know if you want a **PDF of all this**, or want this organized by **cheat sheet format**, or need examples for **real-world datasets like Titanic, Netflix, etc.**


Here's a **deep-dive into how to use string, list, and other datatype-specific functions in `pandas`**, explained in detail with practical examples.

---

## 🔹 1. **String Functions in Pandas (`.str` accessor)**

Pandas provides a `.str` accessor to apply string methods on each element of a Series (usually of `dtype=object` or `string`).

### ✅ Common `.str` Methods

| Method                | Description                        |
| --------------------- | ---------------------------------- |
| `str.lower()`         | Convert to lowercase               |
| `str.upper()`         | Convert to uppercase               |
| `str.title()`         | Capitalize each word               |
| `str.strip()`         | Remove leading/trailing whitespace |
| `str.replace(a, b)`   | Replace substring `a` with `b`     |
| `str.contains("txt")` | Check if string contains substring |
| `str.startswith("a")` | Check if string starts with "a"    |
| `str.endswith("z")`   | Check if string ends with "z"      |
| `str.len()`           | Length of each string              |
| `str.split(" ")`      | Split string on delimiter          |
| `str.extract()`       | Extract substrings using regex     |
| `str.find("txt")`     | Index of first occurrence          |

### 🔍 Example:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": [" Alice ", "bob", "CHARLIE"],
    "Email": ["alice@gmail.com", "bob@yahoo.com", "charlie@outlook.com"]
})

df["Name_clean"] = df["Name"].str.strip().str.title()
df["Domain"] = df["Email"].str.split("@").str[1]
df["Is_Gmail"] = df["Email"].str.contains("gmail")

print(df)
```

---

## 🔹 2. **List-Like Data in Pandas**

If a column contains **lists (e.g. `[1,2,3]`)**, use `.apply()` with a `lambda` or native Python functions.

### ✅ Common operations on list columns

| Operation             | Example                             |
| --------------------- | ----------------------------------- |
| Access list element   | `df['col'].apply(lambda x: x[0])`   |
| Length of list        | `df['col'].apply(len)`              |
| Check if item in list | `df['col'].apply(lambda x: 3 in x)` |
| Flatten list column   | `df['col'].explode()`               |
| Sum values in list    | `df['col'].apply(sum)`              |

### 🔍 Example:

```python
df = pd.DataFrame({
    "Marks": [[10, 20, 30], [25, 35], [50, 60, 70]]
})

df["Total"] = df["Marks"].apply(sum)
df["First_Subject"] = df["Marks"].apply(lambda x: x[0])
df = df.explode("Marks")  # each list item becomes its own row

print(df)
```

---

## 🔹 3. **Datetime Functions in Pandas (`.dt` accessor)**

For `datetime64` dtype columns, use the `.dt` accessor to extract time-based information.

### ✅ Common `.dt` Methods

| Method                              | Description            |
| ----------------------------------- | ---------------------- |
| `dt.year`                           | Extract year           |
| `dt.month`                          | Extract month          |
| `dt.day`                            | Extract day            |
| `dt.weekday`                        | 0 = Monday, 6 = Sunday |
| `dt.hour`, `dt.minute`, `dt.second` | Extract time           |
| `dt.date`                           | Only date part         |
| `dt.time`                           | Only time part         |
| `dt.strftime()`                     | Format as string       |

### 🔍 Example:

```python
df = pd.DataFrame({
    "Joined": pd.to_datetime(["2023-06-01 14:20", "2022-01-11 08:05"])
})

df["Year"] = df["Joined"].dt.year
df["Hour"] = df["Joined"].dt.hour
df["Formatted"] = df["Joined"].dt.strftime("%d-%b-%Y %I:%M %p")

print(df)
```

---

## 🔹 4. **Boolean Functions**

You can filter or operate on Boolean-type data using:

| Function           | Description                     |                                    |
| ------------------ | ------------------------------- | ---------------------------------- |
| `df.any()`         | True if **any** value is True   |                                    |
| `df.all()`         | True if **all** values are True |                                    |
| `df.sum()`         | Counts number of `True` values  |                                    |
| `~` (NOT), `&`, \` | \`                              | Logical NOT, AND, OR for filtering |

```python
df = pd.DataFrame({
    "A": [True, False, True],
    "B": [False, False, True]
})

df["A & B"] = df["A"] & df["B"]
print(df.any())  # Any True?
```

---

## 🔹 5. **Numeric Functions**

| Function                 | Description                |
| ------------------------ | -------------------------- |
| `df['col'].sum()`        | Sum of values              |
| `df['col'].mean()`       | Average                    |
| `df['col'].round(2)`     | Round to decimal places    |
| `df['col'].clip(0, 100)` | Limit values within bounds |
| `df['col'].abs()`        | Absolute values            |

---

## 🔹 6. **Type Checking & Conversion**

| Function             | Purpose                            |
| -------------------- | ---------------------------------- |
| `df.dtypes`          | Show data types                    |
| `df.astype()`        | Change data type                   |
| `pd.to_numeric()`    | Convert to numeric (with coercion) |
| `pd.to_datetime()`   | Convert to datetime                |
| `pd.to_timedelta()`  | Convert to timedelta               |
| `df.select_dtypes()` | Select columns by dtype            |

```python
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
df["JoinDate"] = pd.to_datetime(df["JoinDate"])
```

---

## 🔹 7. **Using `.apply()` vs `.map()` vs `.applymap()`**

| Method        | Applies To          | Description                           |
| ------------- | ------------------- | ------------------------------------- |
| `.apply()`    | Series or DataFrame | Row/Column-wise operations (flexible) |
| `.map()`      | Series              | Element-wise transformation           |
| `.applymap()` | DataFrame           | Element-wise for entire DataFrame     |

### 🔍 Example:

```python
df["Salary"] = df["Salary"].apply(lambda x: x * 1.1)  # 10% hike
df["Grade"] = df["Score"].map({90: "A", 80: "B"})     # Mapping
```

---

## ✅ Summary

| Data Type | Accessor       | Functions/Examples                                    |    |
| --------- | -------------- | ----------------------------------------------------- | -- |
| String    | `.str`         | `lower`, `contains`, `split`, `replace`, `len`, etc.  |    |
| List      | `apply()`      | `len`, `sum`, indexing, `explode`, `lambda` functions |    |
| Datetime  | `.dt`          | `year`, `month`, `hour`, `weekday`, `strftime`, etc.  |    |
| Boolean   | n/a            | `any`, `all`, `sum`, `~`, `&`, \`                     | \` |
| Numeric   | n/a            | `sum`, `mean`, `abs`, `clip`, `round`                 |    |
| General   | `apply`, `map` | Used for transformations and logic                    |    |

---

Let me know if you want a **practice dataset**, or real-world exercises applying all these functions.



"""