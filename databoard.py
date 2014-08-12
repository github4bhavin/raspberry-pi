__author__ = 'bhavinpatel'

from ledPallet      import Pallet
from weatherData    import WeatherData
from fbNotification import fbNotification
from pprint         import pprint
from led            import LED
import time

class DataBoard:

	temperature = dict()
	defaultWait = 5

	def __init__(self):
		self.weatherDataObj    = WeatherData()
		self.palletObj         = Pallet()
		self.fbNotificationObj = fbNotification()
		self.fb_led            = LED(22)

	def show_temperature(self, temperature = None):

		self.weatherDataObj.get_weather()
		if temperature is not None:
			print "\n Temperature : %f" % temperature
		else:
			print "\n Temperature : %f" % self.weatherDataObj.weather['temperature']

		self.__temperature_gradient(temperature)
		self.palletObj.color( self.temperature['led']['r'],
		                      self.temperature['led']['g'],
		                      self.temperature['led']['b'])
		time.sleep( self.defaultWait )


	def __temperature_gradient(self, temperature=None):
		leds = dict()
		if temperature is None:
			leds['r'] = self.__calculate_temperature_gradient( self.weatherDataObj.weather['temperature'] )
		else:
			leds['r'] = temperature
		leds['b'] = 255 - leds['r']
		leds['g'] = 0
		self.temperature['led'] = leds

	def __calculate_temperature_gradient(self, temperature):
		return round( (255 * temperature )/ 90 )

	def fb_notification(self):
		fb_notifications = self.fbNotificationObj.notifications(True)
		if len( fb_notifications ) :
			self.fb_led.pulse()

if __name__ == "__main__":
	db = DataBoard()
	db.fb_notification()

	db.show_temperature()
	db.show_temperature(10)
