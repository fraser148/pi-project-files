#Pre-loaded-pi-sd.com
#This program will flash an LED 10 times making use of a for loop
import RPi.GPIO as io   
import time             

io.setwarnings(False)

io.setmode(io.BCM)  
                     
LED = 17

io.setup(LED, io.OUT)
io.output(LED, 1)

for x in range (0,10):
    print(x)
    io.output(LED,1)
    time.sleep(0.25)
    io.output(LED,0)
    time.sleep(0.25)

