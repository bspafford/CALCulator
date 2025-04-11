from sympy import symbols
from sympy import *
from sympy.calculus.util import continuous_domain
from sympy.calculus.util import function_range
from sympy import E
import HelpfulFunctions

def FindDomainRange(userinput):

    userinput = HelpfulFunctions.ConvertExponent(userinput)
    userinput = HelpfulFunctions.AddSigns(userinput)

    x = symbols('x', real=True)

    var( 'x' )
    domain = continuous_domain(eval(userinput), x, S.Reals )

    if domain == Reals:
        returnDomain =  "D = (-oo, oo)"

    else:

        domain = (str(domain)).replace("Interval", "")
        domain = (str(domain)).replace(".open", "")
        domain = (str(domain)).replace("Union", "")
        domain = (str(domain)).replace("(", "")
        domain = (str(domain)).replace(")", "")
        domain = (str(domain)).replace(" ", "")

        domain = domain.split(",")

        splitdomain = []

        for i in range(int((len(domain))/2)):
            splitdomain.append(f'({domain[i*2]},{domain[i*2 + 1]})')

        splitdomain = str(splitdomain)

        splitdomain = splitdomain.replace("[", "")
        splitdomain = splitdomain.replace("]", "")
        splitdomain = splitdomain.replace("'", "")

        returnDomain = f'D = {splitdomain}'

    Graphrange = (function_range(eval(userinput), x, Interval(-oo, oo)))

    Graphrange = (str(Graphrange)).replace("Interval", "")
    Graphrange = (str(Graphrange)).replace(".open", "")
    Graphrange = (str(Graphrange)).replace("Union", "")
    Graphrange = (str(Graphrange)).replace("(", "")
    Graphrange = (str(Graphrange)).replace(")", "")
    Graphrange = (str(Graphrange)).replace(" ", "")

    Graphrange = Graphrange.split(",")
    splitrange = []

    for i in range (int((len(Graphrange))/2)):
        splitrange.append(f'({Graphrange[i*2]},{Graphrange[i*2 + 1]})')

    splitrange = str(splitrange)
    splitrange = splitrange.replace("[", "")
    splitrange = splitrange.replace("]", "")
    splitrange = splitrange.replace("'", "")

    returnRange = f'R = {splitrange}'

    return f'{returnDomain}\n{returnRange}'
