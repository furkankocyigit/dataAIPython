#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:05:14 2020

@author: furkan
"""


# %% calculator project

class Calc(object):
    
    def __init__(self, a, b):
        #attribute
        self.value1 = a
        self.value2 = b
        
    
    def add(self):
        
        return self.value1 + self.value2
    
    def multiply(self):
        
        return self.value1 * self.value2
    def division(self):
        if self.value2 == 0:
            raise ValueError("Division by Zero")
        else:
            return self.value1 / self.value2

print("choose add(1) or multiply(2) or division(3)")
selection = input("select 1 or 2 or 3: ")


v1 = int(input("first value: "))
v2 = int(input("second value: "))



c1 = Calc(v1, v2)
if selection == "1":
    result = c1.add()
    print("result: {}".format(result))
elif selection == "2":
    result = c1.multiply()
    print("result: {}".format(result))
elif selection == "3":
    result = c1.division()
    print("result: {}".format(result))
else:
    print("there is no proper selection")

