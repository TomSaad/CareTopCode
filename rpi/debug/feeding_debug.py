#Title: 	feeding_debug.py
#Date:		March 23, 2018
#		March 27, 2018
#			- Modifying for Kaitlyn to have a manual test program
#		April 1, 2018
#			- Correcting for flux capacitor compatability
#			- Troubleshooting door opening code
#			- Added an option for h to control humitity
#
#Contributors	David St-Pierre stpied@rpi.edu
#
#DESCRIPTION
#This progam allows a user to control the feeding servos directly using simple
#commands explained when the program is run
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
import RPi.GPIO as GPIO

###GPIO SETUP
GPIO.setwarnings(False)

#Use the BCM numbers not the direct pin numbers
GPIO.setmode(GPIO.BCM)

SERVO_SIGNAL_PIN = 18
SERVO_1_PWR_PIN = 2
SERVO_2_PWR_PIN = 3
SERVO_3_PWR_PIN = 4
SERVO_4_PWR_PIN = 17
SERVO_5_PWR_PIN = 27
HUMIDITY_PIN = 22

GPIO.setup(SERVO_SIGNAL_PIN, GPIO.OUT)
GPIO.setup(SERVO_1_PWR_PIN, GPIO.OUT, initial = 0)
GPIO.setup(SERVO_2_PWR_PIN, GPIO.OUT, initial = 0)
GPIO.setup(SERVO_3_PWR_PIN, GPIO.OUT, initial = 0)
GPIO.setup(SERVO_4_PWR_PIN, GPIO.OUT, initial = 0)
GPIO.setup(SERVO_5_PWR_PIN, GPIO.OUT, initial = 0)
GPIO.setup(HUMIDITY_PIN, GPIO.OUT, initial = 0)

servo = GPIO.PWM(SERVO_SIGNAL_PIN, 50)

servo.start(7.5)
time.sleep(2)


GPIO.output(HUMIDITY_PIN,1)		# Turn the humidity on
time.sleep(1)
GPIO.output(HUMIDITY_PIN,0)		# Turn the humidity on
time.sleep(1)
GPIO.output(HUMIDITY_PIN,1)		# Turn the humidity on
time.sleep(1)
GPIO.output(HUMIDITY_PIN,0)		# Turn the humidity on
time.sleep(1)



#Servo pulse mapping: 2.5 - 12.5 (0 - 180)

def all_off():
	GPIO.output(SERVO_1_PWR_PIN, 0)
	GPIO.output(SERVO_2_PWR_PIN, 0)
	GPIO.output(SERVO_3_PWR_PIN, 0)
	GPIO.output(SERVO_4_PWR_PIN, 0)
	GPIO.output(SERVO_5_PWR_PIN, 0)

def write_servo(pin, direction):
	all_off()			# Turn all servos off (catch all)
	servo.ChangeDutyCycle(direction)# Change the direction the servo pulses are giving
	time.sleep(0.1)			# Give a small delay
	GPIO.output(pin,1)		# Turn the servo on
	time.sleep(1)			# Let the servo get to the position
	GPIO.output(pin,0)		# Turn on the servo pin


print("-------------------------------------------")
print("		CARETOP FEEDING BEBUG		  ")
print("-------------------------------------------")
print("Controls:")
print("[Number of feeding (0-9][Open or closed (o or c)")
print(" ")
print("EXAMPLE")
print("Open door 3")
print(":3o")
print("Close door 5")
print(":5c")
print("-------------------------------------------")
print(" ")
print(" ")
print(" ")
while(True):
	cmd = raw_input(':')
	servo_num = 0
	if(cmd[0] == "0" or cmd[0] == "1"):
		servo_num = SERVO_1_PWR_PIN
	elif(cmd[0] == "2" or cmd[0] == "3"):
		servo_num  = SERVO_2_PWR_PIN
	elif(cmd[0] == "4" or cmd[0] == "5"):
		servo_num  = SERVO_3_PWR_PIN
	elif(cmd[0] == "6" or cmd[0] == "7"):
		servo_num  = SERVO_4_PWR_PIN
	elif(cmd[0] == "8" or cmd[0] == "9"):
		servo_num  = SERVO_5_PWR_PIN
	elif(cmd[0] == "h" or cmd[0] == "H"):
		servo_num  = -1

	if(servo_num > 0):
		if(cmd[1] == "o" or cmd[1] == "O"):
			if(int(cmd[0]) % 2 == 1):
				servo.ChangeDutyCycle(3)  	# Determine if open is one way or the other
				print("Servo " + str(servo_num) + " set to 3")
			else:
				servo.ChangeDutyCycle(12)
				print("Servo " + str(servo_num) + " set to 12")
		elif(cmd[1] == "c" or cmd[1] == "C"):
			servo.ChangeDutyCycle(7.5)		#Close the door -> Same for both sides
			print("Servo " + str(servo_num) + " set to 7.5")
		else:
			print("Error, I did not understand: " + cmd)

		time.sleep(0.5)
		GPIO.output(servo_num, 1)
		time.sleep(1)
		GPIO.output(servo_num, 0)
		
	elif(servo_num < 0):
		if(cmd[1] == "o" or cmd[1] == "O"):
			GPIO.output(HUMIDITY_PIN,1)		# Turn the humidity on
			print("Turning humidity on")
		elif(cmd[1] == "c" or cmd[1] == "C"):
			GPIO.output(HUMIDITY_PIN,0)					
			print("Turning humidity off")
	else:
		print("Error, I did not understand: " + cmd)


