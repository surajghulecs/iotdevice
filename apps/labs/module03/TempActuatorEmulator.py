'''
Created on Feb 1, 2019
@author: Suraj
'''

'''
For env rasp pi use
import sys
sys.path.append('/home/pi/Desktop/howson/iot-device/apps')
'''
from labs.common.ActuatorData import ActuatorData
from labs.module03.SenseHatLedActivator import SenseHatLedActivator
from labs.module03.SimpleLedActivator import SimpleLedActivator

actuatorData = ActuatorData()                                                           #Create an instance of actuatorData
senseHatLedActivator = SenseHatLedActivator()                                           #Create an instance of senseHatLedActivator
simpleLedActivator = SimpleLedActivator()                                               #Create an instance of SimpleLedActivator

class TempActuatorEmulator():
    
    '''
    Constructor
    '''
    def __init__(self):
        senseHatLedActivator.setEnableLedFlag(True)                                     #Enables the LED display flag
        
    '''
    Function that handles display on SenseHat LED
    @param actuatorData - String value. absolute difference in nominal and current temperature
    '''         
    def processMessage(self, actuatorData):
        simpleLedActivator.setEnableLedFlag(True)                                       #Not used since SenseHat is used
        actuatorData.updateData(actuatorData)                                           #Updates the actuator when new data comes
        if actuatorData.getCommand() == 0:                                              #Command 0 for message of lowering temperature
            message = "Temperature need to raise " + str(abs(actuatorData.getValue()))  
        if actuatorData.getCommand() == 1:                                              #Command 1 for message of lowering temperature
            message = "Temperature need to lower " + str(actuatorData.getValue())
        senseHatLedActivator.setDisplayMessage(message)                                 #Display message of regulating temperature
        senseHatLedActivator.run()                                                      #Thread for senseHatLedActivator started
            
