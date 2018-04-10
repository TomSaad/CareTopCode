# deal with gpio here; need 5 sensor lines, power ground can be shared.

import sys
import RPi.GPIO as GPIO
#import Adafruit_Python_DHT/Adafruit_DHT
#import Adafruit_DHT
import sys.path.append('Adafruit_Python_DHT/Adafruit_DHT')

###GPIO SETUP
GPIO.setwarnings(False)

#Use the BCM numbers not the direct pin numbers
GPIO.setmode(GPIO.BCM)

# Assigned just going down left side
# random pins and random comment
UVB_1_PIN = 4
HUMTMP_1_PIN = 17
HUMTMP_2_PIN = 27
HUMTMP_3_PIN = 22
HUMTMP_4_PIN = 5
HUMTMP_5_PIN = 6

GPIO.setup(UVB_1_PIN, GPIO.OUT)
GPIO.setup(HUMTMP_1_PIN, GPIO.OUT)
GPIO.setup(HUMTMP_2_PIN, GPIO.OUT)
GPIO.setup(HUMTMP_3_PIN, GPIO.OUT)
GPIO.setup(HUMTMP_4_PIN, GPIO.OUT)
GPIO.setup(HUMTMP_5_PIN, GPIO.OUT)

uvsensors = [UVB_1_PIN]
uvb = [] * len(uvsensors)

htsensors = [HUMTMP_1_PIN, HUMTMP_2_PIN, HUMTMP_3_PIN, HUMTMP_4_PIN, HUMTMP_5_PIN]
humtemp = [] * len(htsensors)


def read(pin):
    """
        takes in pin for sensor desired to read
        returns tuple of (humidity, temperature), using DHT library read function
    """
    # read_retry from DHT library attempts to read until valid tuple of (humidity, temperature) is returned.
    # if failed to do so in certain number of tries or time, returns (None, None).
    # read_retry arguments:
    # read_retry(sensor, pin, retries=15, delay_seconds=2, platform=None)
    # we use DHT11, so sensor is always 11
    return Adafruit_DHT.read_retry(11, pin)

def readHumidity(pin):
    """
        takes in pin for sensor desired to read
        returns humidity value (first of tuple (humidity, temperature))
    """
    return Adafruit_DHT.read_retry(11, pin)[0]

def readTemperature(pin):
    """
        takes in pin for sensor desired to read
        returns temperature value (second of tuple (humidity, temperature))
    """
    return Adafruit_DHT.read_retry(11, pin)[1]

def readAll():
    for uvb_sensor in range(1, len(uvsensors)):
        uvb[uvb_sensor] = readUVB(uvsensors[uvb_sensor])  # pass in pin of sensor

    for ht_sensor in range(1, len(htsensors)):
        humtemp[ht_sensor] = read(htsensors[ht_sensor])  # pass in pin of sensor

def main():
    while True:
        hum, temp = read(4)
        #print "humidity: {0:0.1f} % \ttemperature: {1:0.1f} C".format(hum, temp)
        # python 2.7 syntax
        print("humidity: {0:0.1f} % \ttemperature: {1:0.1f} C", hum, temp)
        # python 3.6 syntax

if __name__ == "__main__":
    main()
