import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import symbols
from numpy import *
from sympy import E
import HelpfulFunctions


def SolidsOfRevolution(userinput, Window):

    x = symbols('x', real=True)
    u = 0


    res = []
    for ele in userinput:
        if ele.strip():
            res.append(ele)

    userinput = res

    #answer = simplify(pi*(sp.integrate(eval(userinput[i])**2, (x, 0, 1))))
    #answer = HelpfulFunctions.RemoveAndRevert(answer)
    u = np.linspace(eval(str(Window[0])), eval(str(Window[1])), 60)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    #u = np.linspace(float(userinput[2]), float(userinput[3]), 60)
    v = np.linspace(0, 2*np.pi, 60)
    U, V = np.meshgrid(u, v)

    x = U

    for i in range(len(userinput)):

        ax.plot_surface(x,(eval(userinput[i]))*np.cos(V), (eval(userinput[i]))*np.sin(V), alpha=0.3, rstride=6, cstride=12)
        #ax.plot_surface(x, Y2, Z2, alpha=0.3, color='blue', rstride=6, cstride=12)

    plt.show()