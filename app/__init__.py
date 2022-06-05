import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title="About Me", firstname="First", lastname="Name", url=os.getenv("URL"))

@app.route('/experiences.html')
def experiences():
    return render_template('experiences.html', title="My Experiences")
