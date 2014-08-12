__author__ = 'bhavinpatel'

import RPi.GPIO as g
import time
import random


class Diode:

	def __init__(self , red = 12 , blue = 18 , green =16):
		self.red = red
		self.blue = blue
		self.green = green
		self.defaultSleep = 1

		g.setmode( g.BOARD )
		g.setup( self.red , g.OUT )
		g.setup( self.blue , g.OUT )
		g.setup ( self.green , g.OUT )

	def sleep(self , sleepTime = 1):
		time.sleep(sleepTime )

	def redLed(self , status=1) :
		print "\n red %d" % status
		g.output ( self.red , status )
		self.sleep()

	def blueLed( self , status=0):
		print "\n blue %d " % status
		g.output( self.blue, status )
		self.sleep()

	def greenLed(self, status=0):
		print "\n green %d " % status
		g.output( self.green , status)
		self.sleep()

	def off( self):
		g.output( self.red , 0)
		g.output( self.blue , 0)
		g.output( self.green , 0)


	def __def__(self):
		g.cleanup()

if __name__ == "__main__":
	d = Diode()
	d.redLed(True)
	d.redLed(False)

	d.blueLed(True)
	d.blueLed(False)

	d.greenLed(True)
	d.greenLed(False)


	d.redLed(True)
	d.blueLed(True)

	d.off()