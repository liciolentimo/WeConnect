import unittest
from user import User,USERS
from business import Business, businessdetails
from app import app
import json


class UserTest(unittest.TestCase):

	def setUp(self):
		self.user = User()
		self.test_app = app.test_client()
		USERS = {'username':'john',
				'email':'john@email.com',
				'password':'123'	

		}
	def tearDown(self):
		del self.user 	

	def test_create_user(self):
		response = self.test_app.post(
					'/api/v1/register',
					data=json.dumps(dict(
						username='john',
						email='john@email.com',
						password='123')),
					content_type='application/json')	
		self.assertEqual(response.status_code,400)
		self.assertIn('john',USERS,msg='user not found')

	
	def test_duplicate_users(self):
		self.user.create_user('john','john@email.com','123')
		msg = self.user.create_user('john','john@email.com','123')
		self.assertIn("User already exists",msg)

		
if __name__ == '__main__':
	unittest.main()