from sympy import symbols, solve
from sympy import * 
from sympy import E
import HelpfulFunctions

def PointOfIntersection(expr):

    x = symbols('x', real=True)

    expr = HelpfulFunctions.AddSigns(expr)
    expr = HelpfulFunctions.ConvertExponent(expr)
    expr = expr.split(",")

    expr1 = eval(expr[0])
    expr2 = eval(expr[1])

    if len(solve(expr1 - expr2)) == 0:
        return "None"
    else:
        Intersections = solve(expr1 - expr2)
        for i in range(len(Intersections)):



            Intersections[i] = N(Intersections[i])
            #if str(Intersections[i]).count("I") > 0: # <- should it be intersection[i].count???
                #Intersections[i] = ""
                
        while Intersections.count("") > 0:
            Intersections.remove("")
        for i in range(len(Intersections)):

            Intersections[i] = HelpfulFunctions.Round(Intersections[i])

        if len(Intersections) > 0:

            return Intersections

        else:

            return "None"
