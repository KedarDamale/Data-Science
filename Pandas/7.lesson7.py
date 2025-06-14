#handling missing data

import pandas as pd

data={
    "Names":["AMBERKAR KOMAL SURYAKANT",None,"AYARE DARSHAN NARESH",
             "AYARE SANIA NARENDRA","BACHIM ATHARV MARUTI","BHATKAR SAHIL VILAS","BHOMBAL ZIA AMIR",
             "BHUJBAL YUKTA SADASHIV","DABHOLKAR PRACHI PRADIP"," DAMALE KEDAR PRAVIN "],
    
    "DMBI_IA1":[10,9,10,None,8,6,8,10,18,17],
    "DMBI_IA2":[17,10,13,14,12,12,13,8,14,16],
    
    "WEBX_IA1":[17,18,17,20,20,None,18,14,20,19],
    "WEBX_IA2":[13,15,17,12,14,14,9,10,19,20],
    
    "WT_IA1":[16,14,13,15,None,15,14,18,19,20],
    "WT_IA2":[16,11,11,15,16,15,13,16,None,19],
    
    "AIDS-1_IA1":[15,None,13,17,13,15,12,17,17,20],
    "AIDS-1_IA2":[17,15,15,19,8,15,18,18,18,20],
    
    "EHF_IA1":[11,10,10,14,None,10,11,9,14,18],
    "EHF_IA2":[15,None,16,16,16,14,14,18,17,18]
}
df=pd.DataFrame(data)

# print(df.info())
"""
class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 11 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Names       10 non-null     object 
 1   DMBI_IA1    9 non-null      float64
 2   DMBI_IA2    10 non-null     int64  
 3   WEBX_IA1    9 non-null      float64
 4   WEBX_IA2    10 non-null     int64  
 5   WT_IA1      9 non-null      float64
 6   WT_IA2      9 non-null      float64
 7   AIDS-1_IA1  9 non-null      float64
 8   AIDS-1_IA2  10 non-null     int64  
 9   EHF_IA1     9 non-null      float64
 10  EHF_IA2     9 non-null      float64
dtypes: float64(7), int64(3), object(1)
memory usage: 1012.0+ bytes

we can identify null values or NaN values from the datase
"""

# print(df.isnull())
"""
isnull is specifically made for figuring null values this will return a matrix of true and false if true tehn value there is null 
   Names  DMBI_IA1  DMBI_IA2  ...  AIDS-1_IA2  EHF_IA1  EHF_IA2
0  False     False     False  ...       False    False    False
1  False     False     False  ...       False    False     True
2  False     False     False  ...       False    False    False
3  False      True     False  ...       False    False    False
4  False     False     False  ...       False     True    False
5  False     False     False  ...       False    False    False
6  False     False     False  ...       False    False    False
7  False     False     False  ...       False    False    False
8  False     False     False  ...       False    False    False
9  False     False     False  ...       False    False    False

[10 rows x 11 columns]
"""
# print(df.isnull().sum())
"""
[10 rows x 11 columns]
Names         0
DMBI_IA1      1
DMBI_IA2      0
WEBX_IA1      1
WEBX_IA2      0
WT_IA1        1
WT_IA2        1
AIDS-1_IA1    1
AIDS-1_IA2    0
EHF_IA1       1
EHF_IA2       1
dtype: int64

sum metho will sum up the values for upper dimension
"""
# print(df.isnull().sum().sum()) #here upper dimension for columns is entire dataframe so it summs up for that 7

#handling the null values

#1.Dropping the the data if it doesnt affect

# df.dropna(axis=0,inplace=True) #axis=0 means drop rows with missing values and axis=1 means drop columns with missing values

# print(df)

"""
                      Names  DMBI_IA1  DMBI_IA2  ...  AIDS-1_IA2  EHF_IA1  EHF_IA2
0  AMBERKAR KOMAL SURYAKANT      10.0        17  ...          17     11.0     15.0
2      AYARE DARSHAN NARESH      10.0        13  ...          15     10.0     16.0
6          BHOMBAL ZIA AMIR       8.0        13  ...          18     11.0     14.0
7    BHUJBAL YUKTA SADASHIV      10.0         8  ...          18      9.0     18.0
9      DAMALE KEDAR PRAVIN       17.0        16  ...          20     18.0     18.0

"""

# df.dropna(inplace=True,axis=1)
# print(df)

"""
                     Names  DMBI_IA2  WEBX_IA2  AIDS-1_IA2
0   AMBERKAR KOMAL SURYAKANT        17        13          17
1  ARLEKAR PRATHAMESH MAHESH        10        15          15
2       AYARE DARSHAN NARESH        13        17          15
3       AYARE SANIA NARENDRA        14        12          19
4       BACHIM ATHARV MARUTI        12        14           8
5        BHATKAR SAHIL VILAS        12        14          15
6           BHOMBAL ZIA AMIR        13         9          18
7     BHUJBAL YUKTA SADASHIV         8        10          18
8    DABHOLKAR PRACHI PRADIP        14        19          18
9       DAMALE KEDAR PRAVIN         16        20          20
"""

#filling the null values with some data instead of dropping them

# df.fillna(value,inplace=True)

# df.fillna(0,inplace=True)
# print(df) #all null values will be replaced by 0 all means all even the columns with different datatype

#filling out null values of specific columns with mean mode median

# df['DMBI_IA1'].fillna(df['DMBI_IA1'].mean(), inplace=True)#this may give you a warning 
df['DMBI_IA1'] = df['DMBI_IA1'].fillna(df['DMBI_IA1'].mean()) #its better to use assignment 
print(df)#there are methods such as median mode also

# 3.interpolation
#filling null values with interpolation i.e estimation

# 10
# 20
# None  estimation will will for example 30
# 40
# 50

#we can use various inteploation methods like linear polynomial and many more

# df.interpolate(method='linear',axis=0,inplace=0)#linar,polynomial,time#axis 0 means interpolation will happen accoriding to rows

data={
    
    "Time":[1,2,3,4,5],
    "Value":[10,None,None,None,90]
}
df=pd.DataFrame(data)

print(df)
print("after interpolation")

df['Value']=df['Value'].interpolate(axis=0,method='linear')
print(df)

"""

[10 rows x 11 columns]
   Time  Value
0     1   10.0
1     2    NaN
2     3   30.0
3     4   60.0
4     5   90.0
after interpolation
   Time  Value
0     1   10.0
1     2   20.0
2     3   30.0
3     4   60.0
4     5   90.0
"""