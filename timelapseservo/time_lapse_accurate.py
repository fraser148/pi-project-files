import RPi.GPIO as io
import os
import commands
import time
import Adafruit_PCA9685


io.setmode(io.BCM)
io.setwarnings(False)

#initialising some variables
pwm = Adafruit_PCA9685.PCA9685()
servo_min = 150
servo_max = 600
y = 0
servo_channel = 0

#initialise servo
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)
pwm.set_pwm(servo_channel, 0, 150)

#Input Values for time lapse
length = int(raw_input("How long would you like the time lapse to be in seconds? >>> "))
width = int(raw_input("Time betweem frames? (Must be >= 2) >>> "))
while width < 2:
    width = int(raw_input("Invalid. Time betweem frames? (Must be >= 2) >>> "))
directory = raw_input("Name the folder that you would like to make and save the time lapse to >>> ")

#convert to ms and to string for command line
length = length * 1000
length = str(length)
width = width * 1000
width = str(width)

#prints to verify
print(length)
print(width)
print("will insert this command:")
print("raspistill -o /home/pi/" + directory + "/filenum.jpg")
print("Starting...")

#makes the directory for the time lapse images to be saved to
os.system("mkdir /home/pi/" + directory)

#converts the times back to seconds and prints to verify
fileNumber = 1
width = int(width)/1000
length = int(length)/1000
print(length)
print(width)

#some maths
sqr = 90**(1./3)
filenum = "%04d" % (fileNumber)

#time lapse loop which will put main focus of video at 90 degrees as it pans.
#we use a cubic to do this.
for x in range(0,(length+1),width):
    filenum = "%04d" % (fileNumber)
    y = 2 * sqr
    y = y / length
    y = (y * x -sqr) ** 3
    y = y + 90
    print(y)        #prints the angle of the camera 
    y = (y/180) * 420 + servo_min + 15      #converts to number suited to the pwm.set_pwm() function which ranges from 165 to 585 in our case.
    round(y,0)
    pwm.set_pwm(servo_channel, 0, int(y))
    os.system("raspistill -o /home/pi/" + directory + "/" + str(filenum) + ".jpg -t 2000")
    time.sleep(width-2)
    fileNumber += 1

print("Time lapse finished and saved to /home/pi/" + directory)
