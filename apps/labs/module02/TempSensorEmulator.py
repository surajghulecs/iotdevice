'''
Created on Jan 21, 2019
@author: suraj
'''
from threading import Thread
from time import sleep
from random import uniform
from labs.common import SensorData
from labs.module02 import SmtpClientConnector

sensorData = SensorData.SensorData()                        #Create an instance of SensorData class
smtpconnector = SmtpClientConnector.SmtpClientConnector()   #Create an instance of SmtpClientConnector

class TempSensorEmulator(Thread):
    
    '''
    Constructor for TempSensorEmulator
    '''
    def __init__(self):                                     # Overriding constructor __init__ here with parameters
        Thread.__init__(self)                               # Calling __init__(self) from parent class Thread
        self.threadID = 1                                   # initializing Thread ID
        self.enable_Adaptor = False                         # initializing enable_Adaptor
        self.name = "Thread"                                # initializing name of the Thread
        self.counter = 1                                    # initializing counter for thread i.e how many threads we want to create
        self.sleep_cycle = 10                               # Specifies suspend time for the next reading
        self.lowVal = 10                                    # Lower value of temperature from sensor simulator
        self.highVal = 30                                   # Higher value of temperature from sensor simulator
        self.isPrevTempSet = False                          # Checks for previous temperature value
        self.alertDiff = 5                                  # Threshold at which we want to trigger the alert
        self.rateInSec = 1                                  # Initializes suspend time for the next reading
    
    '''
    Overriding the run method in Thread sub-class to suit our purpose for simulating sensor reading and
    displaying the alert on console and email
    ''' 
    def run(self):
        while True:
            if self.enableEmulator: 
                self.curTemp = exit
                sensorData.addValue(self.curTemp)
                print('\n--------------------')
                print('New sensor readings:')
                print('  ' + str(self.curTemp))
                a = sensorData.__str__()
                print (a)
                if self.isPrevTempSet == False: 
                    self.prevTemp = self.curTemp 
                    self.isPrevTempSet = True
                else:
                    if (abs(self.curTemp - sensorData.getAvgValue()) >= self.alertDiff): 
                        print('\n  Current temp exceeds average by > ' + str(self.alertDiff) + '. Triggering alert...')    
                        smtpconnector.publishMessage('Exceptional sensor data [test]', sensorData)
                    sleep(self.rateInSec)
    
    '''
    Enables the Emulator before running the Thread
    '''                
    def enableEmulator(self):
        self.enable_Adaptor = True
