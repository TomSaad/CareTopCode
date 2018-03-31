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
#import jeffery.sensors	#Class easing the use of the sensors
#import jeffery.jsonlog	#
import RPi.GPIO as GPIO
import logging

#------
# SETUP
#------

logging.basicConfig(filename='example.log',level=logging.DEBUG) #Change to INFO?  Change to date.log
								#Log a message everytime a new event takes place
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

#Variable to keep track of whether or not debugging is taking place
DEBUG = FALSE

###GPIO SETUP
GPIO.setwarnings(False)

#Use the BCM numbers not the direct pin numbers
GPIO.setmode(GPIO.BCM)

HUMIDITY_PWR_PIN = 
SERVO_SIGNAL_PIN = 
SERVO_1_PWR_PIN = 
SERVO_2_PWR_PIN = 
SERVO_3_PWR_PIN = 
SERVO_4_PWR_PIN = 
SERVO_5_PWR_PIN = 

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

while(True):

	#------------------------
	# Open and read JSON files
	#------------------------

	#Important to read JSON file everytime through loop incase a change has been made

	f = open('config_ex.json', 'r')     	#open the text file and make into string
	string = f.read()                   	#in real life check to make sure that the file exists

	#Print json string for 
	if(DEBUG):
		print(string)
	
	data = json.loads(string)           	#load the string into json
	
	if(DEBUG):
		print(data["running"])          #use it like a dictionary (cause it is)


	#Gets the desired humidity value from the website
	desired_humidity = 			
	
	#Gets the margins that are acceptable humidity from the website -> Hardcoded?
	humidity_margin = 

	#Calculates the max and min values for humidity -> for use in hysterisis
	#Only need min_humidity because we have no way of removing humidity
	min_humidity = desired_humidity - humidity_margin
	
	
	#-------------
	# Read sensors
	#-------------
	
	#----------------------------------
	# Upload new information to website
	#----------------------------------

	#-----------------------
	# Check for feeding time
	#-----------------------

	#-------------------------
	# Check to change humidity
	#-------------------------






