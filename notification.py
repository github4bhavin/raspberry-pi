__author__ = 'bhavin.patel'


import facebook
import pickle
from pprint import pprint

class fbNotification:

	oauth_access_token = ''
	notification_score = dict()

	def __init__(self):
		self.graph = facebook.GraphAPI( self.oauth_access_token )
		pprint ( self.oauth_access_token )

	def profile(self):
		self._profile = self.graph.get_object("me")
		return self._profile


	def friends(self):
		self.friends = self.graph.get_connections("me","friends")
		return self.friends

	def notifications(self ,include_read=False):
		self._notifications = self.graph.get_connections("me","notifications",
		                                                 fields=['application'],
		                                                 include_read=include_read)

		for notification in self._notifications['data']:

			if notification['application']['name']  not in self.notification_score :
				self.notification_score[notification['application']['name'] ] = 1
			else:
				self.notification_score[notification['application']['name'] ] += 1

		return self.notification_score

if __name__ == "__main__":

	me = fbNotification()
	pprint( me.notifications( True) )