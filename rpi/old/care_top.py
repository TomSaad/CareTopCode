#Title: 	care_top.py
#Date:		April 23, 2018
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

logging.basicConfig(filename='log.log',level=logging.INFO) #Change to INFO?  Change to date.log

logging.info('----------------------------')
logging.info('STARTUP: ' + str(datetime.datetime.now()))
logging.info('----------------------------')

#Variable to keep track of whether or not debugging is taking place
DEBUG = True
NO_SENSORS = True
###GPIO SETUP
GPIO.setwarnings(False)

#Use the BCM numbers not the direct pin numbers
GPIO.setmode(GPIO.BCM)

HUMIDITY_PWR_PIN = 8
SERVO_SIGNAL_PIN = 18
SERVO_1_PWR_PIN = 14
SERVO_2_PWR_PIN = 15
SERVO_3_PWR_PIN = 23
SERVO_4_PWR_PIN = 24
SERVO_5_PWR_PIN = 25

GPIO.setup(HUMIDITY_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_1_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_2_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_3_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_4_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_5_PWR_PIN, GPIO.OUT)
GPIO.setup(SERVO_SIGNAL_PIN, GPIO.OUT)

#
# SPECIAL SET UP FOR SERVO TIMING PIN
#

servo = GPIO.PWM(SERVO_SIGNAL_PIN, 50)

servo.start(7.5)
time.sleep(2)

#--------
# Servo control functions
#--------

def hum_on():
	GPIO.output(HUMIDITY_PWR_PIN, 1)

def hum_off():
	GPIO.output(HUMIDITY_PWR_PIN, 0)

def all_off():
	GPIO.output(SERVO_1_PWR_PIN, 0)
	GPIO.output(SERVO_2_PWR_PIN, 0)
	GPIO.output(SERVO_3_PWR_PIN, 0)
	GPIO.output(SERVO_4_PWR_PIN, 0)
	GPIO.output(SERVO_5_PWR_PIN, 0)

def write_servo(pin, direction):
	all_off()
	servo.ChangeDutyCycle(direction)
	time.sleep(0.1)
	GPIO.output(pin, 1)
	time.sleep(1)
	GPIO.output(pin, 0)

#---------------
# WELCOME SCREEN FOR DEBUG
#---------------
if(DEBUG):
	print("----------------------------------------------")
	print("		    WELCOME TO CARETOP               ")
	print("----------------------------------------------")

#--------
# RUNNING (LOOP)
#--------

#There is a desired value for the humidity, when the hysteresis is true, CareTop is trying to get to the desired
#humidity, when hysteresis is false, careTop is letting the value drift until it passes outside of desired bounds

humidity_hysteresis = True


def main():
	logging.info("New session")
	no_sensor_line_cnt = 0
	while(True):
		logging.info("------------------------------------------------")
		now = datetime.datetime.now()

		#------------------------
		# Open and read JSON files
		#------------------------

		if(DEBUG):
			print("----------------------------------------------")
			print("		    CONFIGURATION FILE               ")
			print("		    LOADED FROM WEBSITE              ")
			print("----------------------------------------------")

		#Loading the configuration file

		f = open('config.json', 'r')

		string = f.read()

		data = json.loads(string)

		created = data["created"]
		start = data["start"]
		running = data["running"]
		dTemp = data["dTemp"]
		dHum = data["dHum"]
		feeding1 = data["feeding1"].split("&")
		feeding2 = data["feeding2"].split("&")
		feeding3 = data["feeding3"].split("&")
		feeding4 = data["feeding4"].split("&")
		feeding5 = data["feeding5"].split("&")
		feeding6 = data["feeding6"].split("&")
		feeding7 = data["feeding7"].split("&")
		feeding8 = data["feeding8"].split("&")
		feeding9 = data["feeding9"].split("&")
		feeding10 = data["feeding10"].split("&")


		if(DEBUG):
			print("Configuration file created: " + str(created))
			print("Started:             " + str(start))
			print("Running:             " + str(running))
			print("Desired Temperature: " + str(dTemp))
			print("Desired Humidity:    " + str(dHum))
			print("Feeding 1:           " + str(feeding1))
			print("Feeding 2:           " + str(feeding2))
			print("Feeding 3:           " + str(feeding3))
			print("Feeding 4:           " + str(feeding4))
			print("Feeding 5:           " + str(feeding5))
			print("Feeding 6:           " + str(feeding6))
			print("Feeding 7:           " + str(feeding7))
			print("Feeding 8:           " + str(feeding8))
			print("Feeding 9:           " + str(feeding9))
			print("Feeding 10:          " + str(feeding10))
			logging.info("Configuration file created: " + str(created))
			logging.info("Started:             " + str(start))
			logging.info("Running:             " + str(running))
			logging.info("Desired Temperature: " + str(dTemp))
			logging.info("Desired Humidity:    " + str(dHum))
			logging.info("Feeding 1:           " + str(feeding1))
			logging.info("Feeding 2:           " + str(feeding2))
			logging.info("Feeding 3:           " + str(feeding3))
			logging.info("Feeding 4:           " + str(feeding4))
			logging.info("Feeding 5:           " + str(feeding5))
			logging.info("Feeding 6:           " + str(feeding6))
			logging.info("Feeding 7:           " + str(feeding7))
			logging.info("Feeding 8:           " + str(feeding8))
			logging.info("Feeding 9:           " + str(feeding9))
			logging.info("Feeding 10:          " + str(feeding10))


		#Gets the desired humidity value from the website
		desired_humidity = dHum

		#Gets the margins that are acceptable humidity from the website -> Hardcoded?
		humidity_margin = 5

		#Calculates the max and min values for humidity -> for use in hysterisis
		#Only need min_humidity because we have no way of removing humidity
		min_humidity = desired_humidity - humidity_margin
		max_humidity = desired_humidity + humidity_margin

		#-------------
		# Read sensors
		#-------------

		#Read the sensor values
		actual_humidity = 64
		actual_temperature = 44

		#DEBUG MODE -> Reading data from a sample data file
		if(NO_SENSORS):
			file_name = "data.debug"
			file = open(file_name)
			lines = file.readlines()
			data_line = lines[no_sensor_line_cnt]
	        	sensor_data = data_line.split(",")
		        actual_humidity = sensor_data[0]
		        actual_temperature = sensor_data[1]
			no_sensor_line_cnt = no_sensor_line_cnt + 1
        	print("[DATA COLLECTED FROM SENSORS]")
	        print("[TEMPERATURE: " + actual_temperature)
	        print("[HUMIDITY: " + actual_humidity)

        	logging.info("[DATA COLLECTED FROM SENSORS]")
	        logging.info("[TEMPERATURE: " + actual_temperature)
	        logging.info("[HUMIDITY: " + actual_humidity)

		#----------------------------------
		# Upload new information to website
		#----------------------------------

		#Call a simple function from sensor library to export data to formatted file

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
		if(desired_humidity > max_humidity and humidity_hysteresis is true):
			hum_off()
			humidity_hysteresis = False
			logging.debug("[" + data + "] Turning humidity on")
		elif(desired_humidity < min_humidity and humidity_hysteresis is false):
			hum_on()
			humidity_hysteresis = True
			logging.debug("[" + data + "] Turning humidity off")


		#Mush slo, no fasst
		time.sleep(1)

try:
	main()
except KeyboardInterrupt:
	logging.info("Program stopped normally by user")
	print("Program stopped normally by user")
