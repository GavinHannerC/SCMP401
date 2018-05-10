
import RPi.GPIO as GPIO ## Import library that lets you control the Pi's GPIO pins
from time import sleep ## Import time for delays


GPIO.setwarnings(False) ## Disables messages about GPIO pins already being in use
GPIO.setmode(GPIO.BOARD) ## Indicates which pin numbering configuration to use
 
pinNumGreenLED = 7 # these are the physical pin locations for GPIO 4 and 23
pinNumYellowLED = 
pinNumBTN = 16
GPIO.setup(pinNumLED,GPIO.OUT) ## Tells it that pinNumLED will be outputting
GPIO.setup(pinNumBTN,GPIO.IN) ## Tells it that pinNumBTN will be giving input
 
## Initialize btnOn and prev_input
btnOn = False
prev_input = 1


while True:
    try:
        input = GPIO.input(pinNumBTN) #input is 1 if the button is currently pressed, 0 otherwise
 		
        if ((not prev_input) and input): # if (prev_input = false and if input = true)
            btnOn = not btnOn 			 # btnOn is now set to the opposite of what is was before (it is now true)
        prev_input=input				 # sets prev_input to whatever the button input was
       	sleep(0.05)
 
        ## When the button is pressed, start toggling the LED between 
        ## HIGH and LOW with a 0.5s interval between
        if btnOn: #if btnOn is true
            GPIO.output(pinNumLED,GPIO.HIGH) # turn the LED off
            sleep(0.5)
            GPIO.output(pinNumLED,GPIO.LOW) #turn the LED on
            sleep(0.5)
        else:
            GPIO.output(pinNumLED,GPIO.HIGH) #turn the LED off
    except KeyboardInterrupt:
        break
