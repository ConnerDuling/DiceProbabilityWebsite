from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/howdy.html')
def index():
    return render_template('howdy.html')