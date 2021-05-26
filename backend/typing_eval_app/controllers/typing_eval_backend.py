from werkzeug.utils import redirect
from typing_eval_app.models.users import User
from typing_eval_app.models.stats import Stat
from typing_eval_app import app
from flask import jsonify, request
import requests, random
import json

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()

@app.route('/')
def index():
    return "STRING"

@app.route('/api/generate')
def doc_generate():
    global WORDS
    res = ' '.join(word.decode() for word in random.choices(WORDS, k=250))
    return jsonify(res) # generates a new random paragraph of content and returns a response object in JSON

@app.route('/user/get/<int:id>')
def show_user(id):
    user = User.get_one({"id":id})
    return jsonify(user.__dict__)

@app.route('/stat/create', methods = ['post'])
def create_stat():
    data = {
        "user_id" : 'placehold', #USER ID HERE
        "wpm" : 100, #WPM HERE
        "accuracy" : 99.9 #ACCURACY HERE
    }
    Stat.save(data)
    return redirect('http://localhost:3000')