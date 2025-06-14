import pandas as pd

data={
    "Names":["AMBERKAR KOMAL SURYAKANT","ARLEKAR PRATHAMESH MAHESH","AYARE DARSHAN NARESH",
             "AYARE SANIA NARENDRA","BACHIM ATHARV MARUTI","BHATKAR SAHIL VILAS","BHOMBAL ZIA AMIR",
             "BHUJBAL YUKTA SADASHIV","DABHOLKAR PRACHI PRADIP"," DAMALE KEDAR PRAVIN "],
    
    "DMBI_IA1":[10,9,10,16,8,6,8,10,18,17],
    "DMBI_IA2":[17,10,13,14,12,12,13,8,14,16],
    
    "WEBX_IA1":[17,18,17,20,20,19,18,14,20,19],
    "WEBX_IA2":[13,15,17,12,14,14,9,10,19,20],
    
    "WT_IA1":[16,14,13,15,17,15,14,18,19,20],
    "WT_IA2":[16,11,11,15,16,15,13,16,18,19],
    
    "AIDS-1_IA1":[15,15,13,17,13,15,12,17,17,20],
    "AIDS-1_IA2":[17,15,15,19,8,15,18,18,18,20],
    
    "EHF_IA1":[11,10,10,14,13,10,11,9,14,18],
    "EHF_IA2":[15,16,16,16,16,14,14,18,17,18]
}

df=pd.DataFrame(data)
df.to_csv("IA_marks.csv")
print(df)# this will print all the data there is which is not optimal many a times

#head(n)
#this function will only display first n number of rows n being default 5
print("first 5 rows")
print(df.head())
print("first 7 rows")
print(df.head(7))

#tail(n)
#this function will only display last n number of rows n being default 5
print("last 5 rows")
print(df.tail())
print("last 7 rows")
print(df.tail(7))

#info()
#info method will display information like
#rows and columns
#dataentries number 
#columns with the data type of its elements with non null count means how many elements are not null
#memory usage

print(df.info())

"""
[7 rows x 11 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 11 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Names       10 non-null     object
 1   DMBI_IA1    10 non-null     int64 
 2   DMBI_IA2    10 non-null     int64 
 3   WEBX_IA1    10 non-null     int64 
 4   WEBX_IA2    10 non-null     int64 
 5   WT_IA1      10 non-null     int64 
 6   WT_IA2      10 non-null     int64 
 7   AIDS-1_IA1  10 non-null     int64 
 8   AIDS-1_IA2  10 non-null     int64 
 9   EHF_IA1     10 non-null     int64 
 10  EHF_IA2     10 non-null     int64 
dtypes: int64(10), object(1)
memory usage: 1012.0+ bytes
None
"""

#descibe() method

#provides descriptive numerical statistics of the dataframe

print(df.describe())

"""
        DMBI_IA1   DMBI_IA2   WEBX_IA1  ...  AIDS-1_IA2    EHF_IA1    EHF_IA2
count  10.000000  10.000000  10.000000  ...    10.00000  10.000000  10.000000
mean   11.200000  12.900000  18.200000  ...    16.30000  12.000000  16.000000
std     4.211096   2.643651   1.873796  ...     3.40098   2.748737   1.414214
min     6.000000   8.000000  14.000000  ...     8.00000   9.000000  14.000000
25%     8.250000  12.000000  17.250000  ...    15.00000  10.000000  15.250000
50%    10.000000  13.000000  18.500000  ...    17.50000  11.000000  16.000000
75%    14.500000  14.000000  19.750000  ...    18.00000  13.750000  16.750000
max    18.000000  17.000000  20.000000  ...    20.00000  18.000000  18.000000

[8 rows x 10 columns]
"""
#as you can see count mean std deviation and many more parameters
"""
You're referring to the statistical summary typically provided by functions like `DataFrame.describe()` in **Pandas** or similar summary statistics in **NumPy**, **SciPy**, etc. Let's break each term down with **detailed technical explanations**, **reasoning**, and **examples**:

---

### 📌 1. `count` – **Number of Non-Null Elements**

* **Definition**: The total number of **non-missing (non-NaN)** values in a column or dataset.
* **Why it’s used**: Helps understand if there are missing values and how many actual values contribute to calculations.
* **Example**:

  ```python
  import pandas as pd
  data = pd.Series([10, 20, None, 30])
  print(data.count())  # Output: 3
  ```

  * Even though there are 4 elements, `count` is 3 because one is `None` (missing/NaN).

---

### 📌 2. `mean` – **Arithmetic Average**

* **Definition**: Sum of all values divided by the number of values.
* **Formula**:

  $$
  \text{mean} = \frac{x_1 + x_2 + \cdots + x_n}{n}
  $$
* **Why it’s used**: Represents the **central tendency** of the data – a "typical" value.
* **Limitation**: Sensitive to **outliers**.
* **Example**:

  ```python
  import numpy as np
  arr = np.array([10, 20, 30, 40])
  print(np.mean(arr))  # Output: 25.0
  ```

---

### 📌 3. `std` – **Standard Deviation**

* **Definition**: Measures the **spread** or **dispersion** of values from the mean.
* **Interpretation**:

  * **Low std** → values are **close to the mean** (less variability).
  * **High std** → values are **widely spread** from the mean.
* **Formula**:

  $$
  \sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n}(x_i - \bar{x})^2}
  $$
* **Why it's important**: Tells you how consistent your data is.
* **Example**:

  ```python
  arr1 = np.array([10, 12, 11])  # std is low
  arr2 = np.array([1, 50, 100]) # std is high
  print(np.std(arr1), np.std(arr2))
  ```

---

### 📌 4. `min` – **Minimum Value**

* **Definition**: The **smallest** value in the data.
* **Why it’s useful**: Gives you the **lower bound** of the range.
* **Example**:

  ```python
  arr = np.array([4, 10, 2, 99])
  print(np.min(arr))  # Output: 2
  ```

---

### 📌 5. `25%` – **First Quartile (Q1)**

* **Definition**: 25th percentile. It means **25%** of the data points are **less than or equal to** this value.
* **Why it’s useful**: Helps understand the **distribution** of the lower segment of data.
* **Example**:

  ```python
  arr = np.array([10, 20, 30, 40])
  print(np.percentile(arr, 25))  # Output: 17.5
  ```

---

### 📌 6. `50%` – **Median (Q2)**

* **Definition**: The **middle value** of a sorted dataset.

  * If odd number of items → middle one.
  * If even → average of two middle values.
* **Why it’s important**: Unlike mean, it is **robust to outliers**.
* **Example**:

  ```python
  arr = np.array([1, 2, 3])
  print(np.median(arr))  # Output: 2

  arr = np.array([1, 2, 3, 100])
  print(np.median(arr))  # Output: 2.5 (resistant to 100)
  ```

---

### 📌 7. `75%` – **Third Quartile (Q3)**

* **Definition**: 75th percentile. It means **75% of values are below** this value.
* **Why it’s used**: Shows the **upper middle** part of the distribution.
* **Example**:

  ```python
  arr = np.array([10, 20, 30, 40])
  print(np.percentile(arr, 75))  # Output: 32.5
  ```

---

### 📌 8. `max` – **Maximum Value**

* **Definition**: The **largest** value in the data.
* **Why it’s useful**: Gives you the **upper bound** of the range.
* **Example**:

  ```python
  arr = np.array([4, 10, 2, 99])
  print(np.max(arr))  # Output: 99
  ```

---

### ✅ Summary Table

| Statistic | Description               | Purpose                 |
| --------- | ------------------------- | ----------------------- |
| `count`   | Number of non-null values | Data completeness check |
| `mean`    | Arithmetic average        | Central tendency        |
| `std`     | Standard deviation        | Spread or variability   |
| `min`     | Minimum value             | Lower bound             |
| `25%`     | First quartile (Q1)       | Lower quartile analysis |
| `50%`     | Median (Q2)               | Robust central value    |
| `75%`     | Third quartile (Q3)       | Upper quartile analysis |
| `max`     | Maximum value             | Upper bound             |

---

### 🧠 Pro Tip: Use `.describe()` in Pandas

```python
import pandas as pd

df = pd.DataFrame({
    "Scores": [35, 40, 45, 50, 55, 60, 65, 70, 75, 100]
})
print(df.describe())
```

This gives:

```
count     10.000000
mean      59.500000
std       19.573743
min       35.000000
25%       48.750000
50%       57.500000
75%       70.000000
max      100.000000
```

---

Let me know if you want **visualizations** for these using **Matplotlib** or **Seaborn**.

"""


"""
from the describe method we can take out conclusions such as

average in DMB! IA1 is lowest and webx ia1 is highest
std dev of ehfia2 is lowest mean all student have closer to mean marks
and much more basically
"""

#shape attribute
# returns a tuple ()number of rows,columns

print(df.shape)#(10, 11)


#columns attribute return columns names and ability to access and mofify them

print(df.columns)
"""
Index(['Names', 'DMBI_IA1', 'DMBI_IA2', 'WEBX_IA1', 'WEBX_IA2', 'WT_IA1',
       'WT_IA2', 'AIDS-1_IA1', 'AIDS-1_IA2', 'EHF_IA1', 'EHF_IA2'],
      dtype='object')
"""