from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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

if __name__ == "__main__":
    app.run(debug=True)