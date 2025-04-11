from sympy import symbols, solve
import sympy as sp
from sympy import *
from sympy import E
import HelpfulFunctions

def AreaofTwoFunctions(userinput):
    
    #equation1, equation2, bottom integral, top integral
    x = symbols('x', real=True)
    IntersectionAboveInput = False
    userinput = userinput.replace(" ", "")
    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)
    userinput = userinput.split(",")

    #find intersection
    intersections = solve((eval(userinput[0]) - eval(userinput[1])))
    intersections.sort()
    reverseInt = intersections

    if userinput[2] == "int" and userinput[3] == "int":

        if len(intersections) < 2:

            return "Not 2 ints"

        elif len(intersections) == 2:

            answer = simplify(sp.integrate(abs(eval(userinput[0]) - eval(userinput[1])), (x, intersections[0], intersections[1])))
            answer = HelpfulFunctions.Round(answer)
            answer = HelpfulFunctions.RemoveAndRevert(answer)
            return answer

        else:
            return "More Than 2 ints"

    elif userinput[2] == "int":
        
        for i in range(len(intersections)):
            if reverseInt[i] < float(userinput[3]):
                FoundIntersection = intersections[i]
                IntersectionAboveInput = True

        if IntersectionAboveInput == True:
            answer = simplify(sp.integrate(abs(eval(userinput[0]) - eval(userinput[1])), (x, FoundIntersection, userinput[3])))
            answer = HelpfulFunctions.Round(answer)
            answer = HelpfulFunctions.RemoveAndRevert(answer)
            return answer
        else:

            return f"No int below {userinput[3]}"

        

    elif userinput[3] == "int":
        reverseInt.reverse()
        for i in range(len(intersections)):
            
            if reverseInt[i] > float(userinput[2]):

                FoundIntersection = intersections[i]
                IntersectionAboveInput = True

        if IntersectionAboveInput == True:
            answer = simplify(sp.integrate(abs(eval(userinput[0]) - eval(userinput[1])), (x,userinput[2], FoundIntersection)))
            answer = HelpfulFunctions.Round(answer)
            answer = HelpfulFunctions.RemoveAndRevert(answer)
            return answer
        else:

            return f"No int above {userinput[2]}"

    else:
            answer = simplify(integrate(abs(eval(userinput[0]) - eval(userinput[1])), (x, userinput[2], userinput[3])))
            answer = HelpfulFunctions.Round(answer)
            answer = HelpfulFunctions.RemoveAndRevert(answer)
            return answer