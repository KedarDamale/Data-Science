#sorting and aggregation

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

# #sorting : arragning the data bsed on something

# # 1.#sorint data in one column

# # df.sort_values(by='column_name',ascending=True or false , true if ascending ,inplace)

# # df.sort_values(by='DMBI_IA1',inplace=True,ascending=False)
# # print(df)
# """
#                       Names  DMBI_IA1  DMBI_IA2  ...  AIDS-1_IA2  EHF_IA1  EHF_IA2
# 8    DABHOLKAR PRACHI PRADIP        18        14  ...          18       14       17
# 9       DAMALE KEDAR PRAVIN         17        16  ...          20       18       18
# 3       AYARE SANIA NARENDRA        16        14  ...          19       14       16
# 0   AMBERKAR KOMAL SURYAKANT        10        17  ...          17       11       15
# 2       AYARE DARSHAN NARESH        10        13  ...          15       10       16
# 7     BHUJBAL YUKTA SADASHIV        10         8  ...          18        9       18
# 1  ARLEKAR PRATHAMESH MAHESH         9        10  ...          15       10       16
# 4       BACHIM ATHARV MARUTI         8        12  ...           8       13       16
# 6           BHOMBAL ZIA AMIR         8        13  ...          18       11       14
# 5        BHATKAR SAHIL VILAS         6        12  ...          15       10       14
# """
# #depending on dmbi ia1 marks we got sorted order of entire dataframe

# #2.sorting based on multiple columsn

# """
# Sorting on two columns in Pandas means you are asking the DataFrame to:

# First, sort by the values in column A.

# Then, if there are duplicate values in column A, sort those rows by values in column B.

# This is called multi-level (lexicographical) sorting.

# """

# # df.sort_values(by=['DMBI_IA2','DMBI_IA1'],inplace=True,ascending=[False,True])#[flase,true] are two differnt operations for both sorting columns
# # print(df)

# # #data aggregsaion

# """
# Data aggregation is the process of summarizing or grouping data to produce meaningful statistics or metrics.

# It typically answers questions like:

# What is the average score per student?

# What is the total revenue per region?

# What is the maximum marks obtained in each subject?

# """

# # df['columnnane'].mean()/sum()/min()/max() etc etc

# dmbi_df=df[['Names','DMBI_IA1','DMBI_IA2']]
# dmbi_df.insert(3,'DMBI_average',(dmbi_df['DMBI_IA1']+dmbi_df['DMBI_IA1'])/2)
# print(dmbi_df)
# """
#                        Names  DMBI_IA1  DMBI_IA2  DMBI_average
# 0   AMBERKAR KOMAL SURYAKANT        10        17          10.0
# 1  ARLEKAR PRATHAMESH MAHESH         9        10           9.0
# 2       AYARE DARSHAN NARESH        10        13          10.0
# 3       AYARE SANIA NARENDRA        16        14          16.0
# 4       BACHIM ATHARV MARUTI         8        12           8.0
# 5        BHATKAR SAHIL VILAS         6        12           6.0
# 6           BHOMBAL ZIA AMIR         8        13           8.0
# 7     BHUJBAL YUKTA SADASHIV        10         8          10.0
# 8    DABHOLKAR PRACHI PRADIP        18        14          18.0
# 9       DAMALE KEDAR PRAVIN         17        16          17.0

# """

# print(f"Average of DMBI averages is {dmbi_df['DMBI_average'].mean()}") #Average of DMBI averages is 11.2

# print(f"Median of DMBI averages is {dmbi_df['DMBI_average'].median()}")#Median of DMBI averages is 10.0

# print(f"Standard deviation of DMBI averages is {dmbi_df['DMBI_average'].std()}") #Standard deviation of DMBI averages is 4.211096452627668

# print(f"Maximum of DMBI averages is {dmbi_df['DMBI_average'].max()}") #Maximum of DMBI averages is 18.0

# print("Names of people who achive maximum marks")
# maximum=dmbi_df['DMBI_average'].max()
# print(dmbi_df.loc[dmbi_df['DMBI_average']>=maximum-1,['Names']].to_string(index=False))

#Grouping groupping data based on something (same as groupby caluse in sql)

#e.g give me avergae score of student based on all exams
#give me the lowest score of each student in all exams somrthing like htis

# syntax: dtaframe.groupby(clumnname)[aggregation]
import pandas as pd


data = {
    "Student": [
        "Alice", "Bob", "Charlie", "David", "Eva",
        "Alice", "Bob", "Charlie", "David", "Eva"
    ],
    "Semester": [
        "Sem1", "Sem1", "Sem1", "Sem1", "Sem1",
        "Sem2", "Sem2", "Sem2", "Sem2", "Sem2"
    ],
    "Subject": [
        "Math", "Math", "Math", "Math", "Math",
        "Math", "Math", "Math", "English", "Math"
    ],
    "Marks": [85, 78, 92, 70, 88, 90, 75, 95, 80, 84]
}

df = pd.DataFrame(data)


#print(df.groupby('Subject')['Marks'].sum())
"""
Subject
English    80.000000
Math       84.111111
Name: Marks, dtype: float64

process:
first data will be grouped depending on the column

englis:[all english maeks marks]
maths[all math maeks marks]

and then aggregation will happen
"""


data={
    "Names":["AMBERKAR KOMAL SURYAKANT","ARLEKAR PRATHAMESH MAHESH","AYARE DARSHAN NARESH",
             "AYARE SANIA NARENDRA","BACHIM ATHARV MARUTI","BHATKAR SAHIL VILAS","BHOMBAL ZIA AMIR",
             "BHUJBAL YUKTA SADASHIV","DABHOLKAR PRACHI PRADIP"," DAMALE KEDAR PRAVIN "],
    "Age":[20,20,20,21,21,20,21,20,21,21],
    
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

print(df.groupby('Age')['DMBI_IA1'].mean())
"""
Age
20     9.0
21    13.4

Basically in group by what happens is Dave Group by column name is age in 
above example so when this is interpreted basically all the data that there is will 
be selected based on the edges which means we have 20 and 21 in ages so all the data 
will be separated in 20 and 21 and then we are giving the only column which is dmbi I 
one as input for aggregation function so that aggregation function basically will just 
take out the dmbi I have one column and it will call mean function that is average 
function on that particular column which is bifurgated already between columns of our group by function
"""

#grouping for two columns

print(df.groupby(['Age','Names'])['DMBI_IA1'].mean())

"""
ge  Names                    
20   AMBERKAR KOMAL SURYAKANT     10.0
     ARLEKAR PRATHAMESH MAHESH     9.0
     AYARE DARSHAN NARESH         10.0
     BHATKAR SAHIL VILAS           6.0
     BHUJBAL YUKTA SADASHIV       10.0
21    DAMALE KEDAR PRAVIN         17.0
     AYARE SANIA NARENDRA         16.0
     BACHIM ATHARV MARUTI          8.0
     BHOMBAL ZIA AMIR              8.0
     DABHOLKAR PRACHI PRADIP      18.0
Name: DMBI_IA1, dtype: float64
"""
#grouping using two aggregations

print(df.groupby(['Age'])[['DMBI_IA1', 'DMBI_IA2']].mean())

print(df.groupby(['Age']).agg({  ##agg function to apply difffernt aggregation
    'DMBI_IA1': 'min',
    'DMBI_IA2': 'max'
}))


