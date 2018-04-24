import time
import sys

print str(sys.argv)

print (str(sys.argv[0]))
hum = sys.argv[1]
temp = sys.argv[2]
for x in range(0,100):
	print("  ")

file = open('sensors.txt', 'r')
lines = file.readlines()


cnt = 0

while(True):
	data = lines[cnt]
	data = data.split(",")
	humidity = data[0]
	temperature = str(data[1]).rstrip()
	print("           ")
	print("-----------")
	print("Sensor data")
	print("-----------")
	new_hum = int(humidity) + int(hum)
	new_temp = int(temperature) + int(temp)
	print("Average Temperature = " + str(new_temp) + "  Average Humidity = " + str(new_hum))
	cnt = cnt + 1
	time.sleep(10)
