from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
import requests



def auth(request):
	code = request.GET['code']
	url = "https://www.linkedin.com/oauth/v2/accessToken"
	data = {'grant_type':'authorization_code','code':code,'redirect_uri':'http://127.0.0.1:8000/auth','client_id':'86n778segshrmo','client_secret':'gu92vsXYQYJL2RAJ'}
	r = requests.post(url, data=data)
	access_token = r.json()['access_token']
	url = "https://api.linkedin.com/v2/me"
	headers = {"Authorization": "Bearer "+access_token}
	r = requests.get(url, headers=headers)
	data = r.json()
	print(data)
	url = "https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))"
	headers = {"Authorization": "Bearer "+access_token}
	r = requests.get(url, headers=headers)
	dat = r.json()
	print(dat)
	url = "https://api.linkedin.com/v2/me?projection=(id,profilePicture(displayImage~digitalmediaAsset:playableStreams))"
	headers = {"Authorization": "Bearer "+access_token}
	r = requests.get(url, headers=headers)
	image_data = r.json()
	image_url = image_data['profilePicture']['displayImage~']['elements'][3]['identifiers'][0]['identifier']
	print(str(image_url))
	fname = data['firstName']['localized']['en_US']
	lname = data['lastName']['localized']['en_US']
	id = data['id']
	email = dat['elements'][0]['handle~']['emailAddress']
	return redirect('registration_view')

# Create your views here.