#Gasoline
#programer : Dylan bellinger
# Version1.0

"""
Define a function to check are gas gauge and determine how far
 we have until we need gasoline based on an if, elif, else,
 condition
"""

#import libery here
import random
from time import sleep

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




gas_Level_Alert()
