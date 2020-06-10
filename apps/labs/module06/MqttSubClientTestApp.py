'''
Created on Mar 2, 2019
@author: Suraj
'''

from labs.module06 import MqttClientConnector
        
connector = MqttClientConnector.MqttClientConnector()   #MQTT instance to connect the MQTT Broker
connector.connect(None, None)                           #Connecting the Broker
connector.subscibetoTopic("MQ Test")                       #Subscribing the Topic
connector.disconnect()                                  #Disconnecting from Broker