import sympy as sp
from sympy import symbols
from sympy import *
from sympy import E
import HelpfulFunctions

def Integrate(Input):

    Input = HelpfulFunctions.ConvertExponent(Input)
    Input = HelpfulFunctions.AddSigns(Input)
    Input = Input.split(",")

    x = symbols('x', real=True)

    if len(Input) == 1:

        integral = sp.integrate(eval(Input[0]), x)
        integral = HelpfulFunctions.RemoveAndRevert(integral)

    elif len(Input) == 4:

        integral = simplify(sp.integrate(eval(Input[0]), (x, Input[1], Input[2])))
        integral = HelpfulFunctions.RemoveAndRevert(integral)
    
    return integral