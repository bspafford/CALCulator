from sympy import symbols
import sympy as sp
from sympy import *
from sympy import E
import HelpfulFunctions

def Tangent(userinput):

     #f(x), x, x value
     userinput = HelpfulFunctions.ConvertExponent(userinput)
     userinput = HelpfulFunctions.AddSigns(userinput)
     userinput = userinput.split(",")

     #solve diff at point
     x = symbols('x')
     diff = sp.diff(userinput[0])
     diff = diff.subs(x, userinput[1])

     #solve for y
     y = eval(userinput[0])
     y = y.subs(x, userinput[1])

     if float(userinput[1]) - float(userinput[1]) == 0:
          userinput[1] = float(userinput[1])
     else:
          userinput[1] = float(userinput[1])

     #y = y1 + m(x - x1)
     answer = simplify(y + (diff * (x - userinput[1])))
     answer = HelpfulFunctions.RemoveAndRevert(answer)

     return answer