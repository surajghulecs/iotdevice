'''
Created on Mar 20, 2019
@author: Suraj
'''

from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst
from coapthon.client.helperclient import HelperClient

class CoapClientConnector():
    
    '''
    Constructor
    '''
    def __init__(self):
        self.config = ConfigUtil()
        self.config.loadConfig()
        self.coapHost = self.config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.HOST_KEY)
        self.coapPort = int (self.config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.PORT_KEY))
        self.coapPath = 'temperature'
        self.coapClient = HelperClient(server=(self.coapHost, self.coapPort))
    
    '''
    Function to send a ping to the Coap client
    '''    
    def coap_ping(self):
        self.coapClient.send_empty("")
    
    '''
    Function to display the response received for HTTP's get request
    '''    
    def http_get(self):
        output = self.coapClient.get(self.coapPath)
        print(output.pretty_print())
    
    '''
    Function to display the response received for HTTP's post request
    ''' 
    def http_post(self, data_in):
        output = self.coapClient.post(self.coapPath, data_in)
        print(output.pretty_print())
    
    '''
    Function to display the response received for HTTP's put request
    '''     
    def http_put(self, data_in):
        output = self.coapClient.put(self.coapPath, data_in)
        print(output.pretty_print())
    
    '''
    Function to display the response received for HTTP's delete request
    '''     
    def http_delete(self):
        output = self.coapClient.delete(self.coapPath)
        print(output.pretty_print())
    
    '''
    Function to terminate the coap connection
    '''    
    def http_stop(self):
        self.coapClient.stop()