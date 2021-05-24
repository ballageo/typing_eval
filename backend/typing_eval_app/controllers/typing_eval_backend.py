from typing_eval_app import app
from flask import jsonify
from random_word import RandomWords

@app.route('/')
def index():
    return "STRING"

class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age:int = age

george = User('georeg', 27)
jin = User('jin', 25)

@app.route('/api/test')
def api_index():
    return jsonify([george.__dict__, jin.__dict__])

@app.route('/api/generate')
def doc_generate():
    r = RandomWords()
    WPM_TEXT = r.get_random_words(minLength=3, maxLength=6, minDictionaryCount=5, limit=400)
    words = ' '.join(word for word in WPM_TEXT)
    print(words)
    print(len(words))
    return jsonify(words) # generates a new random paragraph of content and returns a response object in JSON
