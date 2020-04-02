#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:50:10 2020

@author: furkan
"""

from rent import CarRent, BikeRent, Costumer


bike = BikeRent(100)
car = CarRent(10)
costumer =Costumer()


main_menu = True

while True:
    if main_menu:
        print("""
                  ***** Vehicle Rental Shop *****
                  A. Bike Menu
                  B. Car Menu
                  Q. Exit
                  """)
        main_menu = False
             
        choice = input("Enter choice: ")
        
    if choice == "A" or choice == "a":
        print("""
              ***** BIKE MENU *****
              1. Display available bikes
              2. Request a bike on hourly basis $5
              3. Request a bike on daily basis $84
              4. Return a bike
              5. Main Menu
              6. Exit
              """)
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not an integer")
            continue
        
        if choice == 1:
            bike.displayStock()
            choice = "A"
            
        elif choice == 2:
            costumer.rentalTime_b = bike.rentHourly(costumer.requestVehicle("bike"))
            costumer.rentalBasis_b = 1
            main_menu = True
            print("-------------------------------")
            
        elif choice == 3:
            costumer.rentalTime_b = bike.rentDaily(costumer.requestVehicle("bike"))
            costumer.rentalBasis_b = 2
            main_menu = True
            print("-------------------------------")
            
        elif choice == 4:
            costumer.bill = bike.returnVehicle(costumer.returnVehicle("bike"), "bike")
            costumer.rentalBasis_b, costumer.rentalTime_b, costumer.bikes = 0, 0, 0
            main_menu = True
            
        elif choice == 5:
            main_menu = True
            
        elif choice == 6:
            break
        
        else:
            print("Invalid input. Please enter a number between 1-6")
            main_menu = True
            
    elif choice == "B" or choice == "b":
        print("""
              ***** BIKE MENU *****
              1. Display available cars
              2. Request a car on hourly basis $10
              3. Request a car on daily basis $84
              4. Return a car
              5. Main Menu
              6. Exit
              """)
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not an integer")
            continue
        
        if choice == 1:
            car.displayStock()
            choice = "B"
            
        elif choice == 2:
            costumer.rentalTime_c = car.rentHourly(costumer.requestVehicle("car"))
            costumer.rentalBasis_c = 1
            main_menu = True
            print("-------------------------------")
            
        elif choice == 3:
            costumer.rentalTime_c = car.rentDaily(costumer.requestVehicle("car"))
            costumer.rentalBasis_c = 2
            main_menu = True
            print("-------------------------------")
            
        elif choice == 4:
            costumer.bill = car.returnVehicle(costumer.returnVehicle("car"), "car")
            costumer.rentalBasis_c, costumer.rentalTime_c, costumer.cars = 0, 0, 0
            main_menu = True
            
        elif choice == 5:
            main_menu = True
            
        elif choice == 6:
            break
        
        else:
            print("Invalid input. Please enter a number between 1-6")
            main_menu = True
            
            
    elif choice == "Q" or choice == "q":
        break
    
    else:
        print("Invalid Input. Please Enter A-B-Q")
        main_menu = True
    
    print("Thank you for using rental shop")
    
    