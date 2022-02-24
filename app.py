from flask import Flask
from flask import request 
from flask import render_template
import requests

app = Flask(__name__)


headers = {
    'Authorization': 'Bearer h2qwogylnhh3rfdxgpiz4t58fuhuar',
    'Client-Id': 'lzd6ghbhj9dwlykiqab0uqw5npl6tt',
    'Access-Control-Allow-Origin': '*'
}

@app.route("/")
def hello_world():
    return "<p>Hello, World! </p>"

@app.route('/user')
def user():
    params = {
        ('login', request.args.get('name')),
    }
    response = requests.get('https://api.twitch.tv/helix/users', headers = headers, params=params)

    data = response.json()
    return data

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
