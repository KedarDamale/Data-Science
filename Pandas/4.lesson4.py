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
#creating a column of our own lets say average of two marks of DMBVI subject

# df['Average_DMBI']=((df["DMBI_IA1"]+df["DMBI_IA2"])/2)


# #WE CAN USE DIFFERNT FUNCTION SUCH AS FLOOR OR CEIL TO ROUND TOO
# import numpy as np
# df['Average_DMBI']=np.ceil(((df["DMBI_IA1"]+df["DMBI_IA2"])/2))

#print(df.tail(5))


#inserting data using insert() method

# df.insert(location,"column name",data)

# df.insert(0,"StudentID",[1,2,3,4,5,6,7,8,9,10])

# print(df.tail(5))

"""
   StudentID                    Names  DMBI_IA1  ...  EHF_IA1  EHF_IA2  Average_DMBI
5          6      BHATKAR SAHIL VILAS         6  ...       10       14           9.0
6          7         BHOMBAL ZIA AMIR         8  ...       11       14          11.0
7          8   BHUJBAL YUKTA SADASHIV        10  ...        9       18           9.0
8          9  DABHOLKAR PRACHI PRADIP        18  ...       14       17          16.0
9         10     DAMALE KEDAR PRAVIN         17  ...       18       18          17.0

"""
#insertion using assignment wont have a control where the column will be inserted but in insert method we have that control

import numpy as np
df.insert(4,"DMBI-Average",np.ceil((df['DMBI_IA1']+df["DMBI_IA2"])/2))

print(df[df['DMBI-Average'] > 16]['Names'].to_string(index=False).strip().split(" ")[1])


