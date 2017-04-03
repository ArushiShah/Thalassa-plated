
from flask import Flask,request
from flask import render_template
import requests
import json
from flask_login import LoginManager, UserMixin, login_required
from jinja2 import Template

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def display_menu():
	url = 'https://plated-coding-challenge.herokuapp.com//v1/menus.json'
	headers = {'Authorization':'Token token="JQK2H4QjyhVIqZVyEPJNSwtt"','Content-Type': 'application/json'}
	
	# this issues a GET to the url. replace "get" with "post", "head",
	# "put", "patch"... to make a request using a different method
	r = requests.get(url, headers=headers)

	response = json.loads(r.text)
	#for items in r:
	#	print items[0]
	return render_template('index.html', response=response)

@app.route('/success')
def success():
	return render_template('success.html')

@app.route('/1menus')
def post_menu():
	url = 'https://plated-coding-challenge.herokuapp.com//v1/menus/331/recipes.json'
	headers = {'Authorization':'Token token="JQK2H4QjyhVIqZVyEPJNSwtt"','Content-Type': 'application/json'}
	
	# this issues a GET to the url. replace "get" with "post", "head",
	# "put", "patch"... to make a request using a different method
	r = requests.get(url, headers=headers)

	response = json.loads(r.text)
	

	return render_template('menus.html', response=response)

@app.route('/2menus')
def post_menu2():
	url = 'https://plated-coding-challenge.herokuapp.com//v1/menus/329/recipes.json'
	headers = {'Authorization':'Token token="JQK2H4QjyhVIqZVyEPJNSwtt"','Content-Type': 'application/json'}
	
	# this issues a GET to the url. replace "get" with "post", "head",
	# "put", "patch"... to make a request using a different method
	r = requests.get(url, headers=headers)

	response = json.loads(r.text)
	

	return render_template('menus.html', response=response)

@app.route('/3menus')
def post_menu3():
	url = 'https://plated-coding-challenge.herokuapp.com//v1/menus/332/recipes.json'
	headers = {'Authorization':'Token token="JQK2H4QjyhVIqZVyEPJNSwtt"','Content-Type': 'application/json'}
	
	# this issues a GET to the url. replace "get" with "post", "head",
	# "put", "patch"... to make a request using a different method
	r = requests.get(url, headers=headers)

	response = json.loads(r.text)
	

	return render_template('menus.html', response=response)

	
if __name__ == '__main__':
	app.run(debug=True)

