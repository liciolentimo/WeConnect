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
			USERS.append(user)
			return {'message': 'User successfully created'}
			# self.Users['user'] = json.dumps(user)
			return user		

	def get_user(self):
			return USERS

	def login(self,email,password):
		user = [user for user in USERS if user['email']== email and user['password']==password]
		return user

	def reset_password(self,email,password,new_password):
		user = [user for user in USERS if user['email']==email and user['password']==password]
		user[0]['password']=new_password
		return user
	
					


		# def find_element_by_name(self):
		# 	self.username = username
		# 	self.email = email
		# 	self.password = password

		# def register(self):
		# 	return self.app.post('register/')
		# 	data = dict(username=username,email=email,password=password,follow_rediects=True)	




		