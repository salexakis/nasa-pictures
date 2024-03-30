from flask import Blueprint, render_template, request, url_for, redirect 
from flask_mailman import EmailMessage
import requests
import os

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
  base_url = 'https://api.nasa.gov/planetary/apod?api_key='+ os.getenv('API_KEY')
  resp = requests.get(base_url).json()
  media = resp['url']
  return render_template('main.html', resp=resp, media=media)
 

@main.route('/data')
def fetch_data():
  start = request.args.get('start_date')
  end = request.args.get('end_date')
  base_url = 'https://api.nasa.gov/planetary/apod?api_key=' + os.getenv('API_KEY')
  final_url = base_url + '&start_date=' + start + '&end_date=' + end
  response = requests.get(final_url).json() 
  return response