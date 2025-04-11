import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
import sympy as sp
from sympy import *
from sympy import E
import HelpfulFunctions

def SolidsOfRevolution(userinput):

    userinput = userinput.replace(" ", "")
    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)
    userinput = userinput.split(",")

    x = symbols('x', real=True)

    #find intersection
    intersections = solve(eval(userinput[0]) - eval(userinput[1]))
    intersections.sort()
    reverseInt = intersections

    if userinput[2] == "int" and userinput[3] == "int":

        if len(intersections) < 2:

            return "Not 2 Ints"

        elif len(intersections) == 2:

            answer = simplify(pi*(sp.integrate(eval(userinput[0])**2 - eval(userinput[1])**2, (x, intersections[0], intersections[1]))))
            answer = HelpfulFunctions.RemoveAndRevert(answer)
            return answer

        else:
            return "Has More Than 2 Ints"

    elif userinput[2] == "int":
        
        for i in range(len(intersections)):
            if reverseInt[i] < float(userinput[3]):
                FoundIntersection = intersections[i]

        FoundIntersection = N(FoundIntersection)
        answer = simplify(pi*(sp.integrate(eval(userinput[0])**2 - eval(userinput[1])**2, (x, FoundIntersection, eval(userinput[3])))))
        answer = HelpfulFunctions.RemoveAndRevert(answer)
        return answer

    elif userinput[3] == "int":
        reverseInt.reverse()
        for i in range(len(intersections)):

            if reverseInt[i] > float(userinput[2]):
                FoundIntersection = intersections[i]

        FoundIntersection = N(FoundIntersection)
        answer = simplify(pi*(sp.integrate(eval(userinput[0])**2 - eval(userinput[1])**2, (x, eval(userinput[2]), FoundIntersection))))
        answer = HelpfulFunctions.RemoveAndRevert(answer)
        return answer

    else:

        answer = simplify(pi*(sp.integrate(eval(userinput[0])**2 - eval(userinput[1])**2, (x, eval(userinput[2]), eval(userinput[3])))))
        answer = HelpfulFunctions.RemoveAndRevert(answer)
        return answer