'''
This program will calculate meal price
including tax and tip
Author: GA Sauer
Date:  3/19/16
'''

import os

mealCost = float(input("Enter the cost of the meal:  "))
tipPercent = int(input("Enter the percentage of time you would like:  "))
taxPercent = int(input("Enter the tax percent:  "))


totalCost = mealCost + (mealCost * (tipPercent/100)) + (mealCost * (taxPercent/100))
totalCost = round(totalCost)

print("The total cost of your meal including tax and tip is:  " + str(totalCost))