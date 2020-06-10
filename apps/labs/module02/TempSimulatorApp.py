'''
Created on Jan 21, 2019
@author: suraj
'''
from labs.module02 import TempSensorEmulator
from time import sleep

TempSimulatorApp = TempSensorEmulator.TempSensorEmulator()  # Creating an instance of TempSensorEmulator class
TempSimulatorApp.daemon = True                              # Specifying instance to use thread as daemon process
print ("Temperature readings")
TempSimulatorApp.enableEmulator()                           # Changing the enableEmulator from False to True
wait = 5                                                    # Wait time of 5 seconds for CPU to give it a break
TempSimulatorApp.start()                                    # The thread to collect system performance will be started here
while (True):                                               # infinite loop
    sleep(wait)                                             # method for giving CPU a break of 5 seconds called
    pass                                                    # executes the current loop and pass execution to next iteration
    
