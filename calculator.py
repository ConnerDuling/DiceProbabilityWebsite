def factorial(n):
    '''
    Returns the total of 1 * ... * n
    '''
    sum = 1
    if n == 1:
        return sum
    for i in range(2, n + 1):
        sum *= i
    return sum

def choose(n,r):
    '''
    Calculates the statistical Combination of the inputs n and r
    '''
    if r > n:
        return 0
    else:
        return factorial(n) / (factorial(r) * (factorial(n - r)))

def diceSummation(totalDice, targetDice, prob):
    '''
    Calculates the total probability of targetDice number of dice having a
    certain outcome out of totalDice, given a specific prob of success.
    '''
    probSum = 0
    for i in range(targetDice, (totalDice + 1)):
        probSum += choose(totalDice, i) * pow(prob, i) * pow((1-prob), (totalDice - i))
    return probSum


# -----------------------------------------------------------
# conMod = int(input("What is your CON modifier?: "))

# for j in range(1,7): #Dice numbers
#     outputString = ""
#     outputString += str(j)+" Checks: "
#     i = 5
#     while(i <= 20): #DC

#         #Difficulty Math
#         difficulty = 1 - (((i-conMod)-1)/20)

#         outputString += "   "+str('{:.5f}'.format(diceSummation(j, j, difficulty)))
#         i += 5
    
#     print(outputString)
# ------------------------------------------------------------



# totalDice = int(input("How many dice total?: "))
# targetDice = int(input("How many dice do you want to hit or exceed the target?: "))
# prob = float(input("Probability of a single success?: "))

# print(str(diceSummation(totalDice, targetDice, prob)))