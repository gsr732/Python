"""
This script will :

1. Rename GEOID columns to remove .# extension (GEOID.1, GEOID.13 etc)
2. Remove duplicate GEOID rows but keeping the first one
3. Export it to a new csv file

author:  GA Sauer
date:    March 23, 2016
"""
import os
import glob
import pandas

dir = "/Users/GAMac/pythonPractice/Income-By-State/"
inputFile = "Income-By-State-1984-2013.csv"
outputFile = "E4_Income-By-State-1984-2013.csv"


def dropDuplicates(dir, inputFile, outputFile):
    #change working directory
    os.chdir(dir)
    
    #read in csv file into a dataframe
    dataFrame3 = pandas.read_csv(inputFile, header = 0)
    
    #rename columns to not have .#s on GEOID columns
    dataFrame3.rename(columns = lambda x: x.split('.')[0], inplace=True)
    
    #drop duplicate columns
    dataFrame4 = dataFrame3.T.drop_duplicates().T
    
    '''Check to see if file already exists, if so delete it 
    and then export updated dataframe to new CSV file'''
    if os.path.isfile(outputFile):
        os.remove(outputFile)
        dataFrame4.to_csv(outputFile, index = None)
    else:
       dataFrame4.to_csv(outputFile, index = None) 
    


dropDuplicates(dir, inputFile, outputFile)
