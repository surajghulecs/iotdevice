'''
Created on Jan 21, 2019
@author: Suraj
'''

import configparser
import os
'''
For env rasp pi use below config file path
DEFAULT_CONFIG_FILE_NAME = '/home/pi/workspace/iot-device/config/data/ConnectedDevicesConfig.props'
For local env use below config path
DEFAULT_CONFIG_FILE_NAME = '../../../config/data/ConnectedDevicesConfig.props'
'''
DEFAULT_CONFIG_FILE = '../../../config/data/ConnectedDevicesConfig.props'   # path for ConnectedDevicesConfig.props

class ConfigUtil:
    
    configFile = DEFAULT_CONFIG_FILE
    configData = configparser.ConfigParser()
    isLoaded = False
    
    '''
    Constructor for ConfigUtil, overrides the value for configFile to configFile
    '''  
    def __init__(self, configFile=None):
        if (configFile != None):
            self.configFile = configFile
            
    '''
    Checks for the path of configFile
    '''          
    def loadConfig(self):
        if(os.path.exists(self.configFile)):
            self.configData.read(self.configFile)
            self.isLoaded = True
    
    '''
    Checks if configParser loaded the configuration file
    @return: parsed information in configData
    '''
    def getConfig(self, forceReload=False):
        if(self.isLoaded == False or forceReload):
            self.loadConfig()
        return self.configData
    
    '''
    @return: returns the configFile to be parsed
    '''
    def getConfigFile(self):
        return self.configFile
    
    '''
    extracts the property from configuration file
    @param section: section name from configuration file
    @param key: value of property from configuration file  
    @return: property from the configuration file
    '''
    def getProperty(self, section, key, forceReload=False):
        return self.getConfig(forceReload).get(section, key)
    
    '''
    Used to check if configuration data is loaded
    @return: True - if configuration data is loaded, False if configuration data fails to load
    '''
    def isConfigDataLoaded(self):
        return self.isLoaded

        
