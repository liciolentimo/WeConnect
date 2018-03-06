from flask import Flask, url_for, request, abort, make_response,jsonify
from user import User,USERS 
import json
from business import Business,businessdetails

app = Flask(__name__)

users=User()

@app.route('/api/v1/users',methods=['GET'])
def get_users():
	return jsonify({'users':USERS}),200

# @app.errorhandler(404)
# def not_found(error):
# 		return make_response(jsonify({'error':'Not found'}),404)
@app.route('/api/v1/register', methods=['GET','POST'])
def register_user():
	if not request.json:
		abort(400)
	data = request.get_json()
	email = data.get('email')
	username = data.get('username')
	password = data.get('password')
	allemails = [i['email']for i in USERS if 'email' in i]
	allusernames = [i['username'] for i in USERS if 'username' in i]
	for e in allemails[:]:
		if e == email:
			abort(400)	
	for u in allusernames[:]:
		if u == username:
			abort(400)
	user = users.register_user(username,email,password)
	return jsonify({'user':user})



@app.route('/api/v1/login',methods=['POST'])
def login():
	if not request.json:
		abort(400)
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = users.login(email,password)
	session['useremail'] = user[0]['email']
	if 'useremail' in session:
		useremail = session['useremail']
		return jsonify({'logged_in':useremail}),200
	return jsonify({'status':'Not logged in'}),401
	
@app.route('/api/v1/logout',methods=['POST'])
def logout():
	session.pop('useremail',None)
	return jsonify({'status':'You have been successfully logged out'}),200

@app.route('/api/v1/resetpassword',methods=['POST'])
def reset_password():
	if not request.json:
		abort(400)
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	new_password = data.get('new_password')

	user = users.reset_password(email,password,new_password)
	return jsonify({'user':user}),200					


@app.route('/api/v1/business',methods=['GET'])
def list_business():
	return jsonify({'businessdetails':businessdetails})

@app.route('/api/v1/business/<int:business_id>',methods=['GET'])
def business_details(business_id):
	business = [business for business in businessdetails if business['id']== business_id]
	if len(business) == 0:
		abort(404)
	return jsonify({'business':business[0]})	


@app.errorhandler(404)
def not_found(e):
	return '',404



# @app.route('api/v1//login')
# # def login():


if __name__ == '__main__':
	app.run(debug=True)
