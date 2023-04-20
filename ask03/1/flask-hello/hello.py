from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    var = 'MESSAGE'
    val = os.getenv(var)
    return str(val)

app.run(host='0.0.0.0', port=8080)
