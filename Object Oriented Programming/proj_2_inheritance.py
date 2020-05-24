#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 03:57:07 2020

@author: furkan
"""


class Website:
    #parent
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def loginInfo(self):
        print(self.name + " "  + self.surname)
        
        
class Website1(Website):
    #child
    def __init__(self, name, surname, id):
        Website.__init__(self, name, surname)
        self.id = id
        
    def login(self):
        print(self.name + " "  + self.surname + " " + self.id)
        
        
class Website2(Website):
    #child
    def __init__(self, name, surname, email):
        Website.__init__(self, name, surname)
        self.email = email
        
    def login(self):
        print(self.name + " "  + self.surname + " " + self.email)
        
p1 = Website('furkan', 'koc')

p2 = Website1('ali', 'ab', str(123))

p3 = Website2('ahmet', 'as', 'as@ab.com')