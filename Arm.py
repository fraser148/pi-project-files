
from __future__ import division
import cwiid
import RPi.GPIO as io
import os
import commands
import time
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
servo_min = 150
servo_max = 600
button_delay = 0.1

no1= 375
no2 = 375
no3 = 375
no4 = 375
no4_ = 375
no5 = 375
no5_ = 375
t = 0.005
p = 1
CO = 8
CC = 7


io.setwarnings(False)
io.setmode(io.BCM)


io.setup(CO,io.OUT)
io.setup(CC,io.OUT)

io.output(CC,0)
io.output(CO,0)


print ("Press 1 + 2 on your Wii Remote now ...")
time.sleep(1)

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print ("Error opening wiimote connection")
  quit()

print ('Wii Remote connected...\n')
print ('Press some buttons!\n')
print ('Press PLUS and MINUS together to disconnect and quit.\n')

wii.rpt_mode = cwiid.RPT_BTN

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
for i in range(0,5):
    pwm.set_pwm(i, 0, 375)
    time.sleep(0.05)

while True:

  buttons = wii.state['buttons']

  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print ('\nClosing connection ...')
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)

  if (buttons & cwiid.BTN_UP):
      if no4 > 150:
            no4 = no4 - p
            no4_ = no4_ + p
            pwm.set_pwm(2, 0, no4)
            pwm.set_pwm(3, 0, no4_)
            time.sleep(t)
      else:
              print("Limit")
              time.sleep(t)         

  if (buttons & cwiid.BTN_DOWN):
        if no4 < 600:
            no4 = no4 + p
            no4_ = no4_ - p
            pwm.set_pwm(2, 0, no4)
            pwm.set_pwm(3, 0, no4_)
            time.sleep(t)
        else:
            print("Limit")
            time.sleep(t)           

  if (buttons & cwiid.BTN_RIGHT):
        if no1 > 150:
            no1 = no1 - p 
            pwm.set_pwm(0, 0, no1)
            time.sleep(t)
        else:
              print("Limit")
              time.sleep(t)   

  if (buttons & cwiid.BTN_LEFT):
        if no1 < 600:
            no1 = no1 + p
            pwm.set_pwm(0, 0, no1)
            time.sleep(t)
        else:
            print("Limit")
            time.sleep(t)          


  if (buttons & cwiid.BTN_A):
        print("3")
        io.output(CO, 1)
        time.sleep(0.1)
        io.output(CO, 0)
		
		
  if (buttons & cwiid.BTN_B):
        print("4")
        io.output(CC, 1)
        time.sleep(0.1)
        io.output(CC, 0)

            
  if (buttons & cwiid.BTN_MINUS):
          if no5 < 600:
            no5 = no5 + p
            no5_ = no5_ - p
            pwm.set_pwm(4, 0, no5)
            pwm.set_pwm(1, 0, no5_)
            time.sleep(t)
          else:
            print("Limit")
            time.sleep(t) 
        

  if (buttons & cwiid.BTN_PLUS):
        if no5 > 150:
            no5 = no5 - p
            no5_ = no5_ + p
            pwm.set_pwm(4, 0, no5)
            pwm.set_pwm(1, 0, no5_)
            time.sleep(t)
        else:
              print("Limit")
              time.sleep(t)
