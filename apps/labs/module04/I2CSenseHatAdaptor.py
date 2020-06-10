'''
Created on Feb 7, 2019
@author: Suraj
'''

import smbus
import threading
from                time            import sleep
from                labs.common     import ConfigUtil
from                labs.common     import ConfigConst

i2cBus              = smbus.SMBus(1)                    # Use I2C bus No.1 on Raspberry Pi3 +
enableControl       = 0x2D                              # Register address where bytes are written
enableMeasure       = 0x08                              # Measured sensor data
accelAddr           = 0x1C                              # address for IMU (accelerometer)
magAddr             = 0x6A                              # address for IMU (magnetometer)
pressAddr           = 0x5C                              # address for pressure sensor
humidAddr           = 0x5F                              # address for humidity sensor
begAddr             = 0x28                              # Beginning address for writing the readings
totBytes            = 6                                 # Total bytes to be written
DEFAULT_RATE_IN_SEC = 5                                 # Break time between each reading

class I2CSenseHatAdaptor(threading.Thread):
    
        rateInSec       = DEFAULT_RATE_IN_SEC           # CPU rest time before taking next reading          
        accelData       = None                          # Initialized accelData
        magData         = None                          # Initialized magData
        pressData       = None                          # Initialized pressData
        humidData       = None                          # Initialized humidData
        enableEmulator  = False                         # Initialized enableEmulator
        
        '''
        Constructor
        '''
        def __init__(self):
            super(I2CSenseHatAdaptor, self).__init__()                                  # Calling the parent class constructor
            self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)   # Taking configuration from file
            self.config.loadConfig()                                                    # Loading configuration    
            print('Configuration data...\n' + str(self.config)) 
            self.initI2CBus()                                                           # Calling the initI2CBus function
        
        '''
        Function for writing SenseHat sensor reading data to console 
        '''     
        def initI2CBus(self):
            print("Initializing I2C bus and enabling I2C addresses...")                  
            i2cBus.write_byte_data(accelAddr, enableControl, enableMeasure)             # Block Write transaction for accelerometer
            i2cBus.write_byte_data(magAddr, enableControl, enableMeasure)               # Block Write transaction for magnetometer
            i2cBus.write_byte_data(pressAddr, enableControl, enableMeasure)             # Block Write transaction for pressure
            i2cBus.write_byte_data(humidAddr, enableControl, enableMeasure)             # Block Write transaction for humiduty
        
        '''
        Function for displaying accelerometer data from SenseHat LED to console.
        '''     
        def displayAccelerometerData(self):
            self.accelData = i2cBus.read_i2c_block_data(accelAddr, begAddr, totBytes)   # Block Read transaction for accelerometer
            print("SenseHat Accelerometer reading \t",self.accelData)
        
        '''
        Function for displaying magnetometer data from SenseHat LED to console.
        '''     
        def displayMagnetometerData(self):
            self.magData = i2cBus.read_i2c_block_data(magAddr, begAddr, totBytes)       # Block Read transaction for magnetometer
            print("SenseHat Magnetometer reading \t", self.magData)
        
        '''
        Function for displaying pressure data from SenseHat LED to console.
        ''' 
        def displayPressureData(self):
            self.pressData = i2cBus.read_i2c_block_data(pressAddr, begAddr, totBytes)   # Block Read transaction for Pressure
            print("SenseHat Pressure Reading \t", self.pressData)
        
        '''
        Function for displaying humidity data from SenseHat LED to console.
        ''' 
        def displayHumidityData(self):
            self.humidData = i2cBus.read_i2c_block_data(humidAddr, begAddr, totBytes)   # Block Read transaction for humidity
            print("SenseHat Humidity Reading \t", self.humidData) 
        
        '''
        Overriding the run method in Thread sub-class to suit our purpose for
        continuously displaying the readings on console. 
        '''     
        def run(self):
            while True:
                if self.enableEmulator:
                    print("------------------")
                    self.displayAccelerometerData()
                    self.displayMagnetometerData()
                    self.displayPressureData()
                    self.displayHumidityData()
                    sleep(self.rateInSec)
                    
        '''
        Enables the Emulator before running the Thread
        '''                
        def enableEmulator(self):
            self.enableEmulator = True

