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

for i,row in df.iterrows():
    print(f"{i}:{row}")
    
"""
0:Names         AMBERKAR KOMAL SURYAKANT
DMBI_IA1                            10
DMBI_IA2                            17
WEBX_IA1                            17
WEBX_IA2                            13
WT_IA1                              16
WT_IA2                              16
AIDS-1_IA1                          15
AIDS-1_IA2                          17
EHF_IA1                             11
EHF_IA2                             15
Name: 0, dtype: object
1:Names         ARLEKAR PRATHAMESH MAHESH
DMBI_IA1                              9
DMBI_IA2                             10
WEBX_IA1                             18
WEBX_IA2                             15
WT_IA1                               14
WT_IA2                               11
AIDS-1_IA1                           15
AIDS-1_IA2                           15
EHF_IA1                              10
EHF_IA2                              16
Name: 1, dtype: object
2:Names         AYARE DARSHAN NARESH
DMBI_IA1                        10
DMBI_IA2                        13
WEBX_IA1                        17
WEBX_IA2                        17
WT_IA1                          13
WT_IA2                          11
AIDS-1_IA1                      13
AIDS-1_IA2                      15
EHF_IA1                         10
EHF_IA2                         16
Name: 2, dtype: object
3:Names         AYARE SANIA NARENDRA
DMBI_IA1                        16
DMBI_IA2                        14
WEBX_IA1                        20
WEBX_IA2                        12
WT_IA1                          15
WT_IA2                          15
AIDS-1_IA1                      17
AIDS-1_IA2                      19
EHF_IA1                         14
EHF_IA2                         16
Name: 3, dtype: object
4:Names         BACHIM ATHARV MARUTI
DMBI_IA1                         8
DMBI_IA2                        12
WEBX_IA1                        20
WEBX_IA2                        14
WT_IA1                          17
WT_IA2                          16
AIDS-1_IA1                      13
AIDS-1_IA2                       8
EHF_IA1                         13
EHF_IA2                         16
Name: 4, dtype: object
5:Names         BHATKAR SAHIL VILAS
DMBI_IA1                        6
DMBI_IA2                       12
WEBX_IA1                       19
WEBX_IA2                       14
WT_IA1                         15
WT_IA2                         15
AIDS-1_IA1                     15
AIDS-1_IA2                     15
EHF_IA1                        10
EHF_IA2                        14
Name: 5, dtype: object
6:Names         BHOMBAL ZIA AMIR
DMBI_IA1                     8
DMBI_IA2                    13
WEBX_IA1                    18
WEBX_IA2                     9
WT_IA1                      14
WT_IA2                      13
AIDS-1_IA1                  12
AIDS-1_IA2                  18
EHF_IA1                     11
EHF_IA2                     14
Name: 6, dtype: object
7:Names         BHUJBAL YUKTA SADASHIV
DMBI_IA1                          10
DMBI_IA2                           8
WEBX_IA1                          14
WEBX_IA2                          10
WT_IA1                            18
WT_IA2                            16
AIDS-1_IA1                        17
AIDS-1_IA2                        18
EHF_IA1                            9
EHF_IA2                           18
Name: 7, dtype: object
8:Names         DABHOLKAR PRACHI PRADIP
DMBI_IA1                           18
DMBI_IA2                           14
WEBX_IA1                           20
WEBX_IA2                           19
WT_IA1                             19
WT_IA2                             18
AIDS-1_IA1                         17
AIDS-1_IA2                         18
EHF_IA1                            14
EHF_IA2                            17
Name: 8, dtype: object
9:Names          DAMALE KEDAR PRAVIN 
DMBI_IA1                         17
DMBI_IA2                         16
WEBX_IA1                         19
WEBX_IA2                         20
WT_IA1                           20
WT_IA2                           19
AIDS-1_IA1                       20
AIDS-1_IA2                       20
EHF_IA1                          18
EHF_IA2                          18
Name: 9, dtype: object

"""