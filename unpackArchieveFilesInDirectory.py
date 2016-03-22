"""
This script will extract archive multiple files in a directory .
In this case a .gz file

author:  GA Sauer
date:    March 22, 2016
"""

import os
import glob
import patoolib

#Assign input and output directory variables
inDir = "/Users/GAMac/pythonPractice/gz_files"
outDir = "/Users/GAMac/pythonPractice/gz_unpack2"

#Create a function that will unpack multiple files
def extractFiles(inDir, outDir):
    os.chdir(inDir)
    
    #Create a list of gz files in directory
    archives = glob.glob("*.gz")
    
    #Check to see if outDir exists, if not create it
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    
    #Assign list of files in directory that have already been extracted
    files = os.listdir(outDir)
        
    #Unpack archiver files
    for archFiles in archives:
        #only if file doesn't already exist, extract it
        if archFiles[:-3] not in files:
            patoolib.extract_archive(archFiles, outdir=outDir)
        



extractFiles(inDir, outDir)
