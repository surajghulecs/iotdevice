'''
Created on Feb 13, 2019
@author: Suraj
'''
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
import json

ActuatorData = ActuatorData()
SensorData = SensorData()

class DataUtil(object):

    def __init__(self):
        '''
        Constructor
        '''
    def jsonToActuatorData(self, jsonData):
        adDict = json.loads(jsonData)
        #print(" decode [pre] --> " + str(adDict))
        ad = ActuatorData.ActuatorData()
        ad.name = adDict['name']
        ad.timeStamp = adDict['timeStamp']
        ad.hasError = adDict['hasError']
        ad.command = adDict['command']
        ad.errCode = adDict['errCode']
        ad.statusCode = adDict['statusCode']
        ad.stateData = adDict['stateData']
        ad.curValue = adDict['curValue']
        #print(" decode [post] --> " + str(ad))
        return ad
    
    def jsonToSensorData(self, jsonData):
        sdDict = json.loads(jsonData)
        #print(" decode [pre] --> " + str(sdDict))
        sd = SensorData.SensorData()
        sd.name = sdDict['name']
        sd.timeStamp = sdDict['timeStamp']
        sd.avgValue = sdDict['avgValue']
        sd.minValue = sdDict['minValue']
        sd.maxValue = sdDict['maxValue']
        sd.curValue = sdDict['curValue']
        sd.totValue = sdDict['totValue']
        sd.sampleCount = sdDict['sampleCount']
        #print(" decode [post] --> " + str(sd))
        return sd    