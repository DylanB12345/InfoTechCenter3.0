

#*******************************************************************************************
#Import libaries Here
from time import sleep #We Imported the Sleep funcition from the time libary

import random

#******************************************************************************************

#Welcome Screen
#Developer: Dylan Bellinger
#Version: 1.1

"""
Our Welcome Screen will start are our program letting
drivers know that the infoTechCenter OS is Loading
"""

print('\n\033[1;30m Welcome to Operation Fury InfoTech Center')
sleep(2)
print("\n\033[1;30m Operation Fury's Operating System is Booting Up")

for i in range(2):
    print("OS booting up.")
    sleep(1)
#***********************************************************************************

#Weather
#developer ; Dylan bellinger
#version 1.0

"""
create a function got our current weather using the 
random. choice function to determine what the weather is 
picking from a list - using if, elif & else statement 
to check the condition and print a specific print line
"""




#Weather Condition list using the random.choice library
#to randomly choose a condition and storing it in its brain
def weather ():
    weather_Forcast = ["Rain", "Snow" , "Sunny" , "Windy" , "Foggy" , "Stormy" , "Icy"]
    weather_Condition = random.choice(weather_Forcast)
    return weather_Condition

weatherAlert = weather()
#**********************************************************************************************************************
def vehicle_Response_System():
    if weatherAlert == "Icy":
        print("\vRS has changer your alarm 30 minutes earlier based on the NWS forcast of ",weatherAlert)
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\vRS has changer your alarm 15 minutes earlier based on the NWS forcast of ", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\vRS has changer your alarm 5 minutes earlier based on the NWS forcast of ", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\vRS has changer your alarm 5 minutes earlier based on the NWS forcast of ", weatherAlert)
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\vRS has changer your alarm 10 minutes earlier based on the NWS forcast of ", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Stormy":
        print("\vRS has changer your alarm 15 minutes earlier based on the NWS forcast of ", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    else:
        print("\nThe weather today is,", weatherAlert,"lets Gooo!")
        print("VRS will only allow your car to go 100MPH")

#**********************************************************************************************************************

#Gasoline
#programer : Dylan bellinger
# Version1.0

"""
Define a function to check are gas gauge and determine how far
 we have until we need gasoline based on an if, elif, else,
 condition
"""


# Gas level funtion
def gas_Level_Gauge():
    gaslevelList = ["Empty" , "Low" , "Quarter Tank" , "Half Tank" , "Three Quarter Tank" , "Full Tank" ]
    currentGasLevel = random.choice(gaslevelList)
    return currentGasLevel

# Variable calling the gas_Level_Guage function to store value once
gas_Level_Indicator = gas_Level_Gauge()

def list_Of_Gas_Stations():
    gasStation = ["Shell" , "Circle K" , "Marathon" , "Speedway" , "Meijer"]
    gas_Station_Nearby = random.choice(gasStation)
    return gas_Station_Nearby

def gas_Level_Alert():
    miles_To_Gas_Station_Low = round(random.uniform(1,25),1)
    miles_To_Gas_StationQuater_Tank = round(random.uniform(26, 50), 1)
    if gas_Level_Indicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1.5)
        print("Calling Emergncy Contact")
    elif gas_Level_Indicator == "Low":
        print("***WARNING***")
        sleep(1.5)
        print("Your gas tank is extremely low, checking google maps for the closest gas station")
        sleep(1.5)
        print("The closest gas station is" , list_Of_Gas_Stations(),"which is",miles_To_Gas_Station_Low,"miles away.")
    elif gas_Level_Indicator == "Quarter Tank":
        print("***WARNING***")
        sleep(1.5)
        print("Your gas tank is a quarter tank full, checking google maps to your nearest gas station")
        sleep(1.5)
        print("The closest gas station is", list_Of_Gas_Stations(), "which is", miles_To_Gas_StationQuater_Tank, "miles away.")
    elif gas_Level_Indicator == "Half Tank":
        sleep(1.5)
        print("Your gas tank is a Half Tank full, you have plenty of gas to get to your destination")
    elif gas_Level_Indicator == "Three Quarter Tank":
        sleep(1.5)
        print("Your gas tank is a Three QuarterTank full, you have plenty of gas to get to your destination")
    else:
        sleep(1.5)
        print("Your gas tank is full, you have plenty of gas to get to your destination")






#**************************************************************************************************************

#Call Functions Here ......
print()
gas_Level_Alert()

vehicle_Response_System()





