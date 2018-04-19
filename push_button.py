# Program to test functionality of a push button
# Source: https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

import RPi.GPIO as GPIO

GPIO.setwarnings(False) #ignore warnings for now
GPIO.setmode(GPIO.BOARD) # use physical pin numbering
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set pin 10 to be an input pin and set initial value to be pulled low

print("Push Button Test function")
print(" ")
print("Press ctrl-c to exit")
print("_" *37)
while True: #run forever
	if GPIO.input(17) == GPIO.HIGH:
		print("Button was pushed!")

