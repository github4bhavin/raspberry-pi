__author__ = 'bhavinpatel'
import RPi.GPIO as gpio
import time
import random
from pprint import pprint

gpio.setmode( gpio.BOARD )
gpio.setup( 13 , gpio.OUT )

pwm = gpio.PWM( 13 , 50 )
pwm.start(0)

try:
	while 1:
		pwm.ChangeDutyCycle(random.uniform(0,100))
		time.sleep(0.1)
		pwm.ChangeDutyCycle(random.uniform(100,0))
except KeyboardInterrupt:
	pass

pwm.stop()
gpio.cleanup()
