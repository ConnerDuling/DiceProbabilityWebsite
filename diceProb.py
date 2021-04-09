from flask import Flask, render_template, request
from calculator import diceSummation
#from situationGenerator import outcome

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def diceProb():

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


    if request.form.get("failOneRollOf1"):
        #If a roll of 1 should ALWAYS be a loss
        if hiddenDC > 20:
            hiddenDC = 19
        if hiddenDC < 1:
            hiddenDC = 1
    else:
    #If a roll of 1 should be a win, if the DC is low enough
        if hiddenDC > 20:
            hiddenDC = 19
        if hiddenDC < 1:
            hiddenDC = 0

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
        
        return render_template('index.html',
                                difficultyValue=10,
                                modifier=0,
                                rollType="standard roll")