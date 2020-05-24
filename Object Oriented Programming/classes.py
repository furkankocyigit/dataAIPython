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

# %% methods vs functions

class Emp(object):
    age = 25
    salary = 1000
    
    def ageSalaryRatio(self):
        print(self.age / self.salary)
        
def ageSalaryRatio(age, salary):
    print(age / salary)

       
e1 = Emp()
e1.ageSalaryRatio()

# %% initializer or constructor

class Animal(object):
       
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age
    def getName (self):
        print(self.name)


a1 = Animal("dog", 2)
a2 = Animal("cat", 4)
a3 = Animal("bird",6)
age = a1.getAge()

print(age)