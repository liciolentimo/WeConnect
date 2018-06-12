from flask import jsonify
from user import User
import re
# businessdetails = [{
# 			'id': 1,
# 			'name':'tuskys',
# 			'location': 'nairobi',
# 			'category':'supermarket',
# 			# 'createdby':'john@email.com'

# 	},
# 			{
# 			'id':2,
# 			'name':'andela',
# 			'location':'nairobi',
# 			'category':'tech',
# 			# 'createdby':'mike@email.com'

# 			}]


class Business():

	
	def __init__(self):
		# self.businessname = None
		# self.location = None
		# self.category = None
		self.list_business = []
	

	def create_business(self,businessname,location,category):
		businessinfo = {}
		#
		# }
		if re.match("^[a-zA-Z0-9 _]*$", businessname):
			# biz = self.get_creator(user)
			businessdict = {
							'name':businessname,
							# 'user':user,
							'category':category,
							'location':location }
			self.list_business.append(businessdict),'business created successfully'
		else:
			return "No special characters"
		

	def list_allbusiness():
		business = [i for i in Business.list_business]

		return allbusiness

	def get_business_by_name(self,businessname):
		for business in self.list_business:
			if business['name'] == businessname:
				return business
		else:
			return False	

	def get_creator(self,user):
		businessuser  = [i for i in self.list_business if i['user'] == user]		

			

	# def update_business(self,businessname,location,category):
		

	# def delete_business(self,id):
			
			


			

				
