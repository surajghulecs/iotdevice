'''
Created on Jan 21, 2019
@author: Suraj
'''

import sys,os,json											# Importing the required libraries
sys.path.insert(0,'/home/pi/workspace/iot-device/apps')		# Adding the path for raspberry pi console
from datetime import datetime								# Importing datetime library
from sense_hat 		import 	SenseHat						# Imprting the SenseHat library	
from time 			import 	sleep							# Importing sleep module
from project 		import 	SmtpClientConnector				# Importing SmtpClientConnector module
				
sense = SenseHat()											# Creating instance of SenseHat
sense.clear()												# Clearing the sensehat screen
smtpconnector = SmtpClientConnector.SmtpClientConnector()   # Create an instance of SmtpClientConnector
rateInSec = 1												# Wait time for Weather app

class WeatherData():
	
	'''
	Initializing the variables for Weather class
	'''		
	name = "SenseHAT Data"
	timeStamp = None
	temp = 0
	humidity = 0
	pressure = 0
	magnetometer1 = 0
	accelerometer = 0
	
	'''
	Defining the constructor
	'''
	def __init__(self):
		self.timeStamp = str(datetime.now())
		self.name = "SenseHAT Data"
		self.temp = 0
		self.humidity = 0
		self.pressure = 0
		self.magnetometer1 = 0
		self.accelerometer = 0
	
	'''
	Fetching the temperature value
	@param self:keyword for object of Weather
	@return sense_temp:temperature reading from SenseHAT
	'''	
	def getTempValue(self):
		sense_temp = sense.get_temperature()
		return sense_temp
	
	'''
	Fetching the temperature value
	@param self:keyword for object of Weather
	@return sense_humidity:humidity reading from SenseHAT
	'''		
	def getHumidityValue(self):
		sense_humidity = sense.get_humidity()
		return sense_humidity
	
	'''
	Function to print the Sensor readings
	@param self:keyword for object of Weather
	@return: None
	'''
	def addvalue(self):
			
			'''
			Taking accelerometer readings
			'''
			self.acceleration = sense.get_accelerometer_raw()
			x = self.acceleration["x"]
			y = self.acceleration["y"]
			z = self.acceleration["z"]
			x=round(x, 0)
			y=round(y, 0)
			z=round(z, 0)
			print('Accelerometer')
			print("x={0}, y={1}, z={2}".format(x, y, z))
			self.accelerometer = "x={0}, y={1}, z={2}".format(x, y, z)
			
			'''
			Taking temperature readings
			'''
			self.temp = sense.get_temperature()
			self.temp = round(self.temp, 1)
			print("Temperature C",self.temp) 
			
			'''
			Taking humidity readings
			'''
			self.humidity = sense.get_humidity()  
			self.humidity = round(self.humidity, 1)  
			print("Humidity :",self.humidity)  
			
			'''
			Taking Pressure readings
			'''
			self.pressure = sense.get_pressure()
			self.pressure = round(self.pressure, 1)
			print("Pressure:",self.pressure)
			
			'''
			Taking magnetometer readings
			'''
			self.magnetometer = sense.get_compass_raw()
			print("Magnetometer:",self.magnetometer)
			self.orientation = sense.get_orientation ()
			pitch = self.orientation['pitch']
			roll = self.orientation['roll']
			yaw = self.orientation['yaw']
			pitch = round (pitch,0)
			roll = round (roll,1)
			yaw = round(yaw,2)
			print("pitch={0}, roll={0}, yaw={0}".format(pitch,yaw,roll))
			self.magnetometer1 = "pitch={0}, roll={0}, yaw={0}".format(pitch,yaw,roll)
			
			'''
			Showing the data on SenseHat
			'''
			sense.show_message("Temperature C" + str(self.temp) + "Humidity:" + str(self.humidity) + "Pressure:" + str(self.pressure) + "x={0}, y={1}, z={2}".format(x, y, z), scroll_speed=(0.08), back_colour= [0,0,200])	
			sleep(rateInSec)
			sense.clear()
			
	'''
	Function to convert the Sensor data to Json object
	@param self:keyword for object of Weather
	@param obj:Object of Sensor data
	'''
	def fromSensortoJson(self,obj):
			json_string = json.dumps(obj.__dict__)
			return json_string
	
	'''
	Function to convert object variables to string
	@param self:keyword for object of Weather
	@return customStr:Modified string in our specified format
	'''
	def __str__(self):
		customStr = \
			str(self.name + ":" + \
			os.linesep + "\tTime:" + self.timeStamp + \
			os.linesep + "\tTemperature:" + str(self.temp) + \
			os.linesep + "\tPressure:" + str(self.pressure) +  \
			os.linesep + "\tHumidity:" + str(self.humidity) + \
			os.linesep + '\tAccelerometer:' + str(self.accelerometer) + \
			os.linesep + '\tMagnetometer:' + str(self.magnetometer1))
		return customStr
	
	'''
	Function to convert Json object to String format
	@param self:keyword for object of Weather
	@param obj:Object of Sensor data
	return sd:Sensor data object
	'''
	def jsonToSensorData(self, jsonData):
		sdDict = json.loads(jsonData)
		sd = WeatherData
		sd.name = sdDict['name']
		sd.timeStamp = sdDict['timeStamp']
		sd.avgValue = sdDict['avgValue']
		sd.minValue = sdDict['minValue']
		sd.maxValue = sdDict['maxValue']
		sd.curValue = sdDict['curValue']
		sd.totValue = sdDict['totValue']
		sd.sampleCount = sdDict['sampleCount']
		return sd
		

