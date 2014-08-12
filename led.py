__author__ = 'bhavinpatel'
import RPi.GPIO as GPIO
import time
import random

class LED:

	def __init__( self, led ):
		self.led = led
		GPIO.setmode( GPIO.BOARD )
		GPIO.setup(led , GPIO.OUT )

	def turnOn(self):
		GPIO.output( self.led , 1 )

	def turnOff(self):
		GPIO.output ( self.led , 0 )

	def pulse ( self ):
		self.L = GPIO.PWM( self.led , 100)
		self.L.start(0)
		for dc in range( 0 , 10):
			self.L.ChangeDutyCycle(random.uniform(0,100))
			time.sleep(0.5)

