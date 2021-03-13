from flask import Flask, render_template, request
from calculator import diceSummation

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():

    

    modifier = 0
    rollTypeFlag = ""
    if(request.form.get("dcInput") != None):
        difficultyValue = int(request.form.get("dcInput"))
        modifier = int(request.form.get("modInput"))
        rollTypeFlag = (request.form.get("rollType"))
    else:
        difficultyValue = 10
    
    #Calculates hidden REAL number that needs to be rolled >=
    hiddenDC = difficultyValue - modifier - 1

    #Catches for if the values would cause a result of > 100% or < 0%
    if hiddenDC > 20:
        hiddenDC = 21
    if hiddenDC < 1:
        hiddenDC = 1

    probOfPureWin = 1 - (1 * hiddenDC / 20)

    #Figures out what type of roll is being made.
    #I.e.   Advantage, roll two keep highers
    #       Standard, roll one
    #       Disadvantage, roll two take the lowest

    if rollTypeFlag == "roll at Advantage":
        result = diceSummation(2, 1, probOfPureWin)
    elif rollTypeFlag == "standard roll":
        result = diceSummation(1, 1, probOfPureWin)
    else:
        result = diceSummation(2, 2, probOfPureWin)

    result *= 100

    if request.method == "POST":
        
        return render_template('index.html',
                                result=round(result, 2),
                                difficultyValue=difficultyValue,
                                modifier=modifier,
                                rollType=rollTypeFlag)

    else:
        return render_template('index.html')