from sympy import *
from sympy import symbols
import sympy as sp
from sympy import E
import HelpfulFunctions

def FindAverageValueOfFunction(userinput):

    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)
    userinput = userinput.split(",")

    x = symbols('x', real=True)

    for i in range(len(userinput)):
        userinput[i] = eval(userinput[i])

    answer = simplify((1/(userinput[2] - userinput[1]))*(sp.integrate(userinput[0], (x, userinput[1], userinput[2]))))
    return answer
