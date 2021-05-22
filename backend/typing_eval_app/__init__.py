from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



#session key subject to change
app.secret_key = "key"
