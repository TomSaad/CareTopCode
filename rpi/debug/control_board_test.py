#Title: control_board.py
#Date: March 24, 2018
#Contributors: David St-Pierre stpied@rpi.edu
#Description:
#	Testout the leds on the control board.....and have some fun with it

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

PIN_1 = 2
PIN_2 = 3
PIN_3 = 4
PIN_4 = 17
PIN_5 = 27

GPIO.setup(PIN_1, GPIO.OUT)
GPIO.setup(PIN_2, GPIO.OUT)
GPIO.setup(PIN_3, GPIO.OUT)
GPIO.setup(PIN_4, GPIO.OUT)
GPIO.setup(PIN_5, GPIO.OUT)

GPIO.output(PIN_1, 0)
GPIO.output(PIN_2, 0)
GPIO.output(PIN_3, 0)
GPIO.output(PIN_4, 0)
GPIO.output(PIN_5, 0)

#My simple and friendly functions :)
def on(pin):
	GPIO.output(pin, 1)
def off(pin):
	GPIO.output(pin, 0)
def all_off():
	off(PIN_1)
	off(PIN_2)
	off(PIN_3)
	off(PIN_4)
	off(PIN_5)
def all_on():
	on(PIN_1)
	on(PIN_2)
	on(PIN_3)
	on(PIN_4)
	on(PIN_5)
def say(words):
	espeak.synth(words)
#-----------------
#Pattern Thyme!!!!
#-----------------

#Simple blink
for x in range(0,5):
	on(PIN_1)
	time.sleep(0.2)
	off(PIN_1)
	time.sleep(0.2)

#LETS ALL BLINK!!!
all_off()
all_on()
time.sleep(0.3)
all_off()
time.sleep(0.3)
all_on()
time.sleep(0.3)
all_off()
time.sleep(0.3)
all_on()
time.sleep(0.3)
all_off()
time.sleep(0.3)

#Go in a row!
on(PIN_1)
time.sleep(0.2)
off(PIN_1)
on(PIN_2)
time.sleep(0.2)
off(PIN_2)
on(PIN_3)
time.sleep(0.2)
off(PIN_3)
on(PIN_4)
time.sleep(0.2)
off(PIN_4)
on(PIN_5)
time.sleep(0.2)
off(PIN_5)
on(PIN_4)
time.sleep(0.2)
off(PIN_4)
on(PIN_3)
time.sleep(0.2)
off(PIN_3)
on(PIN_2)
time.sleep(0.2)
off(PIN_2)
on(PIN_1)

all_off

#I call this worm
on(PIN_1)
time.sleep(0.2)
on(PIN_2)
time.sleep(0.2)
on(PIN_3)
time.sleep(0.2)
on(PIN_4)
time.sleep(0.2)
on(PIN_5)
time.sleep(0.2)
off(PIN_5)
time.sleep(0.2)
off(PIN_4)
time.sleep(0.2)
off(PIN_3)
time.sleep(0.2)
off(PIN_2)
time.sleep(0.2)
off(PIN_1)
time.sleep(0.2)

#Inverting pairs
for x in range(0,3):
	on(PIN_1)
	on(PIN_3)
	on(PIN_5)
	off(PIN_2)
	off(PIN_4)
	time.sleep(1)
	off(PIN_1)
	off(PIN_3)
	off(PIN_5)
	on(PIN_2)
	on(PIN_4)
	time.sleep(1)


#-----------------------------------
# Clean up after yourself (all off)
#-----------------------------------

all_off()
