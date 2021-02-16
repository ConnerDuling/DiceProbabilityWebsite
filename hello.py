from flask import Flask, render_template, request
from calculator import diceSummation

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():

    result = diceSummation(2, 1, .5)

    if request.method == "POST":
        return render_template('index.html', result=result)

    else:
        return render_template('index.html')

@app.route('/howdy.html')
def howdy():
    return render_template('howdy.html')