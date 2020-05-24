#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 04:31:48 2020

@author: furkan
"""


from abc import ABC, abstractmethod

class Animal(ABC): # super class
    
    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def eat(self): pass


# a = Animal() error cannot initiate object from abstract class
    
class Bird(Animal): #sub class
    
    def __init__(self):
        print("bird created")
        
    def walk(self):
        print("bird is walking")
        
    def eat(self):
        print("bird is eating")
        
        
b1 = Bird()

    
    