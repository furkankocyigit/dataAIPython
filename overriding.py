#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 04:57:42 2020

@author: furkan
"""


class Animal: # parent
    
    def toString(self):
        print("animal")
        
class Monkey(Animal):
    
    def toString(self):
        print("monkey")
        
a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString() 
'''monkey calls overriding method and calls own function not
super class function'''
