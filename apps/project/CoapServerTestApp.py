'''
Created on Mar 18, 2019
@author: Suraj
'''

from labs.module07.CoapServerConnector import CoapServerConnector

'''
This is the python script to start CoAP Server
'''
print("CoAP at Python---Server side")
coapServer = CoapServerConnector()  #Initiate the CoapServer Connector
coapServer.start()  #It starts the server and open for client request