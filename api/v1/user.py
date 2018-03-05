from flask import json



class User():
	
	
	
	def __init__(self):
		# super(User, self).__init__()
		self.username = None
		self.email = None
		self.password = None
		self.Users = {}

	def create_user(self,username,email,password):
			user = [{'username':username,
					'email':email,
					'password':password}]
			self.Users['user'] = json.dumps(user)
			return user		

	def get_user(self):
			return Users	


		# def find_element_by_name(self):
		# 	self.username = username
		# 	self.email = email
		# 	self.password = password

		# def register(self):
		# 	return self.app.post('register/')
		# 	data = dict(username=username,email=email,password=password,follow_rediects=True)	




		