from flask import Flask, url_for, request, abort, make_response,Response,jsonify
from user import User 
from utils import JSON_MIME_TYPE,search_business
import json


app = Flask(__name__)


# @app.errorhandler(404)
# def not_found(error):
# 		return make_response(jsonify({'error':'Not found'}),404)

@app.route('/api/v1/login')
def login():
	auth = request.authorization
	if auth and auth.password == '123':
		return ''

	return make_response('Could not verify!',401,{'WWW-Authenticate':'Basic realm="Login required"'})		


@app.route('/api/v1/business')
def list_business():
	response = Response(json.dumps(business),status=200,mimetype=JSON_MIME_TYPE)
	return response

@app.route('/api/v1/business/<int:business_id>')
def business_details():
	thebusiness = search_business(business,business_id)
	if thebusiness is None:
		abort(404)

	content = json.dumps(thebusiness)
	return content,200,{'Content-Type':JSON_MIME_TYPE}

@app.errorhandler(404)
def not_found(e):
	return '',404



# @app.route('api/v1//login')
# # def login():


if __name__ == '__main__':
	app.run(debug=True)
