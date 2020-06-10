'''
Created on Jan 21, 2019
@author: Suraj
'''

import sys,os													# Importing the library for raspberry pi path
sys.path.insert(0, '/home/pi/workspace/iot-device/apps')		# Defining the path for raspberry pi
from project  	import WeatherData								# Importing the Weather module	
from time           	import sleep							# Importing the sleep module
from labs.module04 		import SmtpClientConnector				# Importing the SmtpClientConnector for SMTP triggering
from sense_hat 			import SenseHat							# Importing the SenseHat library

smtpconnector = SmtpClientConnector.SmtpClientConnector()   	# Create an instance of SmtpClientConnector
sense = SenseHat()												# Instance of SenseHat
sense.clear()													# Clearing the SenseHat display

SensorReaderApp = WeatherData.WeatherData()       				# Creating an instance of I2CSenseHatAdaptor class
SensorReaderApp.daemon = True                                   # Specifying instance to use thread as daemon process
print ("Sensor Data from SenseHAT")                             # Changing the enableEmulator from False to True
wait = 5                                                        # Wait time of 5 seconds for CPU to give it a break
while (True):
	SensorReaderApp.addvalue()                              	# Changing the enableEmulator from False to True
	a = SensorReaderApp.__str__()								# Storing the Sensor reading apps in string format in a
	print (a)													# Displaying them on console
	'''
	Triggering an email based on SenseHAT temperature readings
	'''
	if (SensorReaderApp.getTempValue() > 25): 		
		print('\n  Current temp exceeds average by > Triggering alert...')    
		smtpconnector.publishMessage('Exceptional sensor data [test]', str(a))
		sense.show_message("Starting the Air Conditioner")
	sleep(wait)
	pass


