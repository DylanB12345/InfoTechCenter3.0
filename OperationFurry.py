
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
    print(weather_Condition)
    return weather_Condition

weatherAlert = weather()

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
vehicle_Response_System()

