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
    

