"""
This script will download connect to a ftp site
and download all files in a certain directory

author:  GA Sauer
date:    March 22, 2016
"""

import os
import glob 
from ftplib import FTP

host = "ftp.ngdc.noaa.gov"  #
user = ""
passwd = ""
siteDir = "pub/outgoing/spidr/dbs/daily/"  # Directory of site
fileMatch = '*.gz'




def ftpDownLoader(host, user, passwd, siteDir, fileMatch):
    #Create an ftp object to a particular FTP site
    ftpSite = FTP(host)
    
    #Login to FTP site
    ftpSite.login(user, passwd)
    
    #Prepare local environment by creating new directory if 
    #it does not already exists
    if not os.path.exists("/Users/GAMac/pythonPractice/%s" % siteDir):
        os.makedirs("/Users/GAMac/pythonPractice/%s" % siteDir)
    os.chdir("/Users/GAMac/pythonPractice/%s" %siteDir)
    
    # Change to the proper directory
    ftpSite.cwd(siteDir)
    
  # Loop through matching files and download each one individually
    for fileName in ftpSite.nlst(fileMatch):
        try:
            fhandle = open(fileName, 'wb')
            print('Getting ' + fileName)
            ftpSite.retrbinary('RETR ' + fileName, fhandle.write)
        except ftplib.all_errors:
            print(fileName + ' is not available')
        fhandle.close()
    

ftpDownLoader(host, user, passwd, siteDir, fileMatch)

