# created 4-16-18

from gpiozero import LED, Button
from time import sleep

gLed = LED(4)
#yLed = LED(18)
#rLed = LED(21)
button = Button(23)

#while True:
#	led.on()
#	sleep(1)
#	led.off()
#	sleep(1)

'''while True:
	if button.is_pressed:
		gLed.on()
	else:
		gLed.off()'''

btnState = 0

'''while True and btnState < 4:
	if button.is_pressed:
		btnState += btnState
		print(btnState)
	if btnState == 1:
		gLed.on()
	if btnState == 2:
		gLed.off()
		yLed.on()
	if btnState == 3:
		yLed.off()
		rLed.on()
		
rLed.off()'''
			
while btnState < 2:
	if button.is_pressed:
		print("Button Pressed")
		btnState += 1
	else:
		btnState = btnState
		
	if btnState == 1:
		gLed.on()
	else: 
		gLed.off()
		
		
		