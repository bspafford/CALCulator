from sympy.solvers import solve
from sympy import symbols
import sympy as sp
from sympy import *
from sympy import E
import HelpfulFunctions

def CrossSection(userinput):

    #equation1, equation2, bottom integral, top integral
    #Notation: f(x), g(x), x1, x2, shape, *height*"
    x = symbols('x')
    userinput = userinput.replace(" ", "")
    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)
    userinput = userinput.split(",")

    if userinput[4].casefold() == "s":
        
        y = (eval(userinput[0]) - eval(userinput[1]))**2

    elif userinput[4].casefold() == "r":

        y = eval(userinput[5]) * (eval(userinput[0]) - eval(userinput[1]))**2

    elif userinput[4].casefold() == "t":
        
        #b * h / 2, 2h * h / 2
        y = eval(userinput[5]) * (eval(userinput[0]) - eval(userinput[1]))**2 / 2

    elif userinput[4].casefold() == "c":

        #pi * r**2
        y = pi * (eval(userinput[0]) - eval(userinput[1]))**2

    #find intersection
    intersections = solve(eval(userinput[0]) - eval(userinput[1]))
    intersections.sort()
    reverseInt = intersections

    if userinput[2] == "int" and userinput[3] == "int":

        if len(intersections) < 2:

            return "Not 2 Ints"

        elif len(intersections) == 2:

            answer = simplify(sp.integrate(y, (x, intersections[0], intersections[1])))
            answer = HelpfulFunctions.RemoveAndRevert(answer)
            return answer

        else:

            return "More Than 2 Ints"

    elif userinput[2] == "int":
        
        for i in range(len(intersections)):
            if reverseInt[i] < float(userinput[3]):
                FoundIntersection = intersections[i]

            FoundIntersection = N(FoundIntersection)

        answer = simplify(sp.integrate(y, (x, FoundIntersection, eval(userinput[3]))))
        answer = HelpfulFunctions.RemoveAndRevert(answer)
        return answer

    elif userinput[3] == "int":
        reverseInt.reverse()
        for i in range(len(intersections)):

            if reverseInt[i] > float(userinput[2]):
                FoundIntersection = intersections[i]

        answer = simplify(sp.integrate(y, (x, eval(userinput[2]), FoundIntersection)))
        answer = HelpfulFunctions.RemoveAndRevert(answer)
        return answer

    else:

            answer = simplify(integrate(y, (x, eval(userinput[2]), eval(userinput[3]))))
            answer = HelpfulFunctions.RemoveAndRevert(answer)
            return answer