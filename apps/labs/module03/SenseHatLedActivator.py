'''
Created on Feb 1, 2019
@author: Suraj
'''

from time import sleep
from sense_hat import SenseHat                                     #Sense HAT API
import threading

class SenseHatLedActivator(threading.Thread):
    
    '''
    Configuration for display on SenseHat
    '''
    enableLed = False
    rateInSec = 1
    rotateDeg = 270
    sh = None
    displayMsg = None
    
    '''
    Constructor
    '''
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        super(SenseHatLedActivator, self).__init__()
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg    
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)

    
    '''
    Thread for displaying LED messages.
    When nothing to display in displayMsg, it will show R else it will show displayMsg content
    '''    
    def run(self):
            if self.enableLed:
                if self.displayMsg != None:
                    self.sh.show_message(str(self.displayMsg))
                else:
                    self.sh.show_letter(str('R'))
                sleep(self.rateInSec)
                self.sh.clear()
            sleep(self.rateInSec)
            
    '''
    This function returns the rate at which reading is fetched per seconds
    '''            
    def getRateInSeconds(self):
        return self.rateInSec
    
    '''
    Enables the LED Flag adaptor
    '''    
    def setEnableLedFlag(self, enable):
        self.sh.clear()
        self.enableLed = enable
        
    '''
    Sets the display message to be shown on LED display
    '''        
    def setDisplayMessage(self, msg):
        self.displayMsg = msg
