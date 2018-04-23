#Author: Coire Gavin-Hanner
#Created 4-19-2018

import time
import Adafruit_ADS1x15
import os
import csv
import datetime
from gpiozero import Button
from time import sleep

btn = Button(23)

adc = Adafruit_ADS1x15.ADS1015()
GAIN = 16
destFolder = "/home/pi/SCMP401/CSV"
os.chdir(destFolder)

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
data = []
btnState = 0


while btnState < 1:
	if not btn.is_pressed: #For the buttons that I am using, this boolean expression is opposite what you would expect
		btnState += 1
	time.sleep(0.2)

# Main loop.
while btnState > 0 and btnState < 2:
    values = [0]*4
    for i in range(4):
	values[i] = adc.read_adc(i, gain=GAIN)
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    time.sleep(0.2)
    data.append(values[1]-values[0])
    if not btn.is_pressed:
    	btnState += 1


csvName = str(datetime.datetime.now())
myFile = open(csvName, 'w')
with myFile:
	writer = csv.writer(myFile)
	writer.writerow(data)