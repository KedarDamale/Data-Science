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


#.loc() property
# syntax: df.loc[condition,columns]

#use1 - sort of like selct function to select columns based on a condition

# print(df.loc[(df['DMBI_IA1'] > 16) & (df['WEBX_IA1']>18), ['Names', 'DMBI_IA2']])

#use2: to update values

# syntax: df.loc[rowindex or condition , column anem]=new value

# df.loc[9,'Names']="Kedar Pravin Damale" #using 9 row index
# print(df.tail(1))

# df.loc[df['DMBI_IA1']>16,'Names']="Fucking legends" #using condition
# print(df.tail())

#although we can update multiple columns at once but it is recommende to use multiple loc satements and also rather using condition in loc put variable name to it and use that variable naem

# condition=(df['DMBI_IA1']>16) & (df['DMBI_IA2']>15)
# df.loc[condition,'Names']="Geniuses"
# print(df.tail(5))

#we can use normal assgigment to update many values

# df['DMBI_IA1']=df['DMBI_IA1']+2 #incrementing 2 marks for all
# print(df.tail())

#but if we want to precisly update something like updation based on a condition then loc
#incremeting marks by 2 for those who have failed

print(df.head(7))
df.loc[df['DMBI_IA1']<8,'DMBI_IA1']=df['DMBI_IA1']+2 #incrementing marks based on condition
print(df[['Names','DMBI_IA1']])
"""
Before:
5        BHATKAR SAHIL VILAS         6        12  ...          15       10       14
Afterr:
5        BHATKAR SAHIL VILAS         8        12  ...          15       10       14

"""

