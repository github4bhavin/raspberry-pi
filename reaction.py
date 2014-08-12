__author__ = 'bhavinpatel'

import RPi.GPIO as g
import time
import random

g.setmode(g.BOARD)

led = 23

g.setup ( led , g.OUT)

g.output ( led , 1 )

time.sleep(random.uniform(5,10))

g.output( led , 0 )

g.cleanup()
