from sympy import symbols
import sympy as sp
from sympy import *
from sympy import E
import HelpfulFunctions

def Derivatives(Input):

    #to find E**x you need to make the letter capital
    Input = HelpfulFunctions.ConvertExponent(Input)
    Input = HelpfulFunctions.AddSigns(Input)
    Input = Input.split(",")

    x = symbols('x')

    if len(Input) == 1:

        diff = sp.diff(Input[0], x)
        diff = HelpfulFunctions.RemoveAndRevert(diff)

    elif len(Input) == 2:

        diff = sp.diff(eval(Input[0]), x)
        diff = diff.subs(x, Input[1])
        diff = HelpfulFunctions.RemoveAndRevert(diff)

    return diff
