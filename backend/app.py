# Imports
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from essential_generators import DocumentGenerator

# Setups
app = Flask(__name__)
CORS(app)
gen = DocumentGenerator()

# Routes
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
    return jsonify(gen.paragraph())

if __name__ == "__main__":
    app.run(debug=True)