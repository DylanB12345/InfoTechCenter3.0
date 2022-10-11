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

# Gas level funtion
def gas_Level_Gauge():
    gaslevelList = ["Empty" , "Low" , "Quarter Tank" , "Half Tank" , "Three Quarter Tank" , "Full Tank" ]
    currentGasLevel = random.choice(gaslevelList)
    return currentGasLevel

# Variable calling the gas_Level_Guage function to store value once

gas_Level_Indicator = gas_Level_Gauge()

def gas_Level_Alert():
    if gas_Level_Indicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\nCalling Emergncy Contact")

gas_Level_Alert()
