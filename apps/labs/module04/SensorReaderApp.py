'''
Created on Jan 21, 2019
@author: Suraj
'''

'''
For env rasp pi use
import sys,os
sys.path.insert(0, '/home/pi/workspace/iot-device/apps')
'''
from labs.module04  import I2CSenseHatAdaptor
from time           import sleep

SensorReaderApp = I2CSenseHatAdaptor.I2CSenseHatAdaptor()       # Creating an instance of I2CSenseHatAdaptor class
SensorReaderApp.daemon = True                                   # Specifying instance to use thread as daemon process
print ("Sensor Data from SenseHAT")
SensorReaderApp.enableEmulator()                                # Changing the enableEmulator from False to True
wait = 5                                                        # Wait time of 5 seconds for CPU to give it a break
SensorReaderApp.start()                                         # The thread to collect system performance will be started here
while (True):                                                   # infinite loop
    sleep(wait)                                                 # method for giving CPU a break of 5 seconds called
    pass                                                        # executes the current loop and pass execution to next iteration
    

