import RPi.GPIO as io
import time
import os

io.setmode(io.BCM)
io.setup(4,io.OUT)

#initialising some variables
y=0
p = io.PWM(4,50)
p.start(2.5)

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
print("raspistill -t " + length + " -tl " + width + " -o /home/pi/" + directory + "/image%04d.jpg")

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
    y = 2*sqr
    y=y/length
    y=(y*x -sqr)**3
    y=y+90
    print(y)        #prints the angle of the camera 
    y = y/18 + 2.5  #converts to number suited to the ChangeDutyCycle() function which ranges from 2.5 to 12.5
    p.ChangeDutyCycle(y)
    os.system("raspistill -o /home/pi/" + directory + "/" + str(filenum) + ".jpg -t 2000")
    time.sleep(width-2)
    fileNumber += 1

print("Time lapse finished and saved to /home/pi/" + directory)



