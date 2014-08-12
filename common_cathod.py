
import RPi.GPIO as gpio
import time
import random
from pprint import pprint

red = 12
blue = 16
green = 18

gpio.setmode( gpio.BOARD )

gpio.setup( red , gpio.OUT)
gpio.setup( blue , gpio.OUT)
gpio.setup( green , gpio.OUT)


r = gpio.PWM( red , 100)
b = gpio.PWM( blue , 100)
b.start(0)
r.start(100)
time.sleep(1)
for dc in range( 0, 100 ) :
	adc = 100 - dc
	print "\n dc: (r:%d) (b:%d) " % (adc , dc)
	r.ChangeDutyCycle(adc)
	b.ChangeDutyCycle(dc)
	time.sleep(0.1)
r.stop()
gpio.cleanup()
