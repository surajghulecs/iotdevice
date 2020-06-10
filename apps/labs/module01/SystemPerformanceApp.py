'''
Created on Jan 21, 2019
@author: suraj
'''
from labs.module01 import SystemPerformanceAdaptor
from time import sleep
# Importing the necessary libraries and modules

SysPerApp = SystemPerformanceAdaptor.SystemPerformanceAdaptor(1, "System Performance Adaptor", 1)
# Specifying the thread ID, Thread Name and number of threads to be created in SysPerApp object
SysPerApp.daemon = True  # SysPerApp will be created as daemon process
print ("Starting system performance reading application as background process")
SysPerApp.enableAdaptor()  # Changing the enable_Adaptor from False to True
wait = 5  # Wait time of 5 seconds for CPU to give it a break

SysPerApp.start()  # The thread to collect system performance will be started here

while (True):  # infinite loop
    sleep(wait)  # method for giving CPU a break of 5 seconds called
    pass  # executes the current loop and the execution goes to second loop after this
    
    