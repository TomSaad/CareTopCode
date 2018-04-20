import random as r
import time as t
import os

while(1):
    print("Data Updated")

    file = open("/var/www/html/Assets/Data/data.js", 'w')

    file.write("var data = {\n")
    file.write("\t\"created\":\t\"{}\",\n\n".format(t.asctime()))
    for i in range(5):
        file.write("\t\"temp{}\":\t{},\n".format(i, r.randint(65, 85)))
        file.write("\t\"hum{}\":\t\t{},\n\n".format(i, r.randint(35, 55)))

    file.write("\t\"lit\":\t\t{}\n".format(r.randint(0,100)))

    file.write("}")

    file.close()

    os.system("fswebcam -r 640x480 /var/www/html/Assets/Images/image.jpg")

    t.sleep(10)


