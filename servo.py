__author__ = 'bhavinpatel'

import RPi.GPIO as gpio
import time
import random
from pprint import pprint


servo_pin = 15

gpio.setmode( gpio.BOARD )
gpio.setup( servo_pin , gpio.OUT)

def simple():
	gpio.output(servo_pin , 1)
	time.sleep(2)
	gpio.output(servo_pin , 0)

def pwm():
	s = gpio.PWM( servo_pin , 100)
	s.start(0)
	time.sleep(2)
	ms = 0.5

	for i in range( 1 , 10):
		j = 2.5 - ms
		dc = ( ms/10 )* 100
		s.ChangeDutyCycle(j)
		pprint(ms)
		pprint ( dc )
		pprint(j)
		time.sleep(1)
		ms +=0.1

	s.stop()

def cleanup():
	gpio.cleanup()

if __name__ == "__main__":
	pwm()
	simple()