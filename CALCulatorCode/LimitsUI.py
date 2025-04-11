from sympy import *
from sympy import symbols
from sympy import E
import HelpfulFunctions

def Limits(userinput):

        userinput = HelpfulFunctions.ConvertExponent(userinput)
        userinput = HelpfulFunctions.AddSigns(userinput)
        userinput = userinput.replace(" ", "")
        userinput = userinput.split(",")
        x = symbols('x', real=True)

        if len(userinput) == 2:
                
                if limit(eval(userinput[0]), x, userinput[1], '+') == limit(eval(userinput[0]), x, userinput[1], '-'):
                        return limit(eval(userinput[0]), x, userinput[1])
                else:
                        return "DNE"

        if len(userinput) == 3:
                if userinput[2] == "+":
                        return limit(eval(userinput[0]), x, userinput[1], '+')

                elif userinput[2] == "-":
                        return limit(eval(userinput[0]), x, userinput[1], '-')