#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 08:12:06 2020

@author: furkan
"""
import datetime

# parent class
class VehicleRent:
    
    def __init__(self, stock):
        
        self.__stock = stock
        self.now = 0
    
    def displayStock(self):
        """
            Display Stock
        
        """
        print("{} vehicle avaliable to rent".format(self.__stock))
        return self.__stock
    
    def rentHourly(self, n):
        """
            Rent hourly
        """
        if n <= 0:
            print("Number should be positive")
            return None
        
        elif n > self.__stock:
            print("Sorry {} vehicle available to rent".format(self.__stock))
            return None
        
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for hourly at {} hours".format(n, self.now.hour))
            
            self.__stock -= n
            
            return self.now
        
    def rentDaily(self, n):
        """
            Rent daily
        """
        if n <= 0:
            print("Number should be positive")
            return None
        
        elif n > self.__stock:
            print("Sorry {} vehicle available to rent".format(self.__stock))
            return None
        
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for daily at {} hours".format(n, self.now.hour))
            
            self.__stock -= n
            
            return self.now
        
    
    def returnVehicle(self, request, brand):
        '''
            return a bill
        '''
        car_h_price  = 10 
        car_d_price  = car_h_price * 8 / 10 * 24
        bike_h_price = 5
        bike_d_price = bike_h_price * 7 / 10 *24
        
        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        
        
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.__stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = abs(now - rentalTime)
                
                if rentalBasis == 1: #hourly
                    bill = rentalPeriod.seconds / 3600 * car_h_price * numOfVehicle
                    
                elif rentalBasis == 2: #daily
                    bill = rentalPeriod.seconds / (3600 * 24) * car_d_price * numOfVehicle
                    
                if numOfVehicle >= 2:
                    print("You have extra 20% discount")
                    bill = bill * 0.8
                
                print("Thank you for returning the rented vehicle")
                print("Price: {}$".format(bill))
                return bill
        
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.__stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = abs(now - rentalTime)
                
                if rentalBasis == 1: #hourly
                    bill = rentalPeriod.seconds / 3600 * bike_h_price * numOfVehicle
                    
                elif rentalBasis == 2: #daily
                    bill = rentalPeriod.seconds / (3600 * 24) * bike_d_price * numOfVehicle
                    
                if numOfVehicle >= 4:
                    print("You have extra 20% discount")
                    bill = bill * 0.8
                
                print("Thank you for returning the rented vehicle")
                print("Price: {}$".format(bill))
                return bill
        
        else:
            print("You did not rent a vehicle")
            return None
           
                 
     
        
 
    
#child class 1
class CarRent(VehicleRent):
    
    global discount_rate
    discount_rate = 15
    
    def __init__(self, stock):
        super().__init__(stock)
    
    def discount(self, b):
        
        '''
            discount
        '''
        bill = b - (b * discount_rate) / 100
 
    
    
#child class 2
class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)
    
# customer
class Costumer:
    
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
    
    def requestVehicle(self, brand):
        
        '''
            take a request bike or car fro m customer
        '''
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")
            try:
                bikes = int(bikes)
            except ValueError:
                print("Please enter an apropriate number!!")
                return -1
            
            if bikes < 1:
                print("Number of bikes should be greater than zero")
                return -1
            else:
                self.bikes = bikes
            
            return self.bikes
            
        elif brand == "car":
            cars = input("How many car would you like to rent?")
             
            try:
                cars = int(cars)
            except ValueError:
                print("Please enter an apropriate number!!")
                return -1
            
            if cars < 1:
                print("Number of cars should be greater than zero")
                return -1
            else:
                self.cars = cars
            
            return self.cars
        else:
            print("Request vehicle error")
        
    
    def returnVehicle(self, brand):
    
        '''
            return bikes or cars
        '''
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0, 0, 0
            
            
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0, 0, 0
            
        else:
            print("Return vehicle error")


        