# #concatination combining rows either vertically or horizontally

# pd.concate([df1,df2,axis=0,igonre_index=True])

# basically it latches to dataframes together its not like join its like collection concatination

import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [4, 5, 6],
    'Name': ['David', 'Eva', 'Frank']
})

print(pd.concat([df1, df2],ignore_index=True,axis=1)) #axis is default 0 
"""
"on axis o i.r row means rows will be addes"
   ID     Name
0   1    Alice
1   2      Bob
2   3  Charlie
3   4    David
4   5      Eva
5   6    Frank

axis=1

   0        1  2      3
0  1    Alice  4  David
1  2      Bob  5    Eva
2  3  Charlie  6  Frank
"""


print(pd.concat([df1, df2],ignore_index=False)) #ingore index true means it wont allocate separate indices for second dataframe
"""
ignore_index=True

   ID     Name
0   1    Alice
1   2      Bob
2   3  Charlie
3   4    David
4   5      Eva
5   6    Frank

false
   ID     Name
0   1    Alice
1   2      Bob
2   3  Charlie
0   4    David
1   5      Eva
2   6    Frank

"""
