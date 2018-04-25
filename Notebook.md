# SCMP Capstone Project Notebook :bowtie:
#### Coire Gavin-Hanner
#### Advisor: Jim Skon

## Overall Goals: 
1. Digitize the output of the GC instrument in the Chemistry Department :pencil: --> :tv:
2. Standardize and analyze the digital output of the instrument
3. Design a user-interface for instrument users to utilize the data

## Research Specs of GC
#### Goal: 
Learn the specifications of the instrument so I can determine what hardware I will need.
#### Process:
Talk with Dudley to get information
#### Results:
After talking with Dudley, I know that the GC instrument's current ourput gives a difference of voltages. 

#### Conclusions:
The system that I design will need to be able to input a difference of voltage.

## Basic Design of A-->D System
#### Goal:
Design the hardware system that will be used to convert the analog output of the GC instrument to digital information.

#### Process:
This will involve meeting with Skon. This will also probably require deciding on the way users will utilize the information.

#### System:
1. Arduino to input the voltage difference
2. Raspberry Pi to interact with the user and send the information to the server
3. Server to analyze the data
4. Website that allows the user to access the data
#### Required Materials:
1. Arduino
2. Raspberry PI

## Reflection: 15 Minute Proposal Presentation
During my presentation I discussed the GC instrument, the problems with it, and my basic design for a solution. Professor Garcia identified an unsupported claim in my proposal; I claimed that the current method for integrating peaks was inaccurate. While this may be true, I have no support for it. I need to revisit my proposal and update it. 
Sam, who has experience with arduinos, mentioned that there is a host of attachments for the arduinos that accomlish various things. He suggested looking for peices that accomplish the task of analog-to-digital conversion.

## Initializing Raspberry Pi :strawberry:
#### Goals:
1. Set up Raspian OS 
2. Become familiar with the environment of Raspian
#### Process: 
1. Download NOOBS files onto SD card
2. insert SD Card into Raspberry Pi
3. Connect Display, Keyboard, and Mouse
4. Connect to power supply
5. Select Raspian OS and download

#### Conclusions:
My Raspberry Pi is initialized!

## Connect to Raspberry Pi from mac :apple:
1. In Raspberry Pi go to setup
2. enable SSH
3. type "hostname -I" in Pi terminal to get ip address
4. In mac, type ssh pi@<IP> where "<IP> is replaced with the IP address
5. type yes when mac questions authenticity of Pi
6. enter password (if one is set up on Pi) and you will be connected
  
## Testing the output of the GC Instrument
#### Goals: 
Measure the voltage output of the GC instrument and plan a hardware solution to connect the GC to my Raspberry Pi

#### Process: 
1. Run the GC instrument and separate two substances in a solution (solution and instrument handling provided by Dudley Thomas)
2. Connect a volt meter to the output wires of the GC (meter and expertise provided by Paula Turner of the Physics department)

#### Results: 
The baseline for the instrument is -0.05 V right now. The baseline can be changed, but only by about ±0.015 V. The peaks for the two substances in the mixture occurred at -0.001V and +0.009V so the maximum measured change in volts was 0.0059V.

#### Conclusions:
Due to the magnitude of the output (in volts) professor Turner suggested using an amplifier before connecting the output wires to a ADC (analog-to-digital) converter and connecting to the Raspberry Pi. The amplifier worked by simply increasing the magnitude of the signal. 

#### Future Steps:
Construct a circuit using an amplifier and an ADC that can be used to connect the GC to my Raspberry Pi (RP).

## Constructing a circuit on a Breadboard

#### Goals: 
Create an initial circuit to connect the GC to the RP. This will be done on a breadboard initially for testing.

#### Process:
1. Connect an OpAmp (amplifier) to an ADC and a potenitometer. 
this was done by porfessor Turner based on an online schematic that she found. 

#### Resutls:

#### Future steps:
write a program that will allow me to input information from the ADC on the RP


## Starting to Program on the Raspberry Pi
#### Goals: 
set up my device so that I can start coding as soon as the circuit is connected

