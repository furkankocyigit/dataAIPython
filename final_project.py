#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 01:19:33 2020

@author: furkan
"""


from abc import ABC, abstractmethod

class Shape(ABC):
    # Shape = super cass / abstract class

    @abstractmethod #abstract method
    def area(self): pass
    
    @abstractmethod
    def perimeter(self): pass
    
    #overriding and polymorphism
    def toString(self): pass

#child
class Square(Shape):
    # sub class
    
    def __init__(self, edge):
        
        self.__edge = edge  #encapsulation private attribute
        
    def area(self):
        
        result = self.__edge ** 2
        print("Square area: ", result)
        
    def perimeter(self):
        result = self.__edge * 4
        print("Square perimeter: ", result)
     
    #override and polymorphism
    def toString(self):
        print("this is square")
        
    
    
    
    
    
    
#child 
class Circle(Shape):
    #circle class
    
    #constant variable
    PI = 3.14
    
    def __init__(self, radius):
        self.__radius = radius
    
    
    def area(self):
        
        result = self.PI * self.__radius ** 2
        print("Circle area: ", result)
    
    def perimeter(self):
        
        result = 2 * self.PI * self.__radius
        print("Circle perimeter: ", result)
    
    def toString(self):
        print("This is a Circle")
        
        
        
        
c = Circle(5)
c.area()
c.perimeter()
c.toString()

s = Square(5)
s.area()
s.perimeter()
s.toString()