# Imports
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from essential_generators import DocumentGenerator

# Setups
app = Flask(__name__)
CORS(app)
gen = DocumentGenerator() # Provides ability to generate random data

# Routes
@app.route('/api/test')
def api_index():
    return jsonify(gen.paragraph()) # Generates a new random paragraph of content, 
    #                                 and returns a Response object containing JSON data

# Server Initialization
if __name__ == "__main__":
    app.run(debug=True)