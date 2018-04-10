#Title "read_json_test.py
#Contributor: David St-Pierre -> stpied@rpi.edu
#Date: April 10, 2018
#Description
#	Test code to read a json file and spit it back to the console
import json

def main():
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

	print(created)
	print(start)
	print(running)
	print(dTemp)
	print(dHum)
	print(feeding1)
	print(feeding2)
	print(feeding3)
	print(feeding4)
	print(feeding5)
	print(feeding6)
	print(feeding7)
	print(feeding8)
	print(feeding9)
	print(feeding10)

try:
	main()
except KeyboardInterrupt:
	print("Program exited manually by user")
