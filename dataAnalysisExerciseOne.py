"""
This script will :

1. Open the Excel file in Python as a pandas dataframe. 
2. Insert another parameter for skipping the first three rows
3. Export the dataframe to a CSV file. 
4. Declare that the index is at position 0.

author:  GA Sauer
date:    March 22, 2016
"""

import pandas
import os


dir = "/Users/GAMac/pythonPractice/DataAnalysis/"
fileName = "Income-By-State-1984.xls"

#Change working directory
os.chdir(dir)

#Open the Excel file in Python as a pandas dataframe
dataFrameOne = pandas.read_excel(fileName,skiprows=[0,1,2])

'''
Export the dataframe to a CSV file. 
Note that the CSV should not contain the first three header lines
'''
dataFrameOne.to_csv("Income-By-State-1984.csv",index=0)


