#single line to fresh
import time
for i in range(101):
    print("\r{:3}%".format(i),end=" ")
    time.sleep(0.1)

#\r mekes cursor back to head 
