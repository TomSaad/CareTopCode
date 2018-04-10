#Title: 	care_top.py
#Date:		March 27, 2018
#Contributors	David St-Pierre stpied@rpi.edu
#
#NOTES:
#Functions to control
#	- Humidity
#	- Reading Sensors
#	- Writing to json website file
#	- Checking data to see if need to do function

#-----------------
# Imports
#-----------------
import time		#Used for delays
import datetime		#Used to get the date and time (for feeding)
#import jeffery.sensors	#Class easing the use of the sensors
#import jeffery.jsonlog	#
import RPi.GPIO as GPIO
import logging
import json

#------
# SETUP
#------

logging.basicConfig(filename='example.log',level=logging.DEBUG) #Change to INFO?  Change to date.log

logging.info
								#Log a message everytime a new event takes place
logging.info('----------------------------')
logging.info('STARTUP: ' + str(datetime.datetime.now()))
logging.info('----------------------------')

#Variable to keep track of whether or not debugging is taking place
DEBUG = True

###GPIO SETUP
GPIO.setwarnings(False)

#Use the BCM numbers not the direct pin numbers
GPIO.setmode(GPIO.BCM)

HUMIDITY_PWR_PIN = 22
SERVO_SIGNAL_PIN = 18
SERVO_1_PWR_PIN = 2
SERVO_2_PWR_PIN = 3
SERVO_3_PWR_PIN = 4
SERVO_4_PWR_PIN = 17
SERVO_5_PWR_PIN = 27

GPIO.setup(HUMIDITY_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_1_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_2_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_3_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_4_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_5_PWR_PIN, GPIO.OUT)

#
# SPECIAL SET UP FOR SERVO TIMING PIN
#



#--------
# RUNNING (LOOP)
#--------

#There is a desired value for the humidity, when the hysteresis is true, CareTop is trying to get to the desired
#humidity, when hysteresis is false, careTop is letting the value drift until it passes outside of desired bounds
#humidity_hysteresis = true	

def main():
	while(True):
		now = datetime.datetime.now()	
		
		#------------------------
		# Open and read JSON files
		#------------------------
	
		#Important to read JSON file everytime through loop incase a change has been made
	
		f = open('config_ex.json', 'r')     	#open the text file and make into string
		string = f.read()                   	#in real life check to make sure that the file exists
	
		#Print json string for 
		if(DEBUG):
			print(string)
		
	#	data = json.loads(string)           	#load the string into json
		
		if(DEBUG):
			print("[DEBUG]")
	#		print(data["running"])          #use it like a dictionary (cause it is)
	
	
		#Gets the desired humidity value from the website
		desired_humidity = 0			
		
		#Gets the margins that are acceptable humidity from the website -> Hardcoded?
		humidity_margin = 0
	
		#Calculates the max and min values for humidity -> for use in hysterisis
		#Only need min_humidity because we have no way of removing humidity
		min_humidity = desired_humidity - humidity_margin
		
		
		#-------------
		# Read sensors
		#-------------
		actual_humidity = 8
		#----------------------------------
		# Upload new information to website
		#----------------------------------
	
		#-----------------------
		# Check for feeding time
		#-----------------------
		#Get the current time and divide it into its useful components
		date = now.date()
		my_time = now.time()	#Called my_time so as to not interfere with time.sleep() instatance
		year = date.year
		month = date.month
		day = date.day
		hour = my_time.hour
		minute = my_time.minute
		second = my_time.second

		#Print them out as a debug exercise
		if(DEBUG):
			print("Date = " + str(month) + "/" + str(day) + "/" + str(year))
			print("Time = " + str(hour) + ":" + str(minute) + ":" + str(second))
			date_str_1 = "Date = " + str(month) + "/" + str(day) + "/" + str(year)
			date_str_2 = "Time = " + str(hour) + ":" + str(minute) + ":" + str(second)
	
			logging.debug(date_str_1)
			logging.debug(date_str_2)
			
		#-------------------------
		# Check to change humidity
		#-------------------------



		#Mush slo, no fasst
		time.sleep(1)
	

		if(0):
			logging.warning('If this message is being printed.....RUN.......RUN FAR')

try:
	main()
except KeyboardInterrupt:
	logging.info("Program stopped normally by user")
	print("Program stopped normally by user")
