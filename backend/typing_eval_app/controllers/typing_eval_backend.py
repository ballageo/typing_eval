from typing_eval_app import app
from flask import jsonify
from essential_generators import DocumentGenerator

gen = DocumentGenerator() # provides ability to generate random data

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
    return jsonify(gen.paragraph()) # generates a new random paragraph of content and returns a response object in JSON
