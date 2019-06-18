#Author: Coire Gavin-Hanner
#Created 6-14-2019

import time
import Adafruit_ADS1x15
import os
import csv
import datetime
import numpy
from gpiozero import Button
from time import sleep

#Setup ADC
adc = Adafruit_ADS1x15.ADS1015()
GAIN = 2/3

#change directory so that all CSV files go into a specific folder
destFolder = "/home/pi/SCMP401/CSV"
os.chdir(destFolder)

#Ask for filename
filename = raw_input("Enter name : ")

rate_01 = []
rate_02 = []
rate_05 = []
rate_1 = []
rate_2 = []
rate_5 = []
stdDev = [0,0,0,0,0,0]

e = 0

while e < 200:
    values = [0]*4
    for i in range(4):
	values[i] = adc.read_adc(i, gain=GAIN) #take in the values from each of the four ADC channels
   	time.sleep(0.01)
    rate_01.append(values[0])
    e += 1 
    
e = 0
stdDev[0] = numpy.std(rate_01)
print(stdDev[0])
 
while e < 200:
    values = [0]*4
    for i in range(4):
	values[i] = adc.read_adc(i, gain=GAIN) #take in the values from each of the four ADC channels
    time.sleep(0.02)
    rate_02.append(values[0])
    e += 1

e = 0
stdDev[1] = numpy.std(rate_02)
print(stdDev[1])

while e < 200:
    values = [0]*4
    for i in range(4):
	values[i] = adc.read_adc(i, gain=GAIN) #take in the values from each of the four ADC channels
    time.sleep(0.05)
    rate_05.append(values[0])
    e += 1

e = 0
stdDev[2] = numpy.std(rate_05)
print(stdDev[2])

while e < 200:
    values = [0]*4
    for i in range(4):
	values[i] = adc.read_adc(i, gain=GAIN) #take in the values from each of the four ADC channels
    time.sleep(0.1)
    rate_1.append(values[0])
    e += 1

e = 0
stdDev[3] = numpy.std(rate_1)
print(stdDev[3])

while e < 200:
    values = [0]*4
    for i in range(4):
	values[i] = adc.read_adc(i, gain=GAIN) #take in the values from each of the four ADC channels
    time.sleep(0.2)
    rate_2.append(values[0])
    e += 1

e = 0
stdDev[4] = numpy.std(rate_2)
print(stdDev[4])

while e < 200:
    values = [0]*4
    for i in range(4):
	values[i] = adc.read_adc(i, gain=GAIN) #take in the values from each of the four ADC channels
    time.sleep(0.5)
    rate_5.append(values[0])
    e += 1

e = 0
stdDev[5] = numpy.std(rate_5)
print(stdDev[5])