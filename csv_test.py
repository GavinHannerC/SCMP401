# created 4-15-18
# Author: Coire Gavin-Hanner

import csv

with open('csvexample.csv') as myFile:  
    reader = csv.reader(myFile)
    for row in reader:
        print(row)
        
myData = [[1, 2, 3], ['Good Morning', 'Good Evening', 'Good Afternoon']]  
myFile = open('csvexample3.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile)
   writer.writerows(myData)
