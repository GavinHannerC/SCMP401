# Created 4-15-18
# Author: Coire Gavin-Hanner

# The purpose of this program is to control the ADC with a button. I will combine the code of two programs ( button.py and simpletest.py).
# If the program works correctly, the ADC will work when the button is pressed. I will know this is working because the LED will blink when
# the button is in its on state and the ADC values should print to the screen


#Set up ADC

#Import libraries for ADC
import time
import Adafruit_ADS1x15
# create an ADS1015 ADC (12-bit) instance.
adc = Adafruit_ADS1x15.ADS1015()
# set gain for ADC. See simpletest.py for more information about GAIN
GAIN=16

# set up button and LEDunctionality

import RPi.GPIO as GPIO ## Import library that lets you control the Pi's GPIO pins
from time import sleep ## Import time for delays
GPIO.setwarnings(False) ## Disables messages about GPIO pins already being in use
GPIO.setmode(GPIO.BOARD) ## Indicates which pin numbering configuration to use
pinNumGreenLED = 7
pinNumBTN = 16
GPIO.setup(pinNumGreenLED,GPIO.OUT) ## Tells it that pinNumLED will be outputting
GPIO.setup(pinNumBTN,GPIO.IN) ## Tells it that pinNumBTN will be giving input
## Initialize btnOn and prev_input
btnOn = False
prev_input = 1

#CSV
import csv

#Combine them
print('Reading ADS1x15 values, press GPIO button to read, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
loops = 0
data = []

testData = [1,2,3,4,5]
while True and loops < 5:
    try:
        input = GPIO.input(pinNumBTN)
 
        if ((not prev_input) and input):
            btnOn = not btnOn
        prev_input=input
       	sleep(0.05)
 
        ## When the button is pressed, start toggling the LED between 
        ## HIGH and LOW with a 0.5s interval between
        if btnOn:
            GPIO.output(pinNumGreenLED,GPIO.HIGH)
            #print(adc.read_adc(1, gain=GAIN)) # prints the value for the ADC to the screen
            tempData = adc.read_adc(1, gain=GAIN)
            print(tempData)
            data.append(tempData)
            loops += 1
            sleep(0.5)
            GPIO.output(pinNumGreenLED,GPIO.LOW)
            sleep(0.5)
            
        else:
            GPIO.output(pinNumGreenLED,GPIO.HIGH)
    except KeyboardInterrupt:
        break
        
GPIO.output(pinNumGreenLED,GPIO.HIGH) # turns off the LED at the end of the program
myFile = open('csvtest1.csv', 'w')
with myFile:
	writer = csv.writer(myFile)
	writer.writerow(data)



