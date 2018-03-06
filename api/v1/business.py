from flask import jsonify
from user import User 
class Business():

	def __init__(self):
		self.businessname = None
		self.location = None
		self.description = None
		self.Business = {}

	def create_business(self,businessname,location,description):
		business = {'businessname':businessname,
					'location':location,
					'description':description
		}
		self.Business['business'] = business
		return business


			

				
