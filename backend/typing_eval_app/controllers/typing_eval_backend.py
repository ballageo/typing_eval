from typing_eval_app.models.users import User
from typing_eval_app import app
from flask import jsonify
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
    res = ' '.join(word.decode() for word in random.choices(WORDS, k=150))
    return jsonify(res) # generates a new random paragraph of content and returns a response object in JSON

@app.route('/user/get/<int:id>')
def show_user(id):
    user = User.get_one({"id":id})
    return jsonify(user.__dict__)