import os
import time 



for i in range(100):
    
        ip = "208.15.1.%d" % (i)
        print ip
        os.system("nc -n -z -v " +ip + " 445") 
        print "scanning:", ip
        time.sleep(4)

print "scanning complete!"        




