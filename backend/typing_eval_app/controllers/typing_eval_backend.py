from typing_eval_app.models.users import User
from typing_eval_app.models.stats import Stat
from typing_eval_app import app
from flask import jsonify, request
import requests, random
import json

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()

@app.get('/')
def index():
    return "STRING"

@app.get('/api/generate')
def doc_generate():
    global WORDS
    res = ' '.join(word.decode() for word in random.choices(WORDS, k=250))
    return jsonify(res) # generates a new random paragraph of content and returns a response object in JSON

@app.get('/api/user/get/<int:id>')
def show_user(id):
    user = User.get_one({"id":id})
    return jsonify(user.__dict__)

@app.post('/api/stat/create')
def create_stat():
    print(request.get_json())
    # data = {
    #     "user_id" : 'placehold', #USER ID HERE
    #     "wpm" : 100, #WPM HERE
    #     "accuracy" : 99.9 #ACCURACY HERE
    # }
    # Stat.save(data)
    return jsonify("testing")