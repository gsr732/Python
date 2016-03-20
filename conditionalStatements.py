'''
Conditional statements to check if number is even and falls 
between a certain range of numbers.
Author: GA Sauer
Date:  3/20/16
'''

import os

def numberCheck(weirdNum):
    if weirdNum % 2 == 0  and (weirdNum >= 2 and weirdNum  <= 5):
        print("Not Weird.")
    elif weirdNum % 2 == 0  and (weirdNum >= 6 and weirdNum  <= 20):
        print("Weird.")
    elif weirdNum % 2 == 0  and (weirdNum > 20):
        print("Not Weird ")
    else:
        print("Weird")
    return;

while True:
  try:
    weirdNum = int(input("Enter any number: "))       
  except ValueError:
     print("Not an integer!")
     continue
  else:
     #print("Yes an integer!")
     break 

numberCheck(weirdNum)     
