from flask import Flask, render_template, request
from calculator import diceSummation

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():

    

    modifier = 0
    if(request.form.get("dcInput") != None):
        difficultyValue = int(request.form.get("dcInput"))
        modifier = int(request.form.get("modInput"))
    else:
        difficultyValue = 10
    hiddenDC = difficultyValue - modifier - 1

    #Catches for if the values would cause a result of > 100% or < 0%
    if hiddenDC > 20:
        hiddenDC = 21
    if hiddenDC < 1:
        hiddenDC = 1

    probOfPureWin = 1 - (1 * hiddenDC / 20)

    result = diceSummation(1, 1, probOfPureWin)

    result *= 100

    if request.method == "POST":
        
        return render_template('index.html',
                                result=round(result, 2),
                                difficultyValue=difficultyValue,
                                modifier=modifier)

    else:
        return render_template('index.html')

# @app.route('/howdy.html')
# def howdy():
#     return render_template('howdy.html')