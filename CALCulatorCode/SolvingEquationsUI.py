from sympy import symbols
from sympy import *
from sympy import E
import HelpfulFunctions

def SolvingEquations(userinput):
    
    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)
    userinput = userinput.split(",")


    x = symbols('x', real=True)

    answer = N(eval(userinput[0])).subs(x, userinput[1])
    answer = HelpfulFunctions.Round(answer)
    
    return answer