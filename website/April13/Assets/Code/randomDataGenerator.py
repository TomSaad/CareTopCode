import random as r
import time as t

while(1):
    print("Data Updated")

    file = open("../Data/data.js", 'w')

    file.write("var data = {\n")
    file.write("\t\"time\":\t\"{}\",\n\n".format(t.asctime()))
    for i in range(5):
        file.write("\t\"temp{}\":\t{},\n".format(i, r.randint(65, 85)))
        file.write("\t\"hum{}\":\t\t{},\n\n".format(i, r.randint(35, 55)))
        
    file.write("\t\"lit\":\t\t{}\n".format(r.randint(0,100)))
    
    file.write("}")

    file.close()

    t.sleep(10)