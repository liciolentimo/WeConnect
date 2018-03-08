from flask import jsonify,make_response
from user import User

businessdetails = [{
			'id': 1,
			'name':'tuskys',
			'location': 'nairobi',
			'category':'supermarket',
			# 'createdby':'john@email.com'

	},
			{
			'id':2,
			'name':'andela',
			'location':'nairobi',
			'category':'tech',
			# 'createdby':'mike@email.com'

			}]


class Business():

	
	def __init__(self):
		# self.businessname = None
		# self.location = None
		# self.category = None
		self.list_business = []
	

	def create_business(self,businessname,location,category):
		business = {'id':len(businessdetails)+1,
					'businessname':businessname,
					'location':location,
					'category':category
					# 'created_by':email
		}
		businessdetails.append(business)
		# self.Business['business'] = business
		return business

	def list_business(self):
		return businessdetails	

	def update_business(self,businessname,location,category):
		business1 = {
					'businessname':tuskys,
					'location':nairobi,
					'category':supermarket
		}
		business2 = {
					'businessname':tuskys,
					'location':nakuru,
					'category':supermarket
		}
		business1.update(business2)
		return make_response(jsonify({'message':'successfully updated'}))

	# def delete_business(self,id):
			
			


			

				
