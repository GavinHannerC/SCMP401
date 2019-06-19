#Author: Coire Gavin-Hanner
#Created 4-19-2018

import time
import Adafruit_ADS1x15
import os
import csv
import datetime
import numpy as np
from gpiozero import Button
from time import sleep
from scipy import signal
import statsmodels.api as sm
import matplotlib.pyplot as plt
#from scipy.signal import find_peaks

btn = Button(23) #23 is the GPIO pin that the button is connected to
BASELINE = 0 #Change this if the baseline changes (this is a rough estimate near the baseline)

##### Setup ADC
adc = Adafruit_ADS1x15.ADS1015()
GAIN = 2/3

##### change directory so that all CSV files go into a specific folder
destFolder = "/home/pi/SCMP401/CSV"
os.chdir(destFolder)

##### Ask for filename
filename = input("Enter name (time and date stamp will be added automatically): ")

#####  Setup data arrays
data = []
xs = []
x = 1

#####  Print nice channel column headers.
print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)


##### Wait for button to be pressed
btnState = 0
while btnState < 1:
        if not btn.is_pressed: # if user presses button:
                btnState += 1
        time.sleep(0.1) #this has to be on a human time scale, otherwise you will change button state multiple times by physically pressing it once

##### Main data collection loop. Entered after button is pressed once, exited when button is pressed again
while btnState > 0 and btnState < 2:
        values = [0]*4
        for i in range(4):
                values[i] = adc.read_adc(i, gain=GAIN)
        print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
        time.sleep(0.001)
        data.append(values[0] + values[1] + values[2] + values[3] - BASELINE) # Adds the input from all four channels and subtracts the baseline estimate
        xs.append(x)
        x += 1
        if not btn.is_pressed: #if the button is pressed again, exit the loop
                btnState += 1        

##### LOWESS smoothing function
newData = []
newData = sm.nonparametric.lowess(data, xs, frac=0.01, is_sorted=False, )
smData = newData[:,1] #LOWESS outputs a 2-D array with x and y values, we want a 1-D list with only y-values

##### Write data to a CSV file
csvName = filename + " " + str(datetime.datetime.now()) + ".csv" #names the file after the date and time the program was run
myFile = open(csvName, 'w')
with myFile:
        for row in smData:
                writer = csv.writer(myFile)
                writer.writerow([row])
        
#### Plot smoothed data
#peaks, _ = find_peaks(smData, width=50)
plt.plot(smData)
#plt.plot(peaks, smData[peaks], "x")
plt.savefig(filename + " " + str(datetime.datetime.now()) + ".png", edgecolor='#7851a9', format='png')
plt.show()


