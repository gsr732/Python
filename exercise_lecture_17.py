#Description:  Write items in a list to a file
#Author:  GA Sauer
#Date:  3/20/16

idsList=["B3","\nB4","\nB5","\nB6"]


dirPath = '/Users/GAMac/pythonPractice/'
fileName = "practice_17.txt"

with open(dirPath + fileName, 'w') as file:
    for item in idsList:
        file.write("%s" % item)