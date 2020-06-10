'''
Created on Mar 2, 2019
@author: Suraj
'''

from labs.module06 import MqttClientConnector

connector = MqttClientConnector.MqttClientConnector()           #MQTT instance to connect the MQTT Broker
print(type(connector.message()))                                #Connecting the Broker                             
connector.connect(None, None)
connector.publishMessage("mytest", connector.message(), 2)      #Publishing the message on the Broker
connector.disconnect()                                          #Disconnecting from Broker

