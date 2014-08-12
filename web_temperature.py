__author__ = 'bhavinpatel'
from flask import Flask
from flask import render_template
from flask import request

from ledPallet      import Pallet
import time
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route('/')
def temperature_slider():
    return render_template('index.html')

@app.route('/rest/temperature/<value>')
def rest_temperature_value(value):
	app.logger.info(value)
	r_led = round( (255 * int(value) )/ 90 )
	b_led = 255 - r_led
	g_led = 0
	p = Pallet()
	p.color( r_led , b_led, g_led)
	time.sleep(0.5)
	app.logger.info( r_led)
	return "updated successfully"



if __name__ == '__main__':
	app.debug = True
	app.run(host="192.168.1.16")