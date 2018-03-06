import unittest
from user import User,USERS
from business import Business, businessdetails


class UserTest(unittest.TestCase):

	def setUp(self):
		self.user = User()
		USERS = {'username':'john',
				'email':'john@email.com',
				'password':'123'	

		}

	def test_create_user(self):
		self.user.create_user('john','john@email.com','123')
		self.assertIn('john',self.username)
		self.assertIn('john@email.com',self.email)
		self.assertIn('123',self.password)

	# def test_get_user(self):

			
if __name__ == '__main__':
	unittest.main()