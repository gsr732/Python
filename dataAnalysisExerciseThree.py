"""
This script will :

Concate data from multiple XLS files into a single CSV file

author:  GA Sauer
date:    March 23, 2016
"""
import os
import glob
import pandas

dir = "/Users/GAMac/pythonPractice/Income-By-State/"
outputFile = "Income-By-State-1984-2013.csv"

#Create definition that concats 
def concatenate(dir, outputFile):
    #change working directory
    os.chdir(dir)
    #create a list of all the files
    fileList = glob.glob("*.xls")
    #create empty list to hold dataframes
    dfList = []
    for fileName in fileList:
        dataFrame2 = pandas.read_excel(fileName, skiprows = [0,1,2], header = None)
        dfList.append(dataFrame2)
        concatDataFrame2 = pandas.concat(dfList, axis = 1)#axis=0 for vertical
    #Check to see if file already exists, if so delete it 
    #and then export updated dataframe to new CSV file
    if os.path.isfile(outputFile):
        os.remove(outputFile)
        concatDataFrame2.to_csv(outputFile, index = None, header = None)
    else:
        concatDataFrame2.to_csv(outputFile, index = None, header = None)   


concatenate(dir, outputFile)
