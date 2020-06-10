'''
Created on Jan 21, 2019
@author: Suraj
'''

import os
import json

from datetime import datetime

class SensorData():
    
    timeStamp = None
    name = 'Sensor Data at Roxbury'
    curValue = 0
    avgValue = 0
    minValue = 40
    maxValue = 0
    totalValue = 0
    sampleCount = 0
    
    '''
    Constructor for SensorData class, sets the timestamp to current Date and time
    '''
    def __init__(self):
        self.timeStamp = str(datetime.now())
    
    '''
    Compares the new temperature value with current temperature value, both min and max values.
    If its lower than min or higher than max, assigns the new min and max values.
    Calculates the average temperature reading.
    @param newValue: new reading sent by SensorData
    '''    
    def addValue(self, newValue):
        self.sampleCount += 1
        
        self.timeStamp = str(datetime.now())
        self.curValue = newValue
        self.totalValue += newValue
        
        if(self.curValue < self.minValue):
            self.minValue = self.curValue
            
        if(self.curValue > self.maxValue):
            self.maxValue = self.curValue
        
        if(self.totalValue != 0 and self.sampleCount > 0):
            self.avgValue = self.totalValue / self.sampleCount
    '''
    @return: average temperature value
    '''        
    def getAvgValue(self):
        return self.avgValue
    
    '''
    @return: maximum temperature value
    '''
    def getMaxValue(self):
        return self.maxValue
    
    '''
    @return: minimum temperature value
    '''
    def getMinValue(self):
        return self.minValue
    
    '''
    @return: current temperature value
    '''
    def getValue(self):
        return self.curValue
    
    def setName(self, name):
        self.name = name
    
    '''
    Converts the object and its attributes to a string value which will be displayed on console or 
    in trigger email
    @return: String
    '''    
    def __str__(self):
        customStr = \
            str(self.name + ':' + \
            os.linesep + '\tTime:    ' + self.timeStamp + \
            os.linesep + '\tCurrent: ' + str(self.curValue) + \
            os.linesep + '\tAverage: ' + str(self.avgValue) + \
            os.linesep + '\tSamples: ' + str(self.sampleCount) + \
            os.linesep + '\tMin: ' + str(self.minValue) + \
            os.linesep + '\tMax: ' + str(self.maxValue))     
        return customStr
    
    '''
    Converts the Sensor data to JSON data format
    @param obj: Sensor data object to be converted to JSON using Json dumps
    @return j:  JSON data object
    '''        
    def fromSensortoJson(self, obj):
        j = json.dumps(obj.__dict__)
        return j
      
    
    '''
    Converts the JSON object to Sensor Data in string format
    @param jsonData: JSON object to be converted to string format
    @return sd: Sensor data in String format   
    '''
    def jsonToSensorData(self, jsonData):
        sdDict = json.loads(jsonData)
        sd = SensorData()
        #sd.name = sdDict['name']
        sd.timeStamp = sdDict['timeStamp']
        sd.avgValue = sdDict['avgValue']
        sd.minValue = sdDict['minValue']
        sd.maxValue = sdDict['maxValue']
        sd.curValue = sdDict['curValue']
        sd.totValue = sdDict['totalValue']
        sd.sampleCount = sdDict['sampleCount']
        return sd 