import sympy as sp
from sympy import *
from sympy import symbols, Eq, pi, cos, sin, solve
from sympy.calculus.util import continuous_domain
import random
from sympy import E
import HelpfulFunctions

def PointsOfInflection(userinput):

    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)

    x = symbols('x', real=True)

    y = eval(userinput)

    var( 'x' )
    domain = continuous_domain(y, x, S.Reals)

    domain = (str(domain)).replace(".open", "")
    domain = (str(domain)).replace("Interval", "")
    domain = (str(domain)).replace("Union", "")
    domain = (str(domain)).replace("(", "")
    domain = (str(domain)).replace(")", "")
    domain = (str(domain)).replace(" ", "")

    domain = domain.split(",")

    if domain[0] == "Reals":
        domain[0] = -oo
        domain.append(oo)
    else:
        for i in range(len(domain)):
            if domain[i] == 'oo':
                domain[i] = oo
            elif domain[i] == '-oo':
                domain[i] = -oo
            else:
                domain[i] = float(domain[i])

    diff = sp.diff(sp.diff(y, x))

    zeros = solve(diff - 0)

    if len(zeros) == 0:
        return "None"
    else:
        zeros.insert(0, min(domain))
        zeros.append(max(domain))

        InflectionList = []

        for i in range(len(zeros) - 2):

            if domain[i] == oo:

                numInRange = random.uniform(zeros[i+1], zeros[i + 2])
                numInRange2 = zeros[i + 1] + 1

            elif domain[i] == -oo:

                numInRange = zeros[i + 1] - 1
                numInRange2 = random.uniform(zeros[i+1], zeros[i + 2])
                
            else:

                numInRange = random.uniform(zeros[i], zeros[i + 1])
                numInRange2 = random.uniform(zeros[i+1], zeros[i + 2])

            numInRange = diff.subs(x, numInRange)

            numInRange2 = diff.subs(x, numInRange2)

            InflectionList.append(zeros[i + 1])

            return InflectionList