'''
This program will prompt user for their name
ask age and calculate in how many years 
they will be 100
'''

from datetime import date
import os

#Prompt user for their name
name = input("What is your name?  ")

#Prompt user for their age
age = input("what is your age? ")

#Get today's date
currentDate = date.today()

#from currentDate parse year
currentYear = currentDate.year

when100 = ((100-int(age)))

print(name + ' you\'ll be 100 in ' + str(when100) + ' years!')

