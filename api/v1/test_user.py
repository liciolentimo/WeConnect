import unittest
from user import User,USERS
from app import app
import json


class UserTest(unittest.TestCase):

	def setUp(self):
		self.user = User()
		self.test = app.test_client()
		self.creds = {'username':'john',
				'email':'john@email.com',
				'password':'123'	

		}
	def tearDown(self):
		del self.user 

	def test_register_user(self):
		response = self.test.post(
								'/api/v1/register',
								data=json.dumps(self.creds),
								headers={'Content-Type':'application/json'})
		self.assertEqual(response.status_code,201)
		self.assertIn('User successfully created',str(response.data))

	def test_get_users(self):
		response = self.test.get('/api/v1/users')
		self.assertEqual(response.status_code,200)														


	def login(self,email='john@email.com',password='123'):
		users = {'email':email,'password':password}
		return self.data.post('/api/v1/login',
								headers={'Content-Type':'application/json'},
								data = json.dumps(data))	

	def test_cannot_login_unregistered_user(self):
		result = self.test.post(
								'/api/v1/login',
								headers={'Content-Type':'application/json'},
								data=json.dumps(self.creds))
		self.assertEqual(result.status_code,401)							

	
	def test_duplicate_users(self):
		self.user.create_user('john','john@email.com','123')
		second_result = self.user.create_user('john','john@email.com','123')
		result = json.loads(second_result.data.decode())
		self.assertEqual(result['message'],'user already exists'+'please login')
		self.assertEqual(second_result.status_code,202)

	def test_invalid_email(self,email):
		msg = ('john',self.email,'john@gmail.com')
		self.assertEqual(msg,"enter a valid email address")

	# def test_login_wrong_password(self):
	# 	self.user.user()=[{'email':'john@email.com','password':'123'}]		

		
if __name__ == '__main__':
	unittest.main()