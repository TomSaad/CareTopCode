import time as t
import os
import json

while(1):
    print("Log Updated")

    file = open("/var/www/html/Assets/Data/log.html", 'a')
    data = open("/var/www/html/Assets/Data/data.js", 'r')
    data = data.read()[10:]
    data = json.loads(data)
    
    temp = (data["temp0"] + data["temp1"] + data["temp2"] + data["temp3"] + data["temp4"])/5
    hum = (data["hum0"] + data["hum1"] + data["hum2"] + data["hum3"] + data["hum4"])/5
    light = data["lit"]

    file.write("<p>Log {} --- Temp|{} --- Hum|{} --- Light|{}</p>\n".format(t.asctime(), temp, hum, light))

    file.close()

    os.system("fswebcam -r 640x480 /var/www/html/Assets/Images/image.jpg")

    t.sleep(10)



