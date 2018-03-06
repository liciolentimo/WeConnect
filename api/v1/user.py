from flask import json

USERS = [{
			'username':'john',
			'email':'john@email.com',
			'password':'123'
	}]

class User():
	
	
	
	
	def __init__(self):
		# super(User, self).__init__()
		self.username = None
		self.email = None
		self.password = None
		

	def create_user(self,username,email,password):
			user = {'username':username,
					'email':email,
					'password':password}
					USERS.append(users)
			# self.Users['user'] = json.dumps(user)
			return user		

	def get_user(self):
			return USERS

	def login(self,email,password):
		user = 
					


		# def find_element_by_name(self):
		# 	self.username = username
		# 	self.email = email
		# 	self.password = password

		# def register(self):
		# 	return self.app.post('register/')
		# 	data = dict(username=username,email=email,password=password,follow_rediects=True)	




		