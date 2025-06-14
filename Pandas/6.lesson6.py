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

#dropping columns and specific rows 

# df.drop(columns=[names of columns],inplace)
#if the inplace is true then it modies original df if false then we have to assign a separate variable for the new df

# df.drop(columns=['DMBI_IA1','DMBI_IA2'],inplace=True)
# print(df.head())
# """
#                        Names  WEBX_IA1  WEBX_IA2  ...  AIDS-1_IA2  EHF_IA1  EHF_IA2
# 0   AMBERKAR KOMAL SURYAKANT        17        13  ...          17       11       15
# 1  ARLEKAR PRATHAMESH MAHESH        18        15  ...          15       10       16
# 2       AYARE DARSHAN NARESH        17        17  ...          15       10       16
# 3       AYARE SANIA NARENDRA        20        12  ...          19       14       16
# 4       BACHIM ATHARV MARUTI        20        14  ...           8       13       16

# [5 rows x 9 columns]
# two columns have been dropped
# """

#to drop specific rows there is inverse method that is applied which means instead of dropping keep those who isnt getting dropped

condition=(df['DMBI_IA1'] < 15) & (df['DMBI_IA2'] < 15)

df=df[~condition]
print(df)


