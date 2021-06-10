from werkzeug.utils import redirect
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
    session['text'] = res
    # print(session.__dict__, session['key'], '***trying to print session dictd and new key value')
    return jsonify(res) # generates a new random paragraph of content and returns a response object in JSON

@app.get('/api/user/get/<int:id>')
def show_user(id):
    user = User.get_one({"id":id})
    return jsonify(user.__dict__)

@app.post('/api/stat/create')
def create_stat():
    from operator import itemgetter
    text, del_count = itemgetter('text', 'delCount')(request.get_json()) # retreives values from incoming JSON data
    words, sesh = text.split(), session['text'].split()
    acc_count = 0
    for idx, word in enumerate(words):
        if word == sesh[idx]:
            acc_count += 1
    acc = round(acc_count/len(words), 4)
    if "user_id" in session:
        user_id = session['user_id']
    else:
        user_id = 1
    data = {
        "user_id" : user_id, #USER ID HERE
        "wpm" : len(words)//60, #WPM HERE
        "accuracy" : acc*100, #ACCURACY HERE
        "backspace_count": del_count
    }
    new_stat_id = Stat.save(data)
    new_stat = Stat.get_one({"id": new_stat_id})
    return jsonify(new_stat)

@app.route('/api/stat/update/<int:id>')
def update_stat():
    if 'user_id' not in session:
        return 404
    from operator import itemgetter
    stat_id = itemgetter('stat_id')(request.get_json())
    data = {
        'user_id' : session['user_id'],
        'stat_id' : stat_id
    }
    updated_stat_id = Stat.update(data)
    updated_stat = Stat.get_one({"id":updated_stat_id})
    return jsonify(updated_stat)