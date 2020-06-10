'''
Created on Mar 18, 2019
@author: Suraj
'''

from coapthon.server.coap import CoAP
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst
from labs.module07.TempResourceHandler import TempResourceHandler

class CoapServerConnector(CoAP):
    
    '''
    This is the implementation of the CoAP server.
    '''
    def __init__(self):
        '''
        This is the default constructor.
        It takes the host and port values and set them as CoAP server
        It adds the resources to server
        '''
        
        self.config = ConfigUtil()
        self.config.loadConfig()
        self.coapHost = self.config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.HOST_KEY)
        self.coapPort = int (self.config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.PORT_KEY))
        CoAP.__init__(self, (self.coapHost,self.coapPort))
        print(self.coapHost)
        print(self.coapPort)
        self.add_resource('temperature/', TempResourceHandler())
        
    def start(self):
        '''
        This function starts the server and opens the port to listen mode for
        clients to connect.
        On keyboard interrupt it would close the connection.
        '''
        
        try:
            self.listen(10)
        except KeyboardInterrupt:
            print("Server is being shutdown.")
            self.close()