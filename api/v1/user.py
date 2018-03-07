import re
# import regular expressions

class User():

	def __init__(self):
		
		self.list_user=[]
		

	def create_user(self,username,email,password,confirm_password):
			# initialize empty dictionary to store users
			userinfo = {}
			
			for user in self.list_user:
				if username == user['username']:
					return "User already exists. Try again"
				elif email == user['email']:
					return "User already exists. Try again"	
			# check for special characters in username
			if not re.match("^[a-zA-Z0-9_]*$", username):
				return "Invalid username."
			elif len(password) < 6:
				return "Your password should be at least 6 characters"
			#check for valid email	
			elif not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
				return "Please enter a valid email address"	
			#check whether password matches with confirm password
			elif password == confirm_password:
				userinfo['username'] = username	
				userinfo['email'] = email
				userinfo['password'] = password

				self.list_user.append(userinfo)
			else:
				return "Passwords do not match"
			return "User successfully registered"					
				
			
			# self.Users['user'] = json.dumps(user)

	def get_user(self):
			return self.list_user

	def login(self,email,password):
		for user in self.list_user:
			if email == user['email']:
				if password == user['password']:
					return "Login successful"
				
				return "Invalid username or password"

		return "Account does not exist. Please register."				

	def reset_password(self,new_password,confirm_password):
		for user in self.list_user:
			if new_password == confirm_password:
				user['password'] = new_password
				return "Password changed successfully"
			
			return "Passwords do not match"
		return "User account does not exist"	
				


		# def find_element_by_name(self):
		# 	self.username = username
		# 	self.email = email
		# 	self.password = password

		# def register(self):
		# 	return self.app.post('register/')
		# 	data = dict(username=username,email=email,password=password,follow_rediects=True)	




		