#Weather
#developer ; Dylan bellinger
#version 1.0

"""
create a function got our current weather using the 
random. choice function to determine what the weather is 
picking from a list - using if, elif & else statement 
to check the condition and print a specific print line
"""

#Import libraries here
import random

#Weather Condition list using the random.choice library
#to randomly choose a condition and storing it in its brain
def weather ():
    weather_Forcast = ["Rainy", "Snowy" , "Sunny" , "Cloudy" , "Foggy" , "Stormy" , "Icy"]
    weather_Condition = random.choice(weather_Forcast)
    print(weather_Condition)
    return weather_Condition




