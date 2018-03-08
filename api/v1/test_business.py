import unittest
from app import app
from business import Business,businessdetails
from user import User
import json

class BusinessTest(unittest.TestCase):
	def setUp(self):
		self.business = Business()
		self.test = app.test_client()
		self.businesscreds = {
					'id': 1,
					'name':'tuskys',
					'location':'nairobi',
					'category':'supermarket'
					# 'createdby':'john@email.com'
		}

	def test_register_business(self):
		response = self.test.post(
								'/api/v1/addbusiness',
								data=json.dumps(self.businesscreds),
								headers={'Content-Type':'application/json'})
		self.assertEqual(response.status_code,201)
		self.assertIn('business created successfully', str(response.data))	



	def test_list_business(self):
		response = self.test.get('/api/v1/business')
		self.assertEqual(response.status_code,200)	

	# def test_update_business(self):
	# 	self.business.business1 = {'created_by':'john@email.com','name':'tuskys','location':'nairobi'}
	# 	self.business.business2 = {'created_by':'john@email.com','name':'naivas','location':'nairobi'}
	# 	message = self.business.update_business(business2)
	# 	self.assertEqual(message,'successfully updated')


if __name__ == '__main__':
	unittest.main()			