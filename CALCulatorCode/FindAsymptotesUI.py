from sympy import symbols
from sympy import *
from sympy.calculus.util import continuous_domain
from sympy.calculus.util import function_range
from sympy import E
import HelpfulFunctions

def FindAsymptotes(userinput):

    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)

    x = symbols('x', real=True)

    userinput = eval(userinput) 

    domain = continuous_domain(userinput, x, S.Reals )
    HorizontalAsymptote = []

    if domain != Reals:

        domain = (str(domain)).replace("Interval", "")
        domain = (str(domain)).replace(".open", "")
        domain = (str(domain)).replace("Union", "")
        domain = (str(domain)).replace("(", "")
        domain = (str(domain)).replace(")", "")
        domain = (str(domain)).replace(" ", "")

        domain = domain.split(",")

        for i in range(len(domain) - 1):
            if domain[i] == domain[i + 1]:
                HorizontalAsymptote.append(eval(domain[i]))

        HorizontalAsymptote = str(HorizontalAsymptote).replace("[", "")
        HorizontalAsymptote = str(HorizontalAsymptote).replace("]", "")

    Graphrange = (function_range(userinput, x, Interval(-oo, oo)))

    Graphrange = (str(Graphrange)).replace("Interval", "")
    Graphrange = (str(Graphrange)).replace(".open", "")
    Graphrange = (str(Graphrange)).replace("Union", "")
    Graphrange = (str(Graphrange)).replace("(", "")
    Graphrange = (str(Graphrange)).replace(")", "")
    Graphrange = (str(Graphrange)).replace(" ", "")

    Graphrange = Graphrange.split(",")

    VerticalAsymptote = []
    HorizontalAsymptote = []

    for i in range(len(Graphrange) - 1):
        if Graphrange[i] == Graphrange[i + 1]:
            VerticalAsymptote.append(eval(Graphrange[i]))

    VerticalAsymptote = str(VerticalAsymptote).replace("[", "")
    VerticalAsymptote = str(VerticalAsymptote).replace("]", "")

    if len(HorizontalAsymptote) > 0:

        returnHorizontal = f'y = {HorizontalAsymptote}'

    else:
        
        returnHorizontal = "No Horiz Asym"

    if len(VerticalAsymptote) > 0:

        returnVertical = f'x = {VerticalAsymptote}'

    else:

        returnVertical = "No Vert Asym"

    return f'{returnVertical}\n{returnHorizontal}'