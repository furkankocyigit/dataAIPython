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