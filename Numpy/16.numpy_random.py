# # truly random= algorithm based randomness means next random can be predicted the data for these algorithms are keystrokes, mouse movements, data on network etc.
# #

# #pseudo random numbers=there is no random algorithms

# random library generates pseudo random numbers 

#numpy has its own random library

from numpy import random

print(random.randint(100)) #0-100 number will be generated
print(random.randint(100,size=10)) #an array of 0-100 number will be generated


print(random.rand()) #random float from 0 to 1
print(random.rand(10)) #generates an array of 10 random floats

#generating 2d arrays

print(random.randint(100,size=(2,3)))
#2 rows 3 columns 2d integer arrays
"""
[[85 55  5]
 [70 41 85]]
"""

print(random.rand(10,4))
"""
[[0.98601366 0.52067661 0.40319863 0.51084111]
 [0.34240045 0.07932649 0.59016252 0.26661166]
 [0.94477341 0.31290942 0.27096023 0.95972698]
 [0.51978613 0.55308817 0.50293303 0.05493515]
 [0.38874454 0.21047446 0.34380224 0.81048931]
 [0.05096302 0.37320631 0.62481443 0.70085459]
 [0.67843421 0.58691118 0.4773865  0.98884024]
 [0.09043754 0.52234991 0.59893659 0.66076933]
 [0.73224698 0.64106824 0.61295652 0.99167932]
 [0.81275122 0.51347805 0.30105462 0.22474532]]
 
 array of 10 rows 4 rows
"""

# generating random number from given array

print(random.choice([1,3,4,5,6,7,8]))

print(random.choice([1,3,4,5,6,7,8],size=(2,5)))

random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))#we can aslo set probsbility of getting chosen #note the sum of probabilities shoulld be one


#A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("Just shuffleing the given array")
random.shuffle(arr)
print(arr) #this will shuffle original  array
print("Permutation:")
print(random.permutation(arr)) #this won;t The permutation() method returns a re-arranged array (and leaves the original array un-changed).



