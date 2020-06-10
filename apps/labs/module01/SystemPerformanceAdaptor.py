from threading import Thread  # threading module is used to import Thread class
import psutil as psu  # psutil is used for retrieving information on running processes and system utilization
from time import sleep  # sleep will suspend execution for the given number of seconds


class SystemPerformanceAdaptor(Thread):  # We are creating sub-class SystemPerformanceAdaptor from Thread class

	def __init__(self, threadID, name, counter):  # Overriding constructor __init__ here with parameters
		Thread.__init__(self)  # Calling __init__(self) from parent class Thread
		self.threadID = threadID  # initializing Thread ID
		self.enable_Adaptor = False  # initializing enable_Adaptor
		self.name = name  # initializing name of the Thread
		self.counter = counter  # initializing counter for thread i.e how many threads we want to create
		self.sleep_cycle = 10  # Specifies suspend time for the next reading
	
	def run(self):  # Overriding the run method in Thread class
		while True:  # Creating infinite loop to take the readings
				if self.enable_Adaptor:
					print("New system performance readings-->\n")
					print("  CPU statistics " + str(psu.cpu_stats()))  # Return various CPU statistics as a named tuple
					print("  Virtual Memory statistics " + str(psu.virtual_memory()))  # Return statistics about system memory usage as a named tuple
				sleep(self.sleep_cycle)  # Specifying wait time of 5 seconds before taking next reading
	
	def enableAdaptor(self):  # Defining function to enable adaptor so that it can enable adaptor before running thread
		self.enable_Adaptor = True  # enable_Adaptor will be changed to True before starting the Thread
		
