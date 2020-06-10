'''
Created on Jan 21, 2019
@author: suraj
'''

import labs.common.ConfigUtil as ConfigUtil
from    threading                               import Thread
from    time                                    import sleep
from    random                                  import uniform
from    labs.common                             import SensorData
from    labs.module02                           import SmtpClientConnector
from    labs.common                             import ConfigConst
from    labs.common.ActuatorData                import ActuatorData
from    labs.module03.TempActuatorEmulator      import TempActuatorEmulator

sensorData = SensorData.SensorData()                        #Create an instance of SensorData class
smtpconnector = SmtpClientConnector.SmtpClientConnector()   #Create an instance of SmtpClientConnector
actuatorData = ActuatorData()                               #Create an instance of ActuatorData
TempActuatorEmulator = TempActuatorEmulator()               #Create an instance of TempActuatorEmulator

class TempSensorAdaptor(Thread):
    
    '''
    Constructor
    '''
    def __init__(self):             # Overriding constructor __init__ here with parameters
        Thread.__init__(self)       # Calling __init__(self) from parent class Thread
        self.threadID = 1           # initializing Thread ID
        self.enable_Adaptor = False # initializing enable_Adaptor
        self.name = "Thread"        # initializing name of the Thread
        self.counter = 1            # initializing counter for thread i.e how many threads we want to create
        self.sleep_cycle = 10       # Specifies suspend time for the next reading
        self.lowVal = 10            # Lower value of temperature from sensor simulator
        self.highVal = 30           # Higher value of temperature from sensor simulator
        self.isPrevTempSet = False  # Checks for previous temperature value
        self.alertDiff = 5          # Threshold at which we want to trigger the alert
        self.rateInSec = 2          # Initializes suspend time for the next reading
        '''
        For the env rasp pi use the below path
        self.config = ConfigUtil.ConfigUtil('/home/pi/workspace/iot-device/config/data/ConnectedDevicesConfig.props')
        For local use the below path
        self.config = ConfigUtil.ConfigUtil('../../../config/data/ConnectedDevicesConfig.props')
        '''
        self.config = ConfigUtil.ConfigUtil('../../../config/data/ConnectedDevicesConfig.props')  
        self.config.loadConfig()    #Loading the configfile
    
    '''
    Overriding the run method in Thread sub-class to suit our purpose for simulating sensor reading and
    displaying the alert on console and email
    ''' 
    def run(self):
        nominalTemp = int(self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.NOMINAL_TEMP_KEY))
        #Takes the nominalTemp value from configfile
        while True:
            if self.enableEmulator: 
                self.curTemp = uniform(float(self.lowVal), float(self.highVal))
                #Takes the random value of low and high temperatures 
                sensorData.addValue(self.curTemp)
                print('\n--------------------')
                print('New sensor readings:')
                print('  ' + str(self.curTemp))
                a = sensorData.__str__()
                print (a)
                SensorData_Json = sensorData.fromSensortoJson(sensorData)           #Convert Sensor data in JSON format
                ActuatorData_Json = actuatorData.fromActuatortoJson(actuatorData)   #Convert Actuator data in JSON format
                
                #print (a)                                                          #Prints the current sensor data
                if self.isPrevTempSet == False:                                     
                    self.prevTemp = self.curTemp                                    #Replace previous temperature with current         
                    self.isPrevTempSet = True                       
                else:
                    if (abs(self.curTemp - sensorData.getAvgValue()) >= self.alertDiff):
                        #Setting the alert condition 
                        print('\n  Current temp exceeds average by > ' + str(self.alertDiff) + '. Triggering alert...')
                        print (SensorData_Json)                                     #Prints the Sesnsor Data in JSON format 
                        smtpconnector.publishMessage('Exceptional sensor data [test]', SensorData_Json)
                        print('\n')
                        print ("Actuator Data", ActuatorData_Json)
                        with open('SensorData.json', 'w') as f:                     
                            f.write(SensorData_Json)                                #Writes the Sensor data in JSON format to a file
                        #Sending the email
                    if (abs(self.curTemp - nominalTemp) > 0):                       #Checks the difference in temperature
                        val = self.curTemp - nominalTemp
                        actuatorData.setValue(val)                                  #Updates actuatorData with difference in temperature
                        if (val > 0):
                            actuatorData.setCommand(1)                              #Command set for temperature raise
                        else:
                            actuatorData.setCommand(0)                              #Command set for temperature low
                        #TempActuatorEmulator.processMessage(actuatorData)
                        
                        TempActuatorEmulator.processMessage(actuatorData)           #LED Display message with new Actuator Data
                    sleep(self.rateInSec)                                           #Rest time for CPU
    
    '''
    Enables the Emulator before running the Thread
    '''                
    def enableEmulator(self):
        self.enable_Adaptor = True
