#Pre-loaded-pi-sd.com
#This program will toggle an LED.
import RPi.GPIO as io   
import time             

io.setwarnings(False)

io.setmode(io.BCM)  
                     
LEDs = (17,27)
for LED in LEDs:
    io.setup(LED,io.OUT)
    io.output(LED,0)

button = 4
io.setup(button,io.IN,pull_up_down=io.PUD_UP)

time_delay = 0.25

    
OF = 0

io.setup(LED, io.OUT)
io.output(LED, 0)

def toggle(channel):
    global OF
    for LED in LEDs:
        io.output(LED,0)
    if OF == 0:
        OF = 1
    else:
        OF = 0
    return OF

io.add_event_detect(button, io.FALLING, bouncetime = 300)
io.add_event_callback(button, toggle)

while True:
    global OF
    io.output(LEDs[OF],1)
    time.sleep(time_delay)
    io.output(LEDs[OF],0)
    time.sleep(time_delay)
    
    