#### Process:
follow the documentation for ADC:
 1.  install Python 3, PIP for Python 3, and the RPi.GPIO library (used to talk to GPIO pins on the Pi) with these commands:
  sudo apt-get update (updates lists of packages)
  sudo apt-get install -y python3 python3-pip python-dev
  sudo pip3 install rpi.gpio
 2. [Python code to use the ADS1015 and ADS1115 analog to digital converters with a Raspberry Pi or BeagleBone black.](https://github.com/adafruit/Adafruit_Python_ADS1X15)
 3. Start by Running a simple python program [Link to intro video](https://www.youtube.com/watch?v=jD4jRgIciHs)
   ```
   pi@raspberrypi:~ $ nano helloPi.py
   ```
   ``` Python
   print "Hello Pi"
   ```
   ```
   pi@raspberrypi:~ $ python helloPi.py
   ```
  4. Save a simple test file [code] (https://github.com/adafruit/Adafruit_Python_ADS1x15/blob/master/examples/simpletest.py)
  
 ## Connecting Circuit to Raspberry Pi
I tried to run the simple test program and kept getting the following error message:

```
Traceback (most recent call last):
  File "simpletest.py", line 12, in <module>
    adc = Adafruit_ADS1x15.ADS1115()
  File "build/bdist.linux-armv7l/egg/Adafruit_ADS1x15/ADS1x15.py", line 319, in __init__
  File "build/bdist.linux-armv7l/egg/Adafruit_ADS1x15/ADS1x15.py", line 82, in __init__
  File "build/bdist.linux-armv7l/egg/Adafruit_GPIO/I2C.py", line 66, in get_i2c_device
  File "build/bdist.linux-armv7l/egg/Adafruit_GPIO/I2C.py", line 99, in __init__
  File "build/bdist.linux-armv7l/egg/Adafruit_PureIO/smbus.py", line 97, in __init__
  File "build/bdist.linux-armv7l/egg/Adafruit_PureIO/smbus.py", line 122, in open
IOError: [Errno 2] No such file or directory: '/dev/i2c-1'
```
To solve the problem, I used the steps on this [website](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) to configure I2C. I needed to use the command ```sudo raspi-config``` and then select Interfacing options > I2C> enable I2C

I Checked where I should be putting the pins and used this [website](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

use the command
```
sudo raspi-config
```
It worked! Now I am getting a different error message:
```
Reading ADS1x15 values, press Ctrl-C to quit...
|      0 |      1 |      2 |      3 |
-------------------------------------
Traceback (most recent call last):
  File "simpletest.py", line 42, in <module>
    values[i] = adc.read_adc(i, gain=GAIN)
  File "build/bdist.linux-armv7l/egg/Adafruit_ADS1x15/ADS1x15.py", line 192, in read_adc
  File "build/bdist.linux-armv7l/egg/Adafruit_ADS1x15/ADS1x15.py", line 128, in _read
  File "build/bdist.linux-armv7l/egg/Adafruit_GPIO/I2C.py", line 129, in writeList
  File "build/bdist.linux-armv7l/egg/Adafruit_PureIO/smbus.py", line 274, in write_i2c_block_data
IOError: [Errno 121] Remote I/O error
```

Use  ```i2cdetect -y 1 ``` to probe all addresses on a bus.
This reported that nothing was connected to the Pi

## Learn to Use GPIO
#### Goal:
##### Because I was having great difficulty connecting the ADC circuit to my Raspberry PI, my new goal is to simply learn to use the GPIO pins on my PI.

I started by installing RPi.GPIO. This [website](https://pypi.python.org/pypi/RPi.GPIO) has a download folder. I put into a folder called gpio in /home. 

I then started to experiment with LEDs and Buttons. I learned that to connect an LED to the Pi, you have to build the following circuit: 
3.3V power source ---> resistor ----> LED ------> GPIO pin. You can then write a python program to use the LED. A [button](https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/) is similar:
3.3V power source ---> resistor ----> button------> GPIO pin.

This [Raspberry Pi documentation page](https://www.raspberrypi.org/documentation/usage/gpio/python/README.md) gives simple functions for using LEDs and Buttons.

I was able to write code so that an LED blinked when I pressed a button and stopped blinking when I pressed it again.

#### Conclusion:
I can find nothing wrong with the GPIO pins. I have been using code from online tutorials and the GPIO pins have been behaving exactly as the tutorials said they would. I beleive that there is something else wrong in the system. 
I think that this was a very useful exercise though. The LEDs and Buttons were very easy to use and simple to set up. I will be using buttons and LEDs in my (initial) user interface. I think it will be very simple to control inputs using the button hardwired to the ADC circuit. 

## Reflection: Presentation #1
#### Disclaimer: as you already know, this reflection is a couple weeks late. I completely forgot that I had to write this after giving my first presentation

In this presentation, I described the background of my project, what I had done so far, and my future plans for the project. When giving the presentation, I was still working with Professor Turner to construct the ADC circuit. My goals for future work included receiving and analyzing data from the ADC, building a UI, and sending the information to the user. I had the class help me figure out how I should accomplish my last goal of sending the information to the user. We decided that email would be the best format. I plan to incorporate that in my project. 

## Reflection: Presentation #2

In this presentation I gave brief overview of my project, explained what I had done since the last presentation, and talked again about my goals for the project. To summarize what I had done, I attempted to connect the ADC circuit to my Raspberry Pi and recieve information. I was unable to accomplish this. I spent a lot of time searching for solutions to the problem that I was having. Most of the "solutions" that I found led me down rabbit holes that did nothing but waste time. I did manage to find a few useful websites and found things like the i2cdetect command that checks to see if anything is connected to the pi with i2c connection protocol. I used the command and determined that nothing was connected. My immediate goal is to remedy that. One of my classmates (i do not remember which one) asked me if there was any way I could tell if the the ADC was giving an output. That is one place to start. I will also try to replace batteries in the power source, connecting wires, etc. One other possibility is that the GPIO pins are not working correctly for some reason. To check that I will try to complete a simple project using the GPIO pins to respond to a signal and light an LED. Because of the stagnant state of my project, I did not have much to present on, but I was given lots of great feedback by my peers and Professor Garcia. 
  

## Redesigning the Circuit

Because I was not able to receive input to the Pi correctly, I brought the ADC circuit back to Professor Turner to see if she had any insights into what could be causing the problem. She noticed that there were multiple grounds in the circuit and beleived that that was most likely this issue. She redesigned the circuit using the power supply from the Pi instead of a battery pack. The circuit now has only one ground and works perfectly! I was able to run the simple test program that I found in the documentation for the ADC and read values between 0 and ~600 that changed when I used the variable resistor. This means that I can now start to program!

## Writing data to a csv file. 
#### Goal:
Be able to store data from the ADC in a permanent file. I chose a CSV file because it can be opened and manipulated using many common programs such as Excel

#### Procedure:
I started with the simple test program for the ADC and modified it to write to a CSV file. I learned about functions that will read and write data to a CSV file from this [website](http://stackabuse.com/reading-and-writing-csv-files-in-python/). I was able to accomplish this. My code is below:
```
import time
import Adafruit_ADS1x15
import os
import csv
import datetime

adc = Adafruit_ADS1x15.ADS1015()
GAIN = 16
destFolder = "/home/pi/SCMP401/CSV"
os.chdir(destFolder)

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
data = []
loopNum = 0
# Main loop.
while loopNum < 20:
    values = [0]*4
    for i in range(4):
	values[i] = adc.read_adc(i, gain=GAIN)
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    time.sleep(0.5)
    data.append(values[1]-values[0])
    loopNum += 1

csvName = str(datetime.datetime.now())
myFile = open(csvName, 'w')
with myFile:
	writer = csv.writer(myFile)
	writer.writerow(data)
```
#### Conclusion:
I now have code that lets me store data easily in a CSV file.

#### Future Steps:
1. add button funcitonality that allows me to control when the program reads data from the ADC. It should write data to the CSV after it stops reading
2. Add in code that creates a new csv file everytime the program runs. It should put these files in a separate folder. My guess is that the best way to do this is to name the files after the time that the program is run.


## Creating a unique CSV file name
#### Goal:
Write data to a csv file named after the date and time that the program is run. 

#### Code:
```
import datetime
import csv
import os

#Path to the directory where the CSV file will be written
destFolder = "/home/pi/SCMP401/CSV"

os.chdir(destFolder)
data = [1,2,3,4,5]
csvName = str(datetime.datetime.now())
myFile = open(csvName, 'w')
with myFile:
	writer = csv.writer(myFile)
	writer.writerow(data)
```
## Using a button to control the ADC
#### Goal:
make it easy for a user to control when the ADC is being used. One press of the button should make the Pi start recording data from the Pi. Another button press will make the Pi stop recording data and write existing data to a CSV file

#### code:
```
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
```
Note: The buttons that I am using seem to give odd boolean values. When they are pressed button.is_pressed returns false and vise versa

## Sending an email from a python Program
#### Goal:
be able to send a csv file to a specfied email account form a python program

#### Setting up ssmtp and email account
I found directions on this [website](http://www.raspberry-projects.com/pi/software_utilities/email/ssmtp-to-send-emails)

#### set up email account
normal gmail set up
go to this [link](https://www.google.com/settings/security/lesssecureapps) and allow less secure apps

## Reflection
This week's presentation was much more successful than last presentation. I was able to show some successes! My classmates did not have many questions or comments for me. Professor Garcia had a great insight during the presentation though. He suggested that instead of emailing the data to the user, set up a githib account and automatically push the data to the repository. This would allow the users to access the informaiton in one spot and it would make it much easier to program for me.


