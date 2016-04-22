"""
This script will :

1. Insert a new column from data merged from two files
2. Export it to a new csv file

author:  GA Sauer
date:    April 22, 2016
"""
import os
import pandas

dir = "/Users/GAMac/pythonPractice/ExerciseFive/"
rightFile = "IncomeByStateByYearNoDupl.csv"
leftFile = "Geoids and states.csv"
outputFile = "E5_Income-By-State-State-Columns.csv"


def addStateColumns(dir, rightFile, leftFile, outputFile):
    #change working directory
    os.chdir(dir)
        
    #read in rightFile into a dataframe
    rightFrame = pandas.read_csv(rightFile, header = 0)
    
    #read in leftFile into a dataframe
    leftFrame = pandas.read_csv(leftFile, header = 0)
    
    #create new column from two existing columns
    mergedFrame = pandas.merge(leftFrame, rightFrame, on = "GEOID")
    
    
    '''Check to see if file already exists, if so delete it 
    and then export updated dataframe to new CSV file'''
    if os.path.isfile(outputFile):
        os.remove(outputFile)
        mergedFrame.to_csv(outputFile, index = None)
    else:
       mergedFrame.to_csv(outputFile, index = None) 
    


addStateColumns(dir, rightFile, leftFile, outputFile)
