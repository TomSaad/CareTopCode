import time as t

while(1):
    
    json = open("../Data/config.json", 'r')
    js = open("../Data/config.js", 'w')
    
    js.write("var data = ")
    
    js.write(json.read())
    
    js.close()
    
    print("File Update Complete")
    
    t.sleep(10);