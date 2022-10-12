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
    miles_To_Gas_Station = round(random.uniform(1,25),1)
    if gas_Level_Indicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1.5)
        print("Calling Emergncy Contact")
    elif gas_Level_Indicator == "Low":
        print("***WARNING***")
        sleep(1.5)
        print("Your gas tank is extremely low, checking google maps for the closest gas station")
        sleep(1.5)
        print("The closest gas station is" , list_Of_Gas_Stations(),"which is",miles_To_Gas_Station,"miles away.")


gas_Level_Alert()
