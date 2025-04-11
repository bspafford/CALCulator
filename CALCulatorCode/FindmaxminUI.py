import sympy as sp
from sympy import *
from sympy import symbols, Eq, pi, cos, sin, solve
from sympy.calculus.util import continuous_domain
import random
from sympy import E
import HelpfulFunctions

def Findmaxmin(userinput):

    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)

    x = symbols('x', real=True)

    var( 'x' )
    domain = continuous_domain(eval(userinput), x, S.Reals )

    if domain == Reals:
        domain = [-oo, oo]

    else:

        domain = (str(domain)).replace(".open", "")
        domain = (domain).replace("Interval", "")
        domain = (domain).replace("Union", "")
        domain = (domain).replace(" ", "")
        domain = HelpfulFunctions.split(domain)

        domain.pop(0)
        domain.pop(0)
        domain.pop(-1)
        domain.pop(-1)

        comma = 0
        for i in range(len(domain)):
            if domain[i] == "," and comma == 1:
                
                domain[i+1] = ""
                domain[i-1] = ""
                comma += 1

            elif domain[i] == ",":
                
                comma += 1

        domain = ''.join(domain)
        domain = domain.split(",")

        for i in range(len(domain)):
            if domain[i] == 'oo':
                domain[i] = oo
            elif domain[i] == '-oo':
                domain[i] = -oo
            else:
                domain[i] = N(domain[i])

        for i in range(len(domain)):
            domain[i] = N(domain[i])

    diff = sp.diff(eval(userinput), x)

    zeros = solve(diff - 0, x)

    keepzeros = []

    for a in range(int(len(zeros))):
        zeros[a] = N(zeros[a])
    #inbetween first set or inbetween second set...
        for b in range(int(len(domain)/2)):
                if float(zeros[a]) > float(domain[b*2]) and float(zeros[a]) < float(domain[b*2+1]):
                    keepzeros.append(domain[b])
                    keepzeros.append(zeros[a])
                    keepzeros.append(domain[b+1])

    maxlist = []
    minlist = []

    for i in range(len(keepzeros) - 2):

        if domain[i] == oo:

            numInRange = random.uniform(keepzeros[i+1], keepzeros[i + 2])
            numInRange2 = keepzeros[i + 1] + 1

        elif domain[i] == -oo:

            numInRange = keepzeros[i + 1] - 1
            numInRange2 = random.uniform(keepzeros[i+1], keepzeros[i + 2])
            
        else:

            numInRange = random.uniform(keepzeros[i], keepzeros[i + 1])
            numInRange2 = random.uniform(keepzeros[i+1], keepzeros[i + 2])

        numInRange = diff.subs(x, numInRange)

        numInRange2 = diff.subs(x, numInRange2)

        if numInRange > 0 and numInRange2 < 0:
            maxlist.append(keepzeros[i + 1])
        elif numInRange < 0 and numInRange2 > 0:
            minlist.append(keepzeros[i + 1])
        
        if len(maxlist) == 0:
            returnMax = "No Max"
        else:
            returnMax = f'Max x = {maxlist}'
        if len(minlist) == 0:
            returnMin = "No Min"
        else:
            returnMin = f'Min x = {minlist}'

    return f'{returnMax}\n{returnMin}'