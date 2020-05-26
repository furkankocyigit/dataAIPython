# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:28:03 2020

@author: u23c37
"""

import numpy as np

# numpy basics
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(array.shape)

a = array.reshape(3,5)
print("shape: ",a.shape)
print("dimension: ", a.ndim)

print("data type: ", a.dtype.name)
print("size: ", a.size)

print("type: ", type(a))

np.zeros((3,4))
np.ones((3,4))

np.empty((2,3))

b = np.arange(10,50,5)
print(b)

c = np.linspace(10,50,20)
print(c)

# %% numpy basic operations

a = np.array([1,2,3])
b = np.array([1,2,3]) 

print("a + b: " , a + b)
print("a - b: " , a - b)
print("a ** 2: ", a ** 2)

print(np.sin(a))

print("a<2: " , a<2)



a = np.array([[1,2,3], [4,5,6]])
b = np.array([[1,2,3], [4,5,6]])

#element wise product
print("a*b: ", a*b)

#matrix product

print("a.b: ", a.dot(b.T))

print("np.exp(a): ", np.exp(a))

a = np.random.random((5,5))
print(a)
print("sum: ",a.sum())
print("max: ",a.max())
print("min: ",a.min())
print("colomnSum: ",a.sum(axis = 0))
print("rowSum: ",a.sum(axis = 1))

# %% indexing and slicing

array = np.array([1,2,3,4,5,6,7])  # vector

reverse_array = array[::-1]
print( "reverse array: ",reverse_array)

array1 = np.array([[1,2,3,4,5],
                   [6,7,8,9,10]])
print(array1[1,1])
print(array1[:,1])
print(array1[1,1:4])

#%% Shape manupilation

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
a = array.ravel()
print(a)
array2 = a.reshape(3,3)
print(array2)

# %% Stacking arrays

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

array3 = np.vstack((array1,array2))
array4 = np.hstack((array1,array2))

print(array3)
print(array4)

# %% convert and copy 

liste = [1,2,3,4]

array = np.array(liste)

liste2 = list(array)

a = np.array([1,2,3])

b = a
b[0] = 5
c = a
print("a: ", a)
print("b: ", b)
print("c: ", c)

d = np.array([1,2,3])

e = d.copy()
e[0] = 5
f = d.copy()

print("d: ", d)
print("e: ", e)
print("f: ", f)







