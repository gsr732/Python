"""
This script will :

1.  Open the CSV file in Python as a pandas dataframe.
2.  Get the current exchange rate from https://currency-api.appspot.com
3.  Add two columns into the dataframe. One of them should contain the household median income 
in Euros and the other one in British pounds (using the rates obtained from site above)
4.  Export the updated dataframe back to a new CSV file.

author:  GA Sauer
date:    March 22-23, 2016
"""
import os
import pandas
import requests

dir = "/Users/GAMac/pythonPractice/DataAnalysis/"
fileName = "Income-By-State-1984.csv"
exRateUrl = 'https://currency-api.appspot.com/api/%s/%s.json'
sourceRate = 'USD'
targetRates = ['EUR', 'GBP']


#Get rates for Euros and British pounds
for rates in targetRates:
    url = ('https://currency-api.appspot.com/api/%s/%s.json') % (sourceRate, rates)
    r = requests.get(url)
    if rates == 'EUR':
        euroRate = r.json()['rate']
    else:
        if rates == 'GBP':
            britRate = r.json()['rate']
            
#Change working directory
os.chdir(dir)

#Open CSV file as pandas dataframe
dataFrame1 = pandas.read_csv(fileName)

#Create list for currencies
currency = ['_Euros', '_Pounds']

#Add new columns to dataframe that holds one for Euros and one for Pounds
for curType in currency:
    if curType == '_Euros':
        dataFrame1['medianIncome' + curType] = dataFrame1['1984']*euroRate
    else:
        if curType == '_Pounds':
            dataFrame1['medianIncome' + curType] = dataFrame1['1984']*britRate

#Check to see if file already exists, if so delete it 
#and then export updated dataframe to new CSV file
if os.path.isfile(fileName.split('.')[0] + "_" + currency[0] + "_" + currency[1] + ".csv"):
    os.remove(fileName.split('.')[0] + "_" + currency[0] + "_" + currency[1] + ".csv")
    dataFrame1.to_csv(fileName.split('.')[0] + "_" + currency[0] + "_" + currency[1] + ".csv")
else:
     dataFrame1.to_csv(fileName.split('.')[0] + "_" + currency[0] + "_" + currency[1] + ".csv")




