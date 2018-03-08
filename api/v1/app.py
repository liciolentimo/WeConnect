from flask import Flask, url_for, request, abort, make_response,jsonify,session
from user import User
import json
import os
from business import Business


app = Flask(__name__)

app.secret_key = os.urandom(24)


users=User()
business = Business()


@app.route('/api/v1/register', methods=['POST'])
def register_user():
	if not request.json:
		abort(400)
	data = request.get_json()
	email = data.get('email')
	username = data.get('username')
	password = data.get('password')
	confirm_password = data.get('confirm_password')
	
	allemails = [i['email']for i in users.list_user if 'email' in i]

	allusernames = [i['username'] for i in users.list_user if 'username' in i]
	for e in allemails[:]:
		if e == email:
			return make_response(jsonify({'message':'User already exists'}))	
	for u in allusernames[:]:
		if u == username:
			return make_response(jsonify({'message':'User already exists'}))
	user = users.create_user(username,email,password,confirm_password)
	print(user)
	if user == True:
		return make_response(jsonify({'message':'successfully registered'}))
		return make_response(jsonify({'user':user}),200)
	else:
		return make_response(jsonify({'message': str(user)}))

@app.route('/api/v1/users',methods=['GET'])
def get_users():
	data = request.get_json()
	userdata=data.get_user(users)
	return jsonify({'users':users}),200	



@app.route('/api/v1/login',methods=['POST'])
def login():
	# if not request.json:
	# 	abort(400)
	 if request.method == "POST":
	 	email = request.json['email']
	 	password = request.json['password']
	 	session['email'] = email
	 	res = users.login(email,password)
	 	response = res
	 	return res 
	
	
@app.route('/api/v1/logout',methods=['POST'])
def logout():
	session.pop('email',None)
	return jsonify({'status':'You have been successfully logged out'}),200

@app.route('/api/v1/resetpassword',methods=['POST'])
def reset_password():
	if not request.json:
		abort(400)
	data = request.get_json()
	# email = data.get('email')
	password = data.get('password')
	new_password = data.get('new_password')

	user = users.reset_password(password,new_password)
	return jsonify({'user':user}),200		

@app.route('/api/v1/addbusiness', methods=['GET','POST'])
def register_business():
	if session.get('username') is not None:
		if request.method == 'POST':
			businessname = request.json['name']
			user = request.json['user']
			location = request.json['location']
			category = request.json['category']
			result = business.create_business(businessname,user,location,category)
			message = jsonify(result)
			response.status_code = 201
			return response	
	
		# if request.json:
		# 	data=request.get_json()
		# 	# email = data.get('email')
		# 	# password = data.get('password')
		# 	# user = users.create_user(email,password)
		# 	# user = users.login(email,password)
		# 	# logged_in_user = user['email']
		# 	# if logged_in_user:
		# 	# 	data = request.get_json()
		# 	# 	useremail = logged_in_user
		# 	name = data.get('name')
		# 	location = data.get('location')
		# 	category = data.get('category')
		# 	business.create_business(name,location,category)
		# 	return make_response(jsonify({'message':'business created successfully'}),201)
		# else:
		# 	return make_response(jsonify({'Business':businessdetails}),200)			




@app.route('/api/v1/business',methods=['GET'])
def list_business():
	return jsonify({'businessdetails':businessdetails})

@app.route('/api/v1/business/<int:business_id>',methods=['GET'])
def business_details(business_id):
	business = [business for business in businessdetails if business['id']== business_id]
	if len(business) == 0:
		return make_response(jsonify({'message':'business not found'}))
		abort(404)
	return jsonify({'business':business[0]})	

@app.route('/api/v1/updatebusiness',methods=['PUT'])
def update_business(business_id):
	business = [business for business in businessdetails['id'] == business_id]
	if len(business)==0:
		abort(404)
	if not request.json:
		abort(400)
	if 'name' in request.json and type(request.json['name']) != unicode:
		abort(400)
	if 'location' in request.json and type(request.json['location']) != unicode:
		abort(400)
	if 'category' in request.json and type(request.json['category']) != unicode:
		abort(400)
	business[0]['name'] = request.json.get('name',business[0]['name'])
	business[0]['location'] = request.json.get('location',business[0]['location'])
	business[0]['category'] = request.json.get('category',business[0]['category'])

	return jsonify({'business':business[0]})	

@app.route('/api/v1/deletebusiness',methods=['DELETE'])
def delete_business(business_id):
	business = [business for business in businessdetails if business['id'] == business_id]
	if len(business) == 0:
		abort(404)
	businessdetails.remove(business[0])
	return jsonify({'result':True})							


@app.errorhandler(404)
def not_found(e):
	return '',404


if __name__ == '__main__':
	app.run(debug=True)
