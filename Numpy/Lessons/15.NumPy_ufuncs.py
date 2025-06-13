import numpy as np

# # #ufuncs stand for universal functions and they are NumPy functions that operate on the ndarray object

# # # Converting iterative statements into a vector based operation is called vectorization. ufuncs help to achieve this

# # #there are several built in universal ufuncs that help us achieve vectorization

# # a=np.array([1,2,3])
# # b=np.array([1,2,3])

# # print(np.add(a,b)) #[2 4 6] 
# # print(a+b) #you can do this too but it will only add 2 ata time

# # #this is vectorization normal python would have joined two list instead of adding element

# # # custom ufuncs

# # # To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

# # def add(a,b):
# #     c=np.array([1,2,3])
# #     return (a+b)

# # #now define a fromfunc()

# # """
# # The frompyfunc() method takes the following arguments:

# # function - the name of the function.
# # inputs - the number of input arguments (arrays).
# # outputs - the number of output arrays.

# # """
# # add_arrays=np.frompyfunc(add,2,1) #here add is method 2 are the number of parameters and 1 is the nunmber of output arrays

# # print(add_arrays(np.array([1,2,3]),np.array([1,2,3])))#[2 4 6]

# # #to check if the function is ufucn that only workd for builkt in num,py ufunc not customo one

# # print(type(np.add))

# # #-------------------------------#

# # #simple arithmetic ufuncs

# # # You could use arithmetic operators + - * / directly between NumPy arrays, but it is recommened to use ufucs

# # arr1 = np.array([10, 11, 12, 13, 14, 15])
# # arr2 = np.array([20, 21, 22, 23, 24, 25])


# # print(np.add(arr1,arr2))#The add() function sums the content of two arrays, and return the results in a new array.

# # print(np.subtract(arr1,arr2))#The subtract() function subtracts the values from first array with the values from second array, and return the results in a new array.

# # print(np.multiply(arr1,arr2))#The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.

# # print(np.divide(arr1,arr2))#Divide the values in arr1 with the values in arr2:

# # print(np.power(arr1,arr2))#The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.

# # print(f"Mod: {np.mod(arr1,arr2)}\n Remainder: {np.remainder(arr1,arr2)}") #Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.

# # print(np.divmod(arr1, arr2)) #this return tuple of 2 nd arrays, 1 for quotients and another for remiander so basically we can use 3 functions to find the remainder

# # arr3=[-1,-4,5,7,-5,-9]
# # print(np.abs(arr3))
# # print(np.absolute(arr3))#Both the absolute() and the abs() functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()


# # #----------------------------------------------------#

# # #rounding decimals

# # arr4=np.array([-3.1666, 3.6667]) #Remove the decimals, and return the float number closest to zero.
# # print(np.trunc(arr4)) #[-3.  3.]
# # print(np.fix(arr4)) #[-3.  3.]

# # print(np.around(arr4)) #[-3.  4.]
# # #The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

# # print(np.floor(arr4))#[-4.  3.]
# # #The floor() function rounds off decimal to nearest lower integer.

# # print(np.ceil(arr4))#[-3.  4.]

# # #The ceil() function rounds off decimal to nearest upper integer.


# # #-----------------------------------#
# # # logarithms

# # arr = np.arange(1, 10) #arrange() creates a numpy array from starting index to last index exclusing last index ofcourse#[1 2 3 4 5 6 7 8 9]

# # print(np.log2(arr)) #return log to the base 2 of each index

# # print(np.log10(arr)) #return log to the base 10 of each index

# # print(np.log(arr))#return log to the base e (normal log) of each index

# #numpy doesnt provide functions for any log just 10 2 and e so we can create one using math.log and ufunc
# import math

# def log_at_any_base(n,log):
#     return math.log(n,log)

# log_base=np.frompyfunc(log_at_any_base,2,1)

# print(log_base(100,15))





#---------------------------#\
    # summations are done with multiple arguments that means 2 or more additions happen wiht only two arguments


a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
c=np.array([11,12,13,14,15])

print(np.sum([a,b,c])) #120
print(np.sum([a,b,c],axis=1)) 
"""
[15 40 65]

axis 1 mean scolumns means columns will gets summes which means column a element=15
b and c will be 40 and 65 

"""
print(np.sum([a,b,c],axis=0)) 
"""
[18 21 24 27 30]
this is row wise summation means 1+6+11 =18 and so on
"""

#partial sum i.e cumulative sum

#The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].


print(np.cumsum(a)) #[ 1  3  6 10 15]

#there is a prod function which multiplyies thing like the sum adds it aslos supports different axis too also has cumprod() function


#discrete difference

# A discrete difference means subtracting two successive elements.

# E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]


arr = np.array([10, 15, 25, 5])

print(np.diff(arr)) #[  5  10 -20]

# we can do the same operation repertedly by giving a argument n

print(np.diff(arr ,n=2)) #[  5  10 -20] n=1
                         #[  5 -30] n=2

#finding lcm and gcd of numbers

a=34
b=67
print(np.lcm(a,b))#2278
print(np.gcd(a,b)) #1

#on 1d arrays
#as these are 1d arrays we need to reduce them to elemetal level as we need to find lcm or gcd of numbers

arr=np.array([1,2,3,4])

print(f"LCM: {np.lcm.reduce(arr)}") #LCM: 12
print(f"GCD: {np.gcd.reduce(arr)}") #GCD: 1


