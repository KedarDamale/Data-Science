#merging in pandas basically like sql joins
#joining to data frames based on common key 

# pd.merge(df1,df2,on="common_column_name",how="join methdo") how=[inner outer left right cross right-anti left anti]

import pandas as pd


customers = {
    "customer_id": [1, 2, 3, 4, 5],
    "customer_name": ["Kedar", "Pravin", "Priya", "Kanchan", "Sugandha"]
}

transactions = {
    "transaction_id": [101, 102, 103, 104, 105, 106, 107],
    "customer_id": [1, 2, 1, 3, 1, 4, 2],
    "product": ["Laptop", "Phone", "Mouse", "Tablet", "Book", "Keyboard", "Monitor"],
    "amount": [70000, 20000, 1500, 30000, 500, 1800, 12000],
}

customers_df = pd.DataFrame(customers)
transactions_df = pd.DataFrame(transactions)


#print(pd.merge(customers_df, transactions_df, on="customer_id", how="inner")) 

"""
   customer_id customer_name  transaction_id   product  amount
0            1         Kedar             101    Laptop   70000
1            1         Kedar             103     Mouse    1500
2            2        Pravin             102     Phone   20000
3            2        Pravin             107   Monitor   12000
4            3         Priya             104    Tablet   30000
5            4       Kanchan             106  Keyboard    1800
6            5      Sugandha             105      Book     500
"""
#print(pd.merge(customers_df, transactions_df, on="customer_id", how="outer"))

"""
   customer_id customer_name  transaction_id   product  amount
0            1         Kedar             101    Laptop   70000
1            1         Kedar             103     Mouse    1500
2            2        Pravin             102     Phone   20000
3            2        Pravin             107   Monitor   12000
4            3         Priya             104    Tablet   30000
5            4       Kanchan             106  Keyboard    1800
6            5      Sugandha             105      Book     500
"""

print(pd.merge(customers_df, transactions_df, how="cross")) #for cross ther is no key


"""
    customer_id_x customer_name  ...   product  amount
0               1         Kedar  ...    Laptop   70000
1               1         Kedar  ...     Phone   20000
2               1         Kedar  ...     Mouse    1500
3               1         Kedar  ...    Tablet   30000
4               1         Kedar  ...      Book     500
5               1         Kedar  ...  Keyboard    1800
6               1         Kedar  ...   Monitor   12000
7               2        Pravin  ...    Laptop   70000
8               2        Pravin  ...     Phone   20000
9               2        Pravin  ...     Mouse    1500
10              2        Pravin  ...    Tablet   30000
11              2        Pravin  ...      Book     500
12              2        Pravin  ...  Keyboard    1800
13              2        Pravin  ...   Monitor   12000
14              3         Priya  ...    Laptop   70000
15              3         Priya  ...     Phone   20000
16              3         Priya  ...     Mouse    1500
17              3         Priya  ...    Tablet   30000
18              3         Priya  ...      Book     500
19              3         Priya  ...  Keyboard    1800
20              3         Priya  ...   Monitor   12000
21              4       Kanchan  ...    Laptop   70000
22              4       Kanchan  ...     Phone   20000
23              4       Kanchan  ...     Mouse    1500
24              4       Kanchan  ...    Tablet   30000
25              4       Kanchan  ...      Book     500
26              4       Kanchan  ...  Keyboard    1800
27              4       Kanchan  ...   Monitor   12000
28              5      Sugandha  ...    Laptop   70000
29              5      Sugandha  ...     Phone   20000
30              5      Sugandha  ...     Mouse    1500
31              5      Sugandha  ...    Tablet   30000
32              5      Sugandha  ...      Book     500
33              5      Sugandha  ...  Keyboard    1800
34              5      Sugandha  ...   Monitor   12000

"""

print(pd.merge(customers_df, transactions_df, on="customer_id", how="right"))
"""
   customer_id customer_name  transaction_id   product  amount
0            1         Kedar             101    Laptop   70000
1            2        Pravin             102     Phone   20000
2            1         Kedar             103     Mouse    1500
3            3         Priya             104    Tablet   30000
4            1         Kedar             105      Book     500
5            4       Kanchan             106  Keyboard    1800
6            2        Pravin             107   Monitor   12000

"""

print(pd.merge(customers_df, transactions_df, on="customer_id", how="left"))
"""
   customer_id customer_name  transaction_id   product   amount
0            1         Kedar           101.0    Laptop  70000.0
1            1         Kedar           103.0     Mouse   1500.0
2            1         Kedar           105.0      Book    500.0
3            2        Pravin           102.0     Phone  20000.0
4            2        Pravin           107.0   Monitor  12000.0
5            3         Priya           104.0    Tablet  30000.0
6            4       Kanchan           106.0  Keyboard   1800.0
7            5      Sugandha             NaN       NaN      NaN
as you can see sugandha hasnt purchased anything thats why NaN is there
"""

