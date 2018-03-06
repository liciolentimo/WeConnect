from flask import jsonify
from user import User,USERS 

businessdetails = [{
			'id': 1,
			'name':'tuskys',
			'location': 'nairobi',
			'category':'supermarket'

	},
			{
			'id':2,
			'name':'andela',
			'location':'nairobi',
			'category':'tech'

			}]


class Business():

	
	def __init__(self):
		self.businessname = None
		self.location = None
		self.category = None
	

	def create_business(self,businessname,location,category):
		business = {'id':business[-1]['id']+1,
					'businessname':businessname,
					'location':location,
					'category':category
		}
		businessdetails.append(business)
		# self.Business['business'] = business
		return business


			

				
