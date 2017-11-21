#Pre-loaded-pi-sd.com
#This program will make use of integer user inputs
import RPi.GPIO as io   
import time             

io.setwarnings(False)

io.setmode(io.BCM)  
                     
LEDs = (17,27)
for LED in LEDs:
    io.setup(LED,io.OUT)
    io.output(LED,0)



print("Which LED would you like on? /n")
print("1: Green")
print("2: Red")

LED_choice = input("Choice:  ")


LED_choice -= 1
io.output(LEDs[LED_choice],1)
