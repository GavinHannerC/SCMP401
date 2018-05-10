# Author: Coire Gavin-Hanner
# Created 4-19-2018
# This program will create a CSV file in the specified folder. The name of the CSV will be the date and time that the program is run


import datetime # get the date and time
import csv #work with csv
import os #Change the working directory

#Path to the directory where the CSV file will be written
destFolder = "/home/pi/SCMP401/CSV"

os.chdir(destFolder)
data = [1,2,3,4,5]
csvName = str(datetime.datetime.now())
myFile = open(csvName, 'w')
with myFile:
	writer = csv.writer(myFile)
	writer.writerow(data)
	