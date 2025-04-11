from sympy import *
from sympy import symbols
import sympy as sp
from sympy import E
import HelpfulFunctions

def AverageRateOfChange(userinput):

    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)
    userinput = userinput.split(",")

    x = symbols('x', real=True)

    for i in range(len(userinput)):
        userinput[i] = eval(userinput[i])

    F1Sub = userinput[0].subs(x, userinput[1])
    F2Sub = userinput[0].subs(x, userinput[2])

    #f(x1) - f(x2)
    #-------------
    #  x1  -   x2

    answer = simplify((F1Sub - F2Sub)/(userinput[1] - userinput[2]))
    return answer