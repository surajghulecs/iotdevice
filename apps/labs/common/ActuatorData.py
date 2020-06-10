'''
Created on Feb 1, 2019
@author: Suraj
'''

import os
import json
from datetime import datetime
COMMAND_OFF = 0
COMMAND_ON = 1
COMMAND_SET = 2
COMMAND_RESET = 3
STATUS_IDLE = 0
STATUS_ACTIVE = 1
ERROR_OK = 0
ERROR_COMMAND_FAILED = 1
ERROR_NON_RESPONSIBLE = -1

class ActuatorData():
    
    timeStamp = None
    name = 'Not set'
    hasError = False
    command = 0
    errorCode = 0
    statusCode = 0
    stateData = None
    val = 0.0
    
    def __init__(self):
        self.updateTimeStamp()
        
    def getCommand(self):
        return self.command
    
    def getName(self):
        return self.name
    
    def getStateData(self):
        return self.stateData
    
    def getStatusCode(self):
        return self.statusCode
    
    def getErrorCode(self):
        return self.errorCode
    
    def getValue(self):
        return self.val;
    
    def hasError(self):
        return self.hasError
    
    def setCommand(self, command):
        self.command = command
        
    def setName(self, name):
        self.name = name
        
    def setStateData(self, stateData):
        self.stateData = stateData
        
    def setStatusCode(self, statusCode):
        self.statusCode = statusCode
        
    def setErrorCode(self, errCode):
        self.errCode = errCode
        if (self.errCode != 0):
            self.hasError = True
        else:
            self.hasError = False
            
    def setValue(self, val):
        self.val = val
        
    def updateData(self, data):
        self.command = data.getCommand()
        self.statusCode = data.getStatusCode()
        self.errCode = data.getErrorCode()
        self.stateData = data.getStateData()
        self.val = data.getValue()
        
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())
            
    def __str__(self):
        customStr = \
            str(self.name + ':' + \
            os.linesep + '\tTime: ' + self.timeStamp + \
            os.linesep + '\tCommand: ' + str(self.command) + \
            os.linesep + '\tStatus Code: ' + str(self.statusCode) + \
            os.linesep + '\tError Code: ' + str(self.errCode) + \
            os.linesep + '\tState Data: ' + str(self.stateData) + \
            os.linesep + '\tValue: ' + str(self.val))
        return customStr
    
    '''
    Converts the Actuator data to JSON object
    @param obj: Actuator data object to be converted to JSON using Json dumps
    @return j:  JSON data object to be sent in email and displayed on console
    ''' 
    def fromActuatortoJson(self, obj):
        j = json.dumps(obj.__dict__)
        return j
    
    '''
    Converts the JSON object to Actuator Data in string format
    @param jsonData: JSON object to be converted to Actuator data string format
    @return ad: Actuator data in String format 
    ''' 
    def jsonToActuatorData(self, jsonData):
        adDict = json.loads(jsonData)
        ad = ActuatorData.ActuatorData()
        ad.name = adDict['name']
        ad.timeStamp = adDict['timeStamp']
        ad.hasError = adDict['hasError']
        ad.command = adDict['command']
        ad.errCode = adDict['errCode']
        ad.statusCode = adDict['statusCode']
        ad.stateData = adDict['stateData']
        ad.curValue = adDict['curValue']
        return ad        