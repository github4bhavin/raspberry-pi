#__author__ = 'bhavinpatel'
import RPi.GPIO as g
import time
import random
from pprint import pprint

class Diode:

	def __init__(self , red=12,blue=18,green=16):

		self.red   = red
		self.blue  = blue
		self.green = green
		self.g     = g
		try:
			self.g.setmode( g.BOARD)
			self.g.setup( self.red   , g.OUT)
			self.g.setup( self.blue  , g.OUT)
			self.g.setup( self.green , g.OUT)
		except:
			pass


	def redLed(self, status ):
		self.g.output( self.red , status)
		time.sleep(status)

	def cleanUp(self):
		self.g.cleanup()

	def __del__(self):
		self.g.cleanup()

class Pallet(Diode):

	initialFrequency = 100
	initialDutyCycle = 0

	def __init( self , red , blue , green ):
		self = Diode.__init__(self, red, blue , green)
		self.RED   = self.g.PWM( self.red   , self.initialFrequency)
		self.BLUE  = self.g.PWM( self.blue  , self.initialFrequency)
		self.GREEN = self.g.PWM( self.green , self.initialFrequency)

		self.RED.start(   self.initialDutyCycle )
		self.BLUE.start(  self.initialDutyCycle )
		self.GREEN.start( self.initialDutyCycle )

	def set_pwm_for_red(self):
		self.RED = self.g.PWM( self.red , self.initialFrequency)
		self.RED.start( self.initialDutyCycle )

	def set_pwm_for_blue(self):
		self.BLUE = self.g.PWM( self.blue , self.initialFrequency)
		self.BLUE.start( self.initialDutyCycle )

	def set_pwm_for_green(self):
		self.GREEN = self.g.PWM( self.green , self.initialFrequency)
		self.GREEN.start( self.initialDutyCycle )

	def mapping(self, val):
		retval = round((100*val)/255,1)
		pprint( retval )
		return retval

	def color (self , r, b, g ):
		if( not hasattr(self,'RED') ) :
			self.set_pwm_for_red()

		if( not hasattr(self,'BLUE') ) :
			self.set_pwm_for_blue()

		if( not hasattr(self,'GREEN') ) :
			self.set_pwm_for_green()

		self.RED.ChangeDutyCycle(   self.mapping( r ) )
		self.BLUE.ChangeDutyCycle(  self.mapping( b ) )
		self.GREEN.ChangeDutyCycle( self.mapping( g ) )

	def wait(self ,waitPeriod=1):
		time.sleep( waitPeriod)

if __name__ == "__main__":
	p = Pallet()

	p.redLed(True)
	p.color(255,0,255)
	p.wait(10)