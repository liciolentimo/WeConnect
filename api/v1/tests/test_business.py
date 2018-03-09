import unittest
from app import app
from business import Business
from user import User
import json

class BusinessTest(unittest.TestCase):
	def setUp(self):
		self.business = Business()
		self.app = app.test_client()
		# self.businesscreds = {
		# 			'id': 1,
		# 			'name':'tuskys',
		# 			'location':'nairobi',
		# 			'category':'supermarket'
		# 			# 'createdby':'john@email.com'
		# }

	def test_register_business(self):
		response = self.app.post(
								'/api/v1/addbusiness',
								# data=json.dumps(self.businesscreds),
								headers={'Content-Type':'application/json'})
		self.assertEqual(response.status_code,201)
		self.assertIn('business created successfully', str(response.data))	



	def test_list_business(self):
		response = self.app.post(
								'/api/v1/business',
								# data=json.dumps(self.businesscreds),
								headers={'Content-Type':'application/json'})
		response = self.app.get('/api/v1/business')

		self.business.list_business = [{'createdby':'john@email.com','name':'biz','location':'nairobi','category':'tech'}]
		result = self.business.list_business
		value = self.business.list_allbusiness()
		self.assertEqual(result,value)
		# self.assertEqual(response.status_code,200)	

	def test_add_empty_business_name(self):
		response = self.app.post(
								'api/v1/addbusiness',
								data=dict(name="",location="nairobi",category="tech"))
		self.assertEqual(response.status_code,401)
		message = json.loads(response.data.decode("UTF-8"))	
		self.assertIn("Business name cannot be empty",message['message'])	

	def test_created_by(self):
		response = self.app.post(
								'/api/v1/business',
								# data=json.dumps(self.businesscreds),
								headers={'Content-Type':'application/json'})
		self.business.list_business = [{'createdby':'john@email.com','name':'biz','location':'nairobi','category':'tech'}]
		user = 'john@email.com'
		result = self.business.get_creator(user)
		self.assertEqual(result,[{'createdby':'john@email.com','name':'biz','location':'nairobi','category':'tech'}])					

	# def test_get_business_by_id(self):
	# 	response = self.app.post(
	# 							'/api/v1/business/<int:business_id>',
	# 							# data=json.dumps(self.businesscreds),
	# 							headers={'Content-Type':'application/json'})
	# 	self.assertEqual(response.status_code,201)
	# 	result = json.loads(response.data.decode('utf-8').replace("'", "\""))
	# 	result = self.app.get(
	# 						'/api/v1/business/{}'.format(result['id']))
	# 	self.assertEqual(response.status_code,200)
							


if __name__ == '__main__':
	unittest.main()			