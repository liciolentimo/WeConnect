import unittest
from user import User
# from app import app
import json
import re 


class UserTest(unittest.TestCase):

	def setUp(self):
		self.user = User()
		# self.test = app.test_client()
		# self.creds = {'username':'john',
		# 		'email':'john@email.com',
		# 		'password':'123'	

		# }
	def tearDown(self):
		del self.user 

	def test_register_user(self):
		response = self.user.create_user('john','john@email.com','12345678','12345678')
		self.assertIn(response,'User successfully registered')	

	def test_valid_login(self):
		"""test login with correct credentials"""
		self.user.list_user = [{'username':'john','email':'john@email.com','password':'12345678'}]
		response = self.user.login('john@email.com','12345678')
		self.assertIn(response, 'Login successful')

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



		
if __name__ == '__main__':
	unittest.main()