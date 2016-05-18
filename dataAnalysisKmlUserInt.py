"""
This script will :

Integrating user input inside the script. Once the user executes the program, 
it should prompt them to first enter the longitude, and then the latitude. 
The entered values should then serve as a pair of coordinates for the KML point.

author:  GA Sauer
date:    May 18, 2016
"""
import os
from sys import argv
import simplekml
from simplekml import Kml

#Set variables
user_name = argv
dir = "/Users/GAMac/pythonPractice/ExerciseKml/"
outputFile = "kmlUserInt.kml"
 

#Prompt user for name
user_name = input("Please enter your name:  ")

print("Hello, %s"  %  user_name)

#Prompt user for longitude from user
longi = input("Please enter the longitude for your location:  ") 

#Prompt user for latitude for user 
latit = input("Now please enter a latitude for your location:  ")

#Create empty kml object
kml = simplekml.Kml()

#Create new points using user enter longitude and latitude
kml.newpoint(name="userLocation",coords=[(longi,latit)]) 

#Change directory
os.chdir(dir)

'''Check to see if file already exists, if so delete it 
    and then save to kml file'''
if os.path.isfile(outputFile):
    os.remove(outputFile)
    kml.save(outputFile)
else:
    kml.save(outputFile)
    
print("The kml map file of your location has been created and is available here:  " + dir + outputFile)
