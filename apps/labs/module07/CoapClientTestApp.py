'''
Created on Mar 20, 2019
@author: Suraj
'''

from labs.common import SensorData
from labs.module07 import CoapClientConnector

print("Python: Client side for CoAP Protocol")
coapClientSD = SensorData.SensorData()                            #Creating a sensor data object to handle Coap Client
coapClient = CoapClientConnector.CoapClientConnector()
coapClientSD.addValue(37)
coapClient.coap_ping()                                            #Calling the function to send a ping
coapClient.http_get()                                             #Calling the function to print the response of HTTP get request
coapClient.http_post(coapClientSD.fromSensortoJson(coapClientSD ))#Calling the function to print the response of HTTP post request
coapClient.http_get()
coapClientSD.addValue(1)                                         #Calling the function to add value to sensor data
coapClient.http_put(coapClientSD.fromSensortoJson(coapClientSD )) #Calling the function to print the response of HTTP put request
coapClient.http_get()
coapClient.http_delete()                                          #Calling the function to print the response of HTTP delete request
coapClient.http_get()
coapClient.http_stop()                                            #Calling the function to terminate the Coap connection