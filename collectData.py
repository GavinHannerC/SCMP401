#Author: Coire Gavin-Hanner
#Created 4-19-2018

import time
import Adafruit_ADS1x15
import os
import csv
import datetime
from gpiozero import Button
from time import sleep

btn = Button(23) #23 is the GPIO pin that the button is connected to

#Setup ADC
adc = Adafruit_ADS1x15.ADS1015()
GAIN = 2/3

#change directory so that all CSV files go into a specific folder
destFolder = "/home/pi/SCMP401/CSV"
os.chdir(destFolder)

# Print nice channel column headers.
print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
data = []

#setup button state
btnState = 0

#Wait for button to be pressed
while btnState < 1:
	if not btn.is_pressed: #For the buttons that I am using, this boolean expression is opposite of what you would expect
		btnState += 1
	time.sleep(0.05)

# Main loop. Entered after button is pressed once
while btnState > 0 and btnState < 2:
    values = [0]*4
    for i in range(4):
	values[i] = adc.read_adc(i, gain=GAIN) #take in the values from each of the four ADC channels
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    time.sleep(0.1)
    data.append(values[1]-values[0]) #the difference between these two values gives the data that we need
    if not btn.is_pressed: #if the button is pressed again, exit the loop
    	btnState += 1

#Write data to a CSV file
csvName = str(datetime.datetime.now()) #names the file after the date and time the program was run
myFile = open(csvName, 'w')
with myFile:
	for row in data:
		writer = csv.writer(myFile)
		writer.writerow([row])
	
