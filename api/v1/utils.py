from flask import make_response

JSON_MIME_TYPE = 'application/json'

def search_business(business,business_id):
	for thebusiness in business:
		if thebusiness['id'] == business_id:
			return thebusiness

def json_response(data='',status=200,headers=None):
	headers = headers or {}
	if 'Content-Type' not in headers:
		headers['Content-Type'] = JSON_MIME_TYPE

	return make_response(data,status,headers)			
