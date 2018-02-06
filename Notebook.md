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







