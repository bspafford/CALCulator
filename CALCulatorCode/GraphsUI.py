from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from sympy import E

# plot function is created for 
# plotting the graph in 
# tkinter window
def Graph(Yequals, Window):
    import numpy as np
    import matplotlib.pyplot as plt

    for i in range(len(Window)):
        Window[i] = eval(str(Window[i]))

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    x = np.linspace(Window[0], Window[1], 100)

    print(Yequals)

    for i in range(len(Yequals)):
            if bool(Yequals[i]):
                plt.plot(x, eval(Yequals[i]))

    plt.xlim(Window[0], Window[1])
    plt.ylim(Window[2], Window[3])

    plt.grid()

    plt.show()