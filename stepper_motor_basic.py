#Projects4Pi.com
#Import libraries
import time
import RPi.GPIO as io

io.setwarnings(False)

#Declare output pins

io.setmode(io.BCM)
out1 = 4
out2 = 17
out3 = 27
out4 = 22
outputs = (out1,out2,out3,out4)

time_delay = 0.005

#Setup outputs

for out in outputs:
    io.setup(out,io.OUT)
    io.output(out,0)

#Define each step using sub-procedures

def step1():
    io.output(out1,0)
    io.output(out2,1)
    io.output(out3,1)
    io.output(out4,0)
    time.sleep(time_delay)

def step2():
    io.output(out1,0)
    io.output(out2,1)
    io.output(out3,0)
    io.output(out4,1)
    time.sleep(time_delay)

def step3():
    io.output(out1,1)
    io.output(out2,0)
    io.output(out3,0)
    io.output(out4,1)
    time.sleep(time_delay)

def step4():
    io.output(out1,1)
    io.output(out2,0)
    io.output(out3,1)
    io.output(out4,0)
    time.sleep(time_delay)

def stopMotor():
    io.output(out1,0)
    io.output(out2,0)
    io.output(out3,0)
    io.output(out4,0)

#Use try to avoid errors

try:
    while True:                     #Repeat this process over and over
        for x in range(0,50):       #Repeats sequence of steps 50 times
            step1()
            step2()
            step3()
            step4()

        stopMotor()                 #Stop the motor
        time.sleep(2)               #Delay

        for x in range(0,50):       #Repeats sequence of steps 50 times
            step3()
            step2()
            step1()
            step4()

        stopMotor()                 #Stop the motor
        time.sleep(2)               #Delay

except KeyboardInterrupt:           #Upon pressing Ctrl + c the program will stop.
    stopMotor()
    print("Stopping...")
    

    

    

    

    
