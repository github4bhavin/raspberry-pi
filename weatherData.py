__author__ = 'bhavin.patel'
import urllib2
import json
from pprint import pprint

class WeatherData:

	api_url = "http://api.wunderground.com/api/"
	api_key = 'fe39ecfd47ccfbc0'
	weather = dict()

	def get_weather(self):

		self.__get_current_conditions()

		wind = dict()
		wind['degree'   ] = self.current_conditions['current_observation']['wind_degrees']
		wind['direction'] = self.current_conditions['current_observation']['wind_dir'    ]
		wind['speed'    ] = self.current_conditions['current_observation']['wind_mph'    ]

		self.weather['uv_index'   ] = self.current_conditions['current_observation']['UV'    ]
		self.weather['temperature'] = self.current_conditions['current_observation']['temp_f']
		self.weather['wind'       ] = wind

		return self.weather

	def __get_current_conditions(self):
		try:
			response = urllib2.urlopen(
				'/'.join([ self.api_url,
							self.api_key,
							'conditions',
							'q',
							'NY',
							'Yonkers.json']))
			self.current_conditions = json.loads( response.read() )
			return self.current_conditions
		except URLError ,e:
			pprint(e)
		except HTTPError ,e:
			pprint(e)

if __name__ == "__main__":
	wd = WeatherData()
	pprint( wd.get_weather() )