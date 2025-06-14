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


#selecting a specific column:

print(df['Names'])
"""
0     AMBERKAR KOMAL SURYAKANT
1    ARLEKAR PRATHAMESH MAHESH
2         AYARE DARSHAN NARESH
3         AYARE SANIA NARENDRA
4         BACHIM ATHARV MARUTI
5          BHATKAR SAHIL VILAS
6             BHOMBAL ZIA AMIR
7       BHUJBAL YUKTA SADASHIV
8      DABHOLKAR PRACHI PRADIP
9         DAMALE KEDAR PRAVIN 
Name: Names, dtype: object
"""
#seelcting multiple columns : basically like a 2d array pass the arguments
print(df[['Names', 'AIDS-1_IA1']])

#filtering rows based on a condition

print(df["DMBI_IA1"]>15)
"""
0    False
1    False
2    False
3     True
4    False
5    False
6    False
7    False
8     True
9     True
Name: DMBI_IA1, dtype: bool

"""
#but we want it in dataframe format so we have to do boolean filtering which means we have to encase this in df[]

print(df[df['DMBI_IA1']>15])

"""
                     Names  DMBI_IA1  DMBI_IA2  ...  AIDS-1_IA2  EHF_IA1  EHF_IA2
3     AYARE SANIA NARENDRA        16        14  ...          19       14       16
8  DABHOLKAR PRACHI PRADIP        18        14  ...          18       14       17
9     DAMALE KEDAR PRAVIN         17        16  ...          20       18       18

[3 rows x 11 columns]
"""

#multiple conditions

fil_rows=df[(df['DMBI_IA1']>15) & (df['DMBI_IA2']>15)] #logical operators dont work we have to use & | ~ and more You cannot use and, or, not 
                                                       #because those are Python’s boolean operators and not designed to work element-wise on Series.
print(fil_rows)

"""
[3 rows x 11 columns]
                   Names  DMBI_IA1  DMBI_IA2  ...  AIDS-1_IA2  EHF_IA1  EHF_IA2
9   DAMALE KEDAR PRAVIN         17        16  ...          20       18       18

[1 rows x 11 columns]
"""
#selecting specific columns in where condition one columns
fil_rows=df[(df['DMBI_IA1']>15) & (df['DMBI_IA2']>15)]['Names'] 
print(fil_rows)
print(fil_rows.to_string(index=False))#this method will convert out dataframe into list and while doing that we can omit the index column 

##selecting specific columns in where condition multiple  columns

fil_rows = df[(df['DMBI_IA1'] > 15) & (df['DMBI_IA2'] > 15)][['Names', 'AIDS-1_IA2']]
print(fil_rows)
