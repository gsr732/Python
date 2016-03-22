"""
This script will extract archive files 
In this case a .gz file

author:  GA Sauer
date:    March 22, 2016
"""

import os, patoolib

#Set working directory
os.chdir("/Users/GAMac/pythonPractice/gz_files")

#Unpack archiver files
patoolib.extract_archive("amie2.20160321.gz", outdir="/Users/GAMac/pythonPractice/gz_unpack")



