'''
Created on Mar 2, 2019
@author: Suraj
'''

import logging
import paho.mqtt.client as mqttClient
from    time        import sleep
from    labs.common import ConfigUtil
from    labs.common import SensorData
from    time        import sleep
from    datetime    import datetime
from    labs.common import DataUtil
from    labs.common import ConfigConst


class MqttClientConnector(object):
    
    port = None
    brokerAddr=""
    brockerKeepAlive = None
    mqttClient=None
    config = None
    dataUtil = None
    
    def __init__(self):
        self.mqttClient = mqttClient.Client()                       #instance of the Client class of paho
        self.config = ConfigUtil.ConfigUtil('../../../config/data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        self.brokerAddr = self.config.getProperty(ConfigConst.MQTT_CLOUD_SECTION, ConfigConst.CLOUD_MQTT_BROKER)
        self.port = int(self.config.getProperty(ConfigConst.MQTT_CLOUD_SECTION,ConfigConst.CLOUD_MQTT_PORT))
        self.brockerKeepAlive = int(self.config.getProperty(ConfigConst.MQTT_CLOUD_SECTION,ConfigConst.KEEP_ALIVE_KEY))
        self.dataUtil = DataUtil.DataUtil()
        self.sensoData = SensorData.SensorData()                    #instance of SensorData class
        print(self.port)
    
    ''' 
    Function to connect to the Broker
    '''    
    def connect(self, connectionCallback = None , msgCallback = None):
        if(connectionCallback!=None):
            self.mqttClient.on_connect = connectionCallback
        else:
            self.mqttClient.on_connect = self.onConnect
            
        if(msgCallback !=None) :
            self.mqclient.on_disconnect = msgCallback
        else :
            self.mqttClient.on_disconnect = self.onMessage
            
        self.mqttClient.on_message = self.onMessage    
        print("Establishing connection with the broker",self.brokerAddr)
        self.mqttClient.connect(self.brokerAddr, self.port, self.brockerKeepAlive)
        #Connecting to the brokers address on the props file and keeping live for 60 sec
    
    '''
    This function will disconnect from the Broker
    '''    
    def disconnect(self):
        print("Disconneting the connection ")
        self.mqttClient.disconnect()
    
    '''
    This function will display success message when the return
    code is 0 during broker connection
    '''    
    def onConnect(self , client ,userData , flags , rc):
        if rc == 0:
            print("Code Returned for connection" , rc)
        else:
            print("Bad connection Returned Code:", rc)
    
    '''
    Function to print the MQTT message
    @param msg: The message which we are sending via Broker
    '''        
    def onMessage(self , client ,userdata , msg):
        print("Our topic is " +msg.topic + "-->" + "'This is a test...'")
        
    '''
    This function is used to publish the message
    @param topic : Topic of the payload message
    @param msg: the actual payload message
    @param qos: stands for quality of service, how hard the broker/client will 
    try to ensure that a message is received., using the value as 2
    '''
    def publishMessage(self , topic , msg , qos=2):   
        self.mqttClient.loop_start()
        self.mqttClient.publish(topic, msg, qos)
        sleep(100)
        self.mqttClient.loop_stop()
    ''' 
    This function is used to subscribe to the topic
    @param topic : The topic at which message is subscribed
    @param qos: stands for quality of service, how hard the broker/client will 
    try to ensure that a message is received., using the value as 2  
    '''
    def subscibetoTopic(self , topic , connnectionCallback = None , qos=2):
        if (connnectionCallback != None):
            self.mqttClient.on_subscribe(connnectionCallback)
            self.mqttClient.on_message(connnectionCallback)
        
        self.mqttClient.loop_start()    
        self.mqttClient.subscribe(topic , qos)
        sleep(100)
        self.mqttClient.loop_stop()
    
    '''
    Function to unsubscribe from a topic
    '''    
    def unsubscibefromTopic(self , topic , connnectionCallback = None ):
        if (connnectionCallback != None):
            self.mqttClient.on_unsubscribe(connnectionCallback)
               
        self.mqttClient.unsubscribe(topic)
    
    '''
    Actual message which we want to send
    '''    
    def message(self):
        self.sensoData.curValue = 20
        self.sensoData.avgValue = 25
        self.sensoData.maxValue = 30
        self.sensoData.minValue = 4
        self.sensoData.timeStamp = str(datetime.now())
        self.sensoData.samples = 7
        self.Jmsg = self.sensoData.fromSensortoJson(self.sensoData)
        return self.Jmsg