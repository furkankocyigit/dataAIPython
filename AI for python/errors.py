# -*- coding: utf-8 -*-
"""
Created on Mon May 25 21:50:22 2020

@author: u23c37
"""



#%% 
# Exceptions

a = 10
b = "2"

liste = [1,2,3]
print(sum(liste))
#print(a+b)
print(str(a) + b)

k = 10
zero = 0
#print(k / zero)

try:
    a = k / zero
except ZeroDivisionError:
    a = 0
    

#index error
list1 = [1,2,3,4]
#list1[15]

#module not found
import numpyyyy

#file not found error
import pandas as pd
pd.read_csv("asd")

#type error
"2" + 2

#value error
int("sad")



try:
    1 / 0
except:
    print("except")
else:
    print("else")
finally:
    print("done")