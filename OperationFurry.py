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
def gaslevelGauge():
    gaslevelList = ["Empty" , "Low" , "Quarter Tank" , "Half Tank" , "Three Quarter Tank" , "Full Tank" ]
    currentGasLevel = random.choice(gaslevelList)
    print(currentGasLevel)
    return currentGasLevel

gaslevelGauge()