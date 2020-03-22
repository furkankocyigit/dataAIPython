#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:14:32 2020

@author: furkan
"""


class Animal:
    
    def __init__(self):
        print("animal is created")
        
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animal is walking")
        
#child

class Monkey(Animal):
    
    def __init__(self):
        super().__init__() #use init of parent
        print("monkey is created")
        
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey is climbing")
 
class Bird(Animal):
    
    def __init__(self):
        super().__init__()
        print("bird is created")
        
    def fly(self):
        print("bird is flying")
        
       
#       
m1 = Monkey()    
m1.toString()
m1.walk()
m1.climb()
print("------------")
b1 = Bird()
b1.walk()
b1.fly()