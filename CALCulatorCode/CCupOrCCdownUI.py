import sympy as sp
from sympy import *
from sympy import symbols, solve
from sympy.calculus.util import continuous_domain
import random
from sympy import E
import HelpfulFunctions

def CCupOrCCdown(userinput):

    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)

    x = symbols('x', real=True)

    y = eval(userinput)

    var( 'x' )
    domain = continuous_domain(y, x, S.Reals)

    if domain == Reals:
        domain = [-oo, oo]
    else:
        domain = (str(domain)).replace(".open", "")
        domain = (str(domain)).replace("Interval", "")
        domain = (str(domain)).replace("Union", "")
        domain = (str(domain)).replace("(", "")
        domain = (str(domain)).replace(")", "")
        domain = (str(domain)).replace(" ", "")
        domain = domain.split(",")

        for i in range(len(domain)):
            if domain[i] == 'oo':
                domain[i] = oo
            elif domain[i] == '-oo':
                domain[i] = -oo
            else:
                domain[i] = N(domain[i])

    diff = sp.diff(sp.diff(eval(userinput), x))
    zeros = solve(diff - 0)
    zeros.insert(0, min(domain))
    zeros.append(max(domain))

    CCup = []
    CCdown = []

    for i in range(len(zeros) - 1):

        if zeros[i + 1] == oo:

            numInRange = random.uniform(zeros[i], zeros[i] + 1)

        elif zeros[i] == -oo:

            numInRange = random.uniform(zeros[i + 1], zeros[i + 1] - 1)
            
        else:

            numInRange = random.uniform(zeros[i], zeros[i + 1])

        numInRange = diff.subs(x, numInRange)

        #for i in range(len())
        if numInRange > 0:
            CCup.append(zeros[i])
            CCup.append(zeros[i + 1])
        elif numInRange < 0 :
            CCdown.append(zeros[i])
            CCdown.append(zeros[i + 1])

    CCuplist = []
    CCdownlist = []

    CCup = str(CCup).replace("[", "")
    CCup = str(CCup).replace("]", "")
    CCup = str(CCup).replace(" ", "")
    CCup = str(CCup).split(",")

    CCdown = str(CCdown).replace("[", "")
    CCdown = str(CCdown).replace("]", "")
    CCdown = str(CCdown).replace(" ", "")
    CCdown = str(CCdown).split(",")

    for i in range(int(len(CCup)/2)):

        CCuplist.append(f'({CCup[i]},{CCup[i+1]})')
        CCuplist[i] = eval(CCuplist[i])

    for i in range(int(len(CCdown)/2)):

        CCdownlist.append(f'({CCdown[i]},{CCdown[i+1]})')
        CCdownlist[i] = eval(CCdownlist[i])

    CCuplist = str(CCuplist).replace("[", "")
    CCuplist = str(CCuplist).replace("]", "")
    CCdownlist = str(CCdownlist).replace("[", "")
    CCdownlist = str(CCdownlist).replace("]", "")

    if len(CCuplist) == 0:
        returnCCup = "No CC up"
    else:
        returnCCup = f'CC Up = {CCuplist}'
    if len(CCdownlist) == 0:
        returnCCdown = "No CC down"
    else:
        returnCCdown = f'CC Down = {CCdownlist}'

    return f'{returnCCup}\n{returnCCdown}'