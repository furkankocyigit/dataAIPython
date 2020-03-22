#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:45:45 2020

@author: furkan
"""


class BankAccount(object):
    
    def __init__(self, name, money, address):
        self.__money = money #private
        self.name = name     #public
        self.address = address
    
    #get and set
    def getMoney(self):
        return self.__money
        
    
    def setMoney(self, amount):
        self.__money = amount
    #private   
    def __increase(self, amount):
        self.__money += amount 

p1 = BankAccount("messi", 1000, "barcelona")
p2 = BankAccount("neymar", 2000, "barcelona")

print("get method: ",p1.getMoney())
p1.setMoney(2500)
print("after set method: ",p1.getMoney())

# p1.__increase(300)
# print("after inc method: ", p1.getMoney())