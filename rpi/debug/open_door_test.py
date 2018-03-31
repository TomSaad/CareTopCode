import RPi.GPIO as GPIO
import time

#Use the actual numbers on the board not the BCM numbers
GPIO.setmode(GPIO.BCM)

SERVO_PIN = 18
POWER_PIN = 2

#Set pin SERVO_PIN as output
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(POWER_PIN, GPIO.OUT, initial = 0)

#Set the servo on pin SERVO_PIN and initialize the PWM
servo = GPIO.PWM(SERVO_PIN, 50)

#Servo pulse mapping: 2.5 - 12.5

servo.start(7.5)
time.sleep(2)

try:
	while True:
		#Move servo
		GPIO.output(POWER_PIN,1)
		time.sleep(1)
		servo.ChangeDutyCycle(4.5)
		time.sleep(1)
		GPIO.output(POWER_PIN,0)
		time.sleep(1)
		#GPIO.output(POWER_PIN,1)
		time.sleep(1)
		servo.ChangeDutyCycle(7.5)
		time.sleep(1)
		GPIO.output(POWER_PIN,0)
		time.sleep(1)
		GPIO.output(POWER_PIN,1)
		time.sleep(1)
		servo.ChangeDutyCycle(10.5)
		time.sleep(1)
		GPIO.output(POWER_PIN,0)
		time.sleep(1)
		GPIO.output(POWER_PIN,1)
		time.sleep(1)
		servo.ChangeDutyCycle(7.5)
		time.sleep(1)
		GPIO.output(POWER_PIN,0)
		time.sleep(1)

		
except KeyboardInterrupt:
	servo.stop()
	GPIO.cleanup()
