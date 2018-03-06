import unittest
from user import User


class UserTest(unittest.TestCase):
	
	def setUp(self):
		self.user = User()

	def test_create_user(self):
		self.user.create_user('john','john@email.com','123')
		self.assertIn('john',self.username)
		self.assertIn('john@email.com',self.email)
		self.assertIn('123',self.password)

	# def test_get_user(self):

			
if __name__ == '__main__':
	unittest.main()