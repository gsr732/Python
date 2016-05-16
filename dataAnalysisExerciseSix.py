"""
This script will :

Use the seaborn library to produce a heatmap PNG image  
Don’t use the direct way to create a heatmap sns.heatmap(df). 
Instead, create a figure and a subplot first, and then let 
the heatmap function know about the subplot you want to plot 
the data to by passing the axes as argument. Creating a 
figure and a subplot will enforce your knowledge on the 
general technique involved in plotting data. It will also 
let you have more control on the figure and the axes objects.

author:  GA Sauer
date:    April 23, 2016
updated:  May 16, 2016
"""
import os
import pandas
import seaborn as sbn
from seaborn import plt

dir = "/Users/GAMac/pythonPractice/ExerciseSix/"
inputFile = "US States Median Income Data.csv"
outputFile = "incomeHeatmap.png"



def createHeatMap(dir, inputFile, outputFile):
    #change working directory
    os.chdir(dir)
        
    #open up CSV file as dataframe and set the columns GEOID and State as indexes
    df = pandas.read_csv(inputFile)#, index_col = ['GEOID', 'State'])
    
    # set the columns GEOID and State as indexes
    df=df.set_index(['GEOID', 'State'])
    
    #create single plot by not passing in any subplot args
    fig, axes = sbn.plt.subplots()

    axes.tick_params(labelsize=8, direction='in')

    '''To relate the heatmap to the axes you created, pass the axes variable name to the ax parameter inside the heatmap method:'''
    sbn.heatmap(df, ax=axes)
    
    
    plt.yticks(rotation=0)

    plt.xticks(rotation=90)

    #Save figure object into a PNG file
    fig.savefig(outputFile, dpi = 200)

    '''Check to see if file already exists, if so delete it
       and then export updated dataframe to new CSV file'''
    if os.path.isfile(outputFile):
        os.remove(outputFile)
        fig.savefig(outputFile, dpi = 200)
    else:
       fig.savefig(outputFile, dpi = 200)
    


createHeatMap(dir, inputFile, outputFile)
