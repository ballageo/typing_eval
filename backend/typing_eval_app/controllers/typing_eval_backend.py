from typing_eval_app.models.users import User
from typing_eval_app.models.stats import Stat
from typing_eval_app import app
from flask import jsonify, request, session
import requests, random
import json

app.secret_key
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
    response = jsonify(res)
    session['key'] = 'value'
    print(session.__dict__, session['key'], '***trying to print session dictd and new key value')
    return jsonify(res) # generates a new random paragraph of content and returns a response object in JSON

@app.get('/api/user/get/<int:id>')
def show_user(id):
    user = User.get_one({"id":id})
    return jsonify(user.__dict__)

@app.post('/api/stat/create')
def create_stat():
    from operator import itemgetter
    text, del_count = itemgetter('text', 'delCount')(request.get_json()) # retreives values from incoming JSON data
    words = text.split()
    data = {
        "user_id" : 1, #USER ID HERE
        "wpm" : len(words)//60, #WPM HERE
        "accuracy" : 69.420, #ACCURACY HERE
        "backspace_count": del_count
    }
    print(session['key'], '***trying to print key value')
    # new_stat_id = Stat.save(data)
    # new_stat = Stat.get_one({"id": new_stat_id})
    # response = jsonify(new_stat)
    return jsonify(data)