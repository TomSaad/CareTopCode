"""
	Required:
	I2C to read sensors
	Digital measurement of:
		1. humidity
		2. temperature
		3. UVB

	Add into some data structure (dictionary?)

	Serialize & send

	average humidity
	average temperature
	uvb reading
"""

def tankHumidity():
	"""
		Returns float of tank humidity in percent.
		Average of the values from the sensors in the tank.
	"""
	avgH = 0; # avg humidity
	for sVal in range(0, len(sensors[humidity])):
		avgH = avgH + sVal
	avgH = avgH / len(sensors[humidity])
	return avg

def tankTemperature():
	"""
		Returns float of tank temperature in Fahrenheit.
		Average of the values from the sensors in the tank.
	"""
	avgT = 0; # avg temperature
	for sVal in range(0, len(sensors[temperature])):
		avgT = avgT + sVal
	avgT = avgT / len(sensors[temperature])
	return avgT

def tankUVB():
	"""
		Returns float of <light metric?>.
		Only one UVB sensor; no average.
		Expandability: for future, if more light sensors, average like the others.
	"""
	return sensors[uvb]

