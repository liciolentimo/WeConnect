import unittest
from user import User
from app import app
import json
import re 


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
		return self.test.post(
							'/api/v1/register',
							headers={'Content-Type':'application/json'},
							data=json.dumps(self.creds))
		response = self.user.create_user('john','john@email.com','12345678','12345678')
		self.assertIn(response,'User successfully registered')	
		self.assertEqual(response.status_code,200)

	def test_valid_login(self):
		"""test login with correct credentials"""
		return self.test.post(
							'/api/v1/login',
							headers={'Content-Type':'application/json'},
							data=json.dumps(self.creds))
		self.user.list_user = [{'username':'john','email':'john@email.com','password':'12345678'}]
		response = self.user.login('john@email.com','12345678')
		self.assertIn(response, 'Login successful')
		self.assertEqual(response.status_code,200)

	def test_login_incorrect_password(self):
		"""test login attemt with wrong password"""
		self.user.list_user = [{'username':'john','email':'john@email.com','password':'12345678'}]	
		response = self.user.login('john@email.com','john1234')
		self.assertEqual(response, 'Invalid username or password')

	def test_passwords_match(self):
		"""test if password matches with confirm password"""
		response = self.user.create_user('john','john@email.com','12345678','123456')
		self.assertEqual(response,'Passwords do not match')	

	def test_invalid_email(self):
		"""test if email entered is an email address of type email"""
		response = self.user.create_user('john','john.com','12345678','12345678')
		self.assertEqual(response,'Please enter a valid email address')

	def test_login_unregistered_user(self):
		self.user.list_user = [{'username':'john','email':'john@email.com','password':'12345678'}]
		response = self.user.login('mike@gmail.com','123456')
		self.assertEqual(response,'Account does not exist. Please register.')

	def test_special_characters(self):
		response = self.user.create_user('jo$n','john@email.com','12345678','12345678')
		self.assertIn(response,'Invalid username.')	

	def test_duplicate_registration(self):
		self.user.create_user('john','john@email.com','12345678','12345678')
		response = self.user.create_user('john','john@email.com','12345678','12345678')
		self.assertIn(response,'User already exists. Try again')

	def test_password_length(self):
		response = self.user.create_user('john','john@email.com','1234','1234')	
		self.assertEqual(response,'Your password should be at least 6 characters')

	# def test_get_users(self):
	# 	response = self.test.get('api/v1/users')
	# 	self.assertEqual(response.status_code,200)	



		
if __name__ == '__main__':
	unittest.main()