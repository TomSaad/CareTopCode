# deal with gpio here; need 5 sensor lines, power ground can be shared.

import sys
import RPi.GPIO as GPIO
import Adafruit_DHT
import smbus
import time

###GPIO SETUP
GPIO.setwarnings(False)

#Use the BCM numbers not the direct pin numbers
GPIO.setmode(GPIO.BCM)

# Assigned pins going down left side of breakout
HUMTMP_0_PIN = 4
HUMTMP_1_PIN = 17
HUMTMP_2_PIN = 27
HUMTMP_3_PIN = 22
HUMTMP_4_PIN = 5

#I2C setup
bus = smbus.SMBus(1)
UVB_I2C_ADDR = 0x10

GPIO.setup(UVB_I2C_ADDR, GPIO.OUT)
GPIO.setup(HUMTMP_0_PIN, GPIO.OUT)
GPIO.setup(HUMTMP_1_PIN, GPIO.OUT)
GPIO.setup(HUMTMP_2_PIN, GPIO.OUT)
GPIO.setup(HUMTMP_3_PIN, GPIO.OUT)
GPIO.setup(HUMTMP_4_PIN, GPIO.OUT)

def read(pin):
    return Adafruit_DHT.read_retry(11, pin)
    """
        takes in pin for sensor desired to read
        returns tuple of (humidity, temperature), using DHT library read function
        read_retry from DHT library attempts to
        read until valid tuple of (humidity, temperature) is returned.
        if failed to do so in certain number of tries or time, returns (None, None).
        read_retry arguments:
        read_retry(sensor, pin, retries=15, delay_seconds=2, platform=None)
        we use DHT11, so sensor is always 11
    """

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

def readUVB(addr):
	"""
		takes pin for uvb sensor to read
		uvb uses i2c protocol
	"""
        return bus.read_byte_data(addr, 0)

def readAll(htsensors, uvsensors, humtemp, uvb):
    for hts in range(0, len(htsensors)):
        humtemp[hts] = read(htsensors[hts])  # pass in pin of sensor
    """
    for uvbs in range(len(uvsensors)):
        uvb[uvbs] = readUVB(uvsensors[uvbs])  # pass in i2c address of sensor
    """

def avgHum(htsensors, uvsensors, humtemp, uvb):
    readAll(htsensors, uvsensors, humtemp, uvb)
    avg = 0
    for value in range(len(humtemp)):
        avg = avg + humtemp[value][0] #just humidity here
    return avg/len(humtemp)

def avgTemp(htsensors, uvsensors, humtemp, uvb):
    readAll(htsensors, uvsensors, humtemp, uvb)
    avg = 0
    for value in range(len(humtemp)):
        avg = avg + humtemp[value][1] #just temperature here
    return avg/len(humtemp)

def main():
	htsensors = [
            HUMTMP_0_PIN
			, HUMTMP_1_PIN
			, HUMTMP_2_PIN
			, HUMTMP_3_PIN
			, HUMTMP_4_PIN
            ]
	humtemp = [] * len(htsensors)

	uvsensors = [UVB_I2C_ADDR]
	uvb = [] * len(uvsensors)

	while True:

		hum0, temp0 = read(HUMTMP_0_PIN)
		hum1, temp1 = read(HUMTMP_1_PIN)
		hum2, temp2 = read(HUMTMP_2_PIN)
		hum3, temp3 = read(HUMTMP_3_PIN)
		#hum4, temp4 = read(HUMTMP_4_PIN)
		hum4 = readHumidity(HUMTMP_4_PIN)
		temp4 = readTemperature(HUMTMP_4_PIN)

        if (hum0 > 100):
            humtemp[0] = (humtemp[0][0], temp0)
        else:
            humtemp[0] = (hum0, temp0)

        if (hum1 > 100):
            humtemp[1] = (humtemp[1][0], temp1)
        else:
            humtemp[1] = (hum1, temp1)

        if (hum2 > 100):
            humtemp[2] = (humtemp[2][0], temp2)
        else:
            humtemp[2] = (hum2, temp2)

        if (hum3 > 100):
            humtemp[3] = (humtemp[3][0], temp3)
        else:
            humtemp[3] = (hum3, temp3)

        if (hum0 > 100):
            humtemp[4] = (humtemp[4][0], temp4)
        else:
            humtemp[4] = (hum4, temp4)

        file = open("/var/wwww/html/Assets/Data/data.js", 'w')
        file.write("var data = {\n")
        file.write("\t\"created\":\t\"{}\",\n\n".format(time.asctime()))
        for i in range(5):
            file.write("\t\"temp{}\":\t{},\n".format(i, htsensors[i][1]))
            file.write("\t\"hum{}\":\t\t{},\n\n".format(i, htsensors[i][0]))
        file.write("\t\"lit\":\t\t{}\n".format(r.randint(0,100)))
        file.write("}")
        file.close()
		
        print(""
            + "\n h1= {0:0.1f} %  t1= {1:0.1f} C"
            + "\t h2= {2:0.1f} %  t2= {3:0.1f} C"
            + "\t h3= {4:0.1f} %  t3= {5:0.1f} C"
            + "\t h4= {6:0.1f} %  t4= {7:0.1f} C"
            + "\t h5= {8:0.1f} %  t5= {9:0.1f} C"
            + "").format(
                float(hum0), float(temp0)
                , float(hum1), float(temp1)
                , float(hum2), float(temp2)
                , float(hum3), float(temp3)
                , float(hum4), float(temp4)
                )

if __name__ == "__main__":
	main()
