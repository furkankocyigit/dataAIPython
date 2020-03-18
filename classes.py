# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Employee(object):
    #attribute = age, adress, name
    #behaviour = pass, shoot
    pass

employee1 = Employee()

# %% attributes


class Footballer:
    footbal_club = "barcelona"
    age = 30
    
f1 = Footballer()

print(f1.age)
print(f1.footbal_club) 

f1.footbal_club = "Real Madrid"
print(f1.footbal_club)

# %% methods

class Square(object):
    edge = 5 #meter
    area = 0
    
    def area1(self):
        self.area = self.edge * self.edge
        print("Area: ", self.area)
        
s1 = Square()
print(s1.area1())

s1.edge = 7
print(s1.area1())
