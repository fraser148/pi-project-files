#Pre-loaded-pi-sd.com
#This program switches on an LED for 0.5 seconds when a button is pulled to ground(0V)
import RPi.GPIO as io   
import time             


io.setmode(io.BCM)  
                   

button_pin = 4     
LED = 17            

io.setup(button_pin, io.IN, pull_up_down=io.PUD_UP)
io.setup(LED, io.OUT)

io.output(LED, 1)

while True:
    input_state = io.input(button_pin)
    if input_state == False:
        io.output(LED,1)
        print('Button Pressed')
        time.sleep(0.5)
        io.output(LED,0)
