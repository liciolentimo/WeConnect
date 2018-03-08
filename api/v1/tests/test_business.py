import unittest
from app import app
from business import Business,businessdetails
from user import User
import json

class BusinessTest(unittest.TestCase):
	def setUp(self):
		self.business = Business()
		self.app = app.test_client()
		self.businesscreds = {
					'id': 1,
					'name':'tuskys',
					'location':'nairobi',
					'category':'supermarket'
					# 'createdby':'john@email.com'
		}

	def test_register_business(self):
		response = self.app.post(
								'/api/v1/addbusiness',
								data=json.dumps(self.businesscreds),
								headers={'Content-Type':'application/json'})
		self.assertEqual(response.status_code,201)
		self.assertIn('business created successfully', str(response.data))	



	def test_list_business(self):
		response = self.app.get(
								'/api/v1/business',
								data=json.dumps(self.businesscreds),
								headers={'Content-Type':'application/json'})
		response = self.app.get('/api/v1/business')
		self.assertEqual(response.status_code,200)	

	def test_get_business_by_id(self):
		response = self.app.get(
								'/api/v1/business/<int:business_id>',
								data=json.dumps(self.businesscreds),
								headers={'Content-Type':'application/json'})
		self.assertEqual(response.status_code,200)
		result = json.loads(response.data.decode('utf-8').replace("'", "\""))
		result = self.app.get(
							'/api/v1/business/{}'.format(result['id']))
		# self.assertEqual(response.status_code,200)
														

	# def test_update_business(self):
	# 	self.business.business1 = {'created_by':'john@email.com','name':'tuskys','location':'nairobi'}
	# 	self.business.business2 = {'created_by':'john@email.com','name':'naivas','location':'nairobi'}
	# 	message = self.business.update_business(business2)
	# 	self.assertEqual(message,'successfully updated')


if __name__ == '__main__':
	unittest.main()			