#Iterating means going through elements one by one

import numpy as np

#iterating over 1d arrays using for loops
a=np.array([1,2,3,4,5,6])

for i in a:
    print(i,end=" ")
print() #1 2 3 4 5 6 

#iterating over 2d arrays using for loops

b=np.array([[1,2,3,4],[5,6,7,8]])

for i in b:
    for j in i:
        print(j,end=" ")
    print()
    
#here i will iterate over the arrays and j will itrerate over elements present in i i,re array 
# 1 2 3 4 
# 5 6 7 8 

# basically if there are 1d arrays then itration will be 1 if 2 then we require 2 loops if nd array then n loops

#to solve this loop mess numpy support a method named nditer()

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#here we have 3d array
print(arr.ndim)

#to iterate over this means to access scalars i.e single quantity we have to have write 3 for loop nditer() minimizes that

for x in np.nditer(arr):
    print(x ,end=" ") #1 2 3 4 5 6 7 8 
print()
# our work is done in one for loop

for x in np.nditer(arr[:, ::2]):
  print(x ,end=" ")
print() #1 2 5 6 

"""
we can also skip elements using arry slicing this means get all the arrays but for elements that is innermost get all the elements skipping one

"""
#we can also get array with our preffered datatype by op_dtype which will convert the array not inplace that why we need flags argumetnts to execute this in buffer and not with original array
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x,end=" ")
print()



#enumerate method basically maps each iteration as a counter so you have to manually maintain a counter in vaniall a python
arr=[23,45,67,89]

for i,j in enumerate(arr):
    print(f"{i}: {j}",end=" ")
print()  #0: 23 1: 45 2: 67 3: 89 

#numpy also provides us with ndenumerate() function whihc also can map sequences in nd arrays in one loop

a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(np.ndim(a))

for idx,i in np.ndenumerate(a):
    print(f"id:{idx},element:{i}")
print()

"""
id:(0, 0, 0),element:1 #0th outermost array i.e 1st 2d array , 0th element in 2d arrays that is 1st id array and oth element in that 1d array i.r 1 , it return a tuple of indeices
id:(0, 0, 1),element:2
id:(0, 0, 2),element:3
id:(0, 1, 0),element:4
id:(0, 1, 1),element:5
id:(0, 1, 2),element:6
id:(1, 0, 0),element:1
id:(1, 0, 1),element:2
id:(1, 0, 2),element:3
id:(1, 1, 0),element:4
id:(1, 1, 1),element:5
id:(1, 1, 2),element:6
"""