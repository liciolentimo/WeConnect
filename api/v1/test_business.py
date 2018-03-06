import unittest
from app import app
from business import Business,businessdetails
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
		}

	# def test_register_business(self):
	# 	response = self.test.post(
	# 							'/api/v1/addbusiness',
	# 							data=json.dumps(self.businesscreds),
	# 							headers={'Content-Type':'application/json'})
	# 	self.assertEqual(response.status_code,201)
	# 	self.assertIn('Business successfully created', str(response.data))	

	def test_list_business(self):
		response = self.test.get('/api/v1/business')
		self.assertEqual(response.status_code,200)					

if __name__ == '__main__':
	unittest.main()			