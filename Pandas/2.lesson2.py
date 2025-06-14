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
# count:number of elements
# mean:average
# std deviation mean how data differs from mean smal std: those who are very close to mean large std: numbers who are not close to mean
# min ; minimumum of all
# 25%:0t0 25 percentile data
# 50%;median middle element
# 75% means values from 50 to 100
# max means maximum from elements

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