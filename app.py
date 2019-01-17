from flask import Flask
from flask import request
from flask import render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/poem/<poem_id>/')

def poem_now(poem_id):
    poem_id = int(poem_id)

    return render_template('poem_detail.html')
