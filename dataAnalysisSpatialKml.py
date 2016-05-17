"""
This script will :

Create kml file with UES and Albany mapped

author:  GA Sauer
date:     May 16-17, 2016
"""
import os
import simplekml
from simplekml import Kml

#create empty kml object
kml = simplekml.Kml()

#create on point with new point and pass name
kml.newpoint(name="Upper East Side of Manhattan", coords = [(-73.9566, 40.7736)])


#create another new oint
kml.newpoint(name="Albany, NY", coords = [(-73.7562, 42.6526)])


'''Check to see if file already exists, if so delete it 
    and then save kml object to kml file'''
if os.path.isfile("UESandAlbany.kml"):
    os.remove("UESandAlbany.kml")
    kml.save("UESandAlbany.kml")
else:
    kml.save("UESandAlbany.kml") 
    
