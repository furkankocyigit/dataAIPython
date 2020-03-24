#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 05:07:35 2020

@author: furkan
"""


class Employee:
    
    def __init__(self, salary, raisePercentage):
        self.salary = salary
        self.raisePercentage = raisePercentage
    
    def raisee(self):
        self.salary =self.salary + self.salary * self.raisePercentage
        print("employee new salary: ", self.salary)
        
    
class CompEng(Employee):
    
    def __init(self, salary, raisePercentage):
        
        Employee._init(self, salary, raisePercentage)
   
    def raisee(self):
        self.salary =self.salary + self.salary * self.raisePercentage
        print("Computer Engineer new salary: ", self.salary)
        
        
class EEE(Employee):
    
    def __init(self, salary, raisePercentage):
        
        Employee._init(self, salary, raisePercentage)
   
    def raisee(self):
        self.salary =self.salary + self.salary * self.raisePercentage
        print("EEE new salary: ", self.salary)
    
e1 = Employee(1000, 0.1)
e1.raisee()     

ce = CompEng(1000, 0.2)
ce.raisee()

eee = EEE(1000, 0.3)
eee.raisee()
