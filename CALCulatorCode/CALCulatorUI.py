import tkinter
import tkinter as tk
from tkinter import *
from sympy import *
import HelpfulFunctions
import matplotlib
from sympy import E

from SolidsOfRevolutionUIGraph import SolidsOfRevolution
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from pynput.keyboard import Key, Controller

import DerivativesUI
import IntegrateUI
import TangentUI
import LimitsUI
import SolvingEquationsUI
import GraphsUI
import SolidsOfRevolutionUIGraph
import AreaofTwoFunctionsUI
import SolidsOfRevolutionUI
import CrossSectionUI
import FindDomainRangeUI
import FindAsymptotesUI
import FindmaxminUI
import CCupOrCCdownUI
import PointsOfInflectionUI
import AverageRateOfChangeUI
import FindAverageValueOfFunctionUI
import PointOfIntersectionUI

calculator=tkinter.Tk()
calculator.title("CALCulator")
calculator.geometry("350x730")
calculator.resizable(False, False)
calculator.configure(bg='black')

pixel = tk.PhotoImage(width=1, height=1)

x = symbols('x')
keyboard = Controller()

lastResultLength = 0
startValue = 1
SetWindowScreen = ["0", "10", "0", "10"]
isMath = False
isMath2 = False
isMode = False
isYequals = False
isVars = False
isWindow = False
isSecond = False
EntryNumber = 0
EntryList = []
GetTextLen = 0
CarrotButton = "^"
DivideButton = "/"
SetYequalScreen = ['','','','','','','','']
SaveYequals = "Y₁=\nY₂=\nY₃=\nY₄=\nY₅=\nY₆=\nY₇=\nY₈="
SaveWindow = "X min:0\nX max:10\nY min:0\nY max:10"

#58 35
width=53
height=30

#outputbox
OutputBox1 = tk.Text(width=16, height=8)
OutputBox1.configure(font=("Courier", 20))

OutputBox1.bind("<KeyPress>", lambda _:getrow())

OutputBox1.bind('<ButtonRelease-1>', lambda _:getrow())

OutputBox1.bind('<BackSpace>', lambda _:delete())
OutputBox1.bind('<Return>', lambda _:Solve())
OutputBox1.bind('<=>', lambda _:Solve())

OutputBox1.bind('1', lambda _:ButtonInput(1))
OutputBox1.bind('2', lambda _:ButtonInput(2))
OutputBox1.bind('3', lambda _:ButtonInput(3))
OutputBox1.bind('4', lambda _:ButtonInput(4))
OutputBox1.bind('5', lambda _:ButtonInput(5))
OutputBox1.bind('6', lambda _:ButtonInput(6))
OutputBox1.bind('7', lambda _:ButtonInput(7))
OutputBox1.bind('8', lambda _:ButtonInput(8))
OutputBox1.bind('9', lambda _:ButtonInput(9))
OutputBox1.bind('0', lambda _:ButtonInput(0))
OutputBox1.bind('<Control-Key-1>', lambda _:OutputBox1.insert("insert", "Y₁"))
OutputBox1.bind('<Control-Key-2>', lambda _:OutputBox1.insert("insert", "Y₂"))
OutputBox1.bind('<Control-Key-3>', lambda _:OutputBox1.insert("insert", "Y₃"))
OutputBox1.bind('<Control-Key-4>', lambda _:OutputBox1.insert("insert", "Y₄"))
OutputBox1.bind('<Control-Key-5>', lambda _:OutputBox1.insert("insert", "Y₅"))
OutputBox1.bind('<Control-Key-6>', lambda _:OutputBox1.insert("insert", "Y₆"))
OutputBox1.bind('<Control-Key-7>', lambda _:OutputBox1.insert("insert", "Y₇"))
OutputBox1.bind('<Control-Key-8>', lambda _:OutputBox1.insert("insert", "Y₈"))

OutputBox1.bind('<Up>', lambda _:UpArrow())
OutputBox1.bind('<Down>', lambda _:DownArrow())
OutputBox1.bind('<Left>', lambda _:LeftArrow())
OutputBox1.bind('<Right>', lambda _:RightArrow())

OutputBox1.bind('a', lambda _:ReBindA())
OutputBox1.bind('b', 'break')
OutputBox1.bind('c', lambda _:ReBindC())
OutputBox1.bind('d', 'break')
OutputBox1.bind('e', lambda _:ReBindE())
OutputBox1.bind('f', 'break')
OutputBox1.bind('g', 'break')
OutputBox1.bind('h', 'break')
OutputBox1.bind('i', lambda _:ReBindI())
OutputBox1.bind('j', 'break')
OutputBox1.bind('k', 'break')
OutputBox1.bind('l', 'break')
OutputBox1.bind('m', 'break')
OutputBox1.bind('n', 'break')
OutputBox1.bind('o', 'break')
OutputBox1.bind('p', lambda _:ReBindP())
OutputBox1.bind('q', 'break')
OutputBox1.bind('r', 'break')
OutputBox1.bind('s', lambda _:ReBindS())
OutputBox1.bind('t', lambda _:ReBindT())
OutputBox1.bind('u', 'break')
OutputBox1.bind('v', 'break')
OutputBox1.bind('w', 'break')
OutputBox1.bind('y', 'break')
OutputBox1.bind('z', 'break')
OutputBox1.bind('A', 'break')
OutputBox1.bind('B', 'break')
OutputBox1.bind('C', 'break')
OutputBox1.bind('D', 'break')
OutputBox1.bind('E', lambda _:ReBindE())
OutputBox1.bind('F', 'break')
OutputBox1.bind('G', 'break')
OutputBox1.bind('H', 'break')
OutputBox1.bind('I', lambda _:ReBindI())
OutputBox1.bind('J', 'break')
OutputBox1.bind('K', 'break')
OutputBox1.bind('L', 'break')
OutputBox1.bind('M', 'break')
OutputBox1.bind('N', 'break')
OutputBox1.bind('O', 'break')
OutputBox1.bind('P', lambda _:ReBindP())
OutputBox1.bind('Q', 'break')
OutputBox1.bind('R', 'break')
OutputBox1.bind('S', lambda _:ReBindShiftS())
OutputBox1.bind('T', 'break')
OutputBox1.bind('U', 'break')
OutputBox1.bind('V', 'break')
OutputBox1.bind('W', 'break')
OutputBox1.bind('X', 'break')
OutputBox1.bind('Y', 'break')
OutputBox1.bind('Z', 'break')
OutputBox1.bind('<Tab>', 'break')
OutputBox1.bind(':', 'break')
OutputBox1.bind(';', 'break')
OutputBox1.bind('"', 'break')
OutputBox1.bind("'", 'break')
OutputBox1.bind('{', 'break')
OutputBox1.bind('}', 'break')
OutputBox1.bind('[', 'break')
OutputBox1.bind(']', 'break')
OutputBox1.bind('\\', 'break')
#OutputBox1.bind('|', 'break')
OutputBox1.bind('<less>', 'break')
OutputBox1.bind('>', 'break')
OutputBox1.bind('?', 'break')
OutputBox1.bind('_', 'break')
OutputBox1.bind('&', 'break')
OutputBox1.bind('$', 'break')
OutputBox1.bind('#', 'break')
OutputBox1.bind('@', 'break')
OutputBox1.bind('!', 'break')
OutputBox1.bind('<space>', 'break')

TopButtonWidth = 40
TopButtonHeight = 20

#Top Buttons
buttonYeuqals = tk.Button(calculator, text="Y=", width=TopButtonWidth, height=TopButtonHeight, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:Yequals())
buttonWindow = tk.Button(calculator, text="WINDOW", width=TopButtonWidth, height=TopButtonHeight, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:window())
buttonZoom = tk.Button(calculator, text="ZOOM", width=TopButtonWidth, height=TopButtonHeight, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:zoom())
buttonCalc = tk.Button(calculator, text="CALC", width=TopButtonWidth, height=TopButtonHeight, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:calc())
buttonGraph = tk.Button(calculator, text="GRAPH", width=TopButtonWidth, height=TopButtonHeight, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:graph())


#numbers
button1 = tk.Button(calculator, text="1", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("1"))
button2 = tk.Button(calculator, text="2", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("2"))
button3 = tk.Button(calculator, text="3", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("3"))
button4 = tk.Button(calculator, text="4", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("4"))
button5 = tk.Button(calculator, text="5", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("5"))
button6 = tk.Button(calculator, text="6", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("6"))
button7 = tk.Button(calculator, text="7", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("7"))
button8 = tk.Button(calculator, text="8", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("8"))
button9 = tk.Button(calculator, text="9", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("9"))
button0 = tk.Button(calculator, text="0", width=width, height=height, image=pixel, compound="center", background='white', foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("0"))

#x
buttonX = tk.Button(calculator, text="x", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("x"))

#Trig
buttonSin = tk.Button(calculator, text="SIN", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("sin("))
buttonCos = tk.Button(calculator, text="COS", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("cos("))
buttonTan = tk.Button(calculator, text="TAN", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("tan("))

#( ) , ^ √ log ln ^-1
buttonL_parentheses = tk.Button(calculator, text="(", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("("))
buttonR_parentheses = tk.Button(calculator, text=")", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput(")"))
buttonComma = tk.Button(calculator, text=",", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput(","))
buttonCarrot = tk.Button(calculator, text="^", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput(CarrotButton))
buttonSqrt = tk.Button(calculator, text="√", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("√("))
buttonLog = tk.Button(calculator, text="LOG", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("log("))
buttonLn = tk.Button(calculator, text="LN", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("ln("))
buttonUpNeg1 = tk.Button(calculator, text="x^-1", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("^-1"))

#Operator Buttons
buttonAdd = tk.Button(calculator, text="+", width=width, height=height, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("+"))
buttonSubtract = tk.Button(calculator, text="-", width=width, height=height, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("-"))
buttonMultiply = tk.Button(calculator, text="*", width=width, height=height, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("*"))
buttonDivide = tk.Button(calculator, text="/", width=width, height=height, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput(DivideButton))
buttonDecimal = tk.Button(calculator, text=".", width=width, height=height, image=pixel, compound="center", background="white", foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("."))
buttonNegative = tk.Button(calculator, text="( - )", width=width, height=height, image=pixel, compound="center", background="white", foreground='#0B0B0B', relief = GROOVE, padx=0, pady=0, command=lambda:ButtonInput("-"))
buttonEqual = tk.Button(calculator, text="ENTER", width=width, height=height, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:Solve())

#Math Mode Vars 2nd Alpha
buttonMath = tk.Button(calculator, text="MATH", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:Math())
buttonMode = tk.Button(calculator, text="MODE", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:Mode())
buttonVars = tk.Button(calculator, text="VARS", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:Vars())
button2nd = tk.Button(calculator, text="2nd", width=width, height=height, image=pixel, compound="center", background="#DABE33", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:second())
buttonAlpha = tk.Button(calculator, text="ALPHA", width=width, height=height, image=pixel, compound="center", background="#2DC460", foreground='white', relief = GROOVE, padx=0, pady=0)#, command=lambda:Alpha())
buttonMath2 = tk.Button(calculator, text="MATH 2", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:Math2())
buttonBlank = tk.Button(calculator, text="INT", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:ReBindI())
buttonBlank2 = tk.Button(calculator, text="", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0)
buttonOn = tk.Button(calculator, text="ON", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, padx=0, pady=0)

#Delete Buttons
buttondel = tk.Button(calculator, text="DEL", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, command=lambda:delete())
buttonclear = tk.Button(calculator, text="CLEAR", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, command=lambda:clear())
buttonQuit = tk.Button(calculator, text="QUIT", width=width, height=height, image=pixel, compound="center", background="#0B0B0B", foreground='white', relief = GROOVE, command=lambda:Quit())

ArrowWidth = 40
ArrowHeight = 25

#Arrow Keys
buttonUp = tk.Button(calculator, text="↑", width=ArrowWidth, height=ArrowHeight, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:UpArrow())
buttonDown = tk.Button(calculator, text="↓", width=ArrowWidth, height=ArrowHeight, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:DownArrow())
buttonLeft = tk.Button(calculator, text="←", width=ArrowHeight, height=ArrowWidth, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:LeftArrow())
buttonRight = tk.Button(calculator, text="→", width=ArrowHeight, height=ArrowWidth, image=pixel, compound="center", background="#334FDA", foreground='white', relief = GROOVE, padx=0, pady=0, command=lambda:RightArrow())

Xpad = 5
Ypad = 5


#outputbox
OutputBox1.grid(row=1, rowspan=8, column=1, columnspan=5, pady=10)

#Top Buttons
buttonYeuqals.grid(row=9, column=1, padx=0, pady=9)
buttonWindow.grid(row=9, column=2, padx=0, pady=9)
buttonZoom.grid(row=9, column=3, padx=0, pady=9)
buttonCalc.grid(row=9, column=4, padx=0, pady=9)
buttonGraph.grid(row=9, column=5, padx=0, pady=9)


#numbers
button1.grid(row=17, column=2, padx=Xpad, pady=Ypad)
button2.grid(row=17, column=3, padx=Xpad, pady=Ypad)
button3.grid(row=17, column=4, padx=Xpad, pady=Ypad)
button4.grid(row=16, column=2, padx=Xpad, pady=Ypad)
button5.grid(row=16, column=3, padx=Xpad, pady=Ypad)
button6.grid(row=16, column=4, padx=Xpad, pady=Ypad)
button7.grid(row=15, column=2, padx=Xpad, pady=Ypad)
button8.grid(row=15, column=3, padx=Xpad, pady=Ypad)
button9.grid(row=15, column=4, padx=Xpad, pady=Ypad)
button0.grid(row=18, column=2, padx=Xpad, pady=Ypad)

#x
buttonX.grid(row=11, column=2, padx=Xpad, pady=Ypad)

#Trig
buttonSin.grid(row=13, column=2, padx=Xpad, pady=Ypad)
buttonCos.grid(row=13, column=3, padx=Xpad, pady=Ypad)
buttonTan.grid(row=13, column=4, padx=Xpad, pady=Ypad)

#( ) , ^ √ log ln ^-1
buttonL_parentheses.grid(row=14, column=3, padx=Xpad, pady=Ypad)
buttonR_parentheses.grid(row=14, column=4, padx=Xpad, pady=Ypad)
buttonComma.grid(row=14, column=2, padx=Xpad, pady=Ypad)
buttonCarrot.grid(row=13, column=5, padx=Xpad, pady=Ypad)
buttonSqrt.grid(row=14, column=1, padx=Xpad, pady=Ypad)
buttonLog.grid(row=15, column=1, padx=Xpad, pady=Ypad)
buttonLn.grid(row=16, column=1, padx=Xpad, pady=Ypad)
buttonUpNeg1.grid(row=13, column=1, padx=Xpad, pady=Ypad)

#Operator Buttons
buttonAdd.grid(row=17, column=5, padx=Xpad, pady=Ypad)
buttonSubtract.grid(row=16, column=5, padx=Xpad, pady=Ypad)
buttonMultiply.grid(row=15, column=5, padx=Xpad, pady=Ypad)
buttonDivide.grid(row=14, column=5, padx=Xpad, pady=Ypad)
buttonDecimal.grid(row=18, column=3, padx=Xpad, pady=Ypad)
buttonNegative.grid(row=18, column=4, padx=Xpad, pady=Ypad)
buttonEqual.grid(row=18, column=5, padx=Xpad, pady=Ypad)

#Math Mode Vars 2nd Alpha
buttonMath.grid(row=12, column=1, padx=Xpad, pady=Ypad)
buttonMode.grid(row=10, column=2, padx=Xpad, pady=Ypad)
buttonVars.grid(row=12, column=4, padx=Xpad, pady=Ypad)
button2nd.grid(row=10, column=1, padx=Xpad, pady=Ypad)
buttonAlpha.grid(row=11, column=1, padx=Xpad, pady=Ypad)
buttonMath2.grid(row=12, column=2, padx=Xpad, pady=Ypad)
buttonBlank.grid(row=12, column=3, padx=Xpad, pady=Ypad)
buttonBlank2.grid(row=17, column=1, padx=Xpad, pady=Ypad)
buttonOn.grid(row=18, column=1, padx=Xpad, pady=Ypad)

#Delete Buttons
buttonclear.grid(row=12, column=5, padx=Xpad, pady=Ypad)
buttondel.grid(row=10, column=3, padx=Xpad, pady=Ypad)
buttonQuit.grid(row=11, column=3, padx=Xpad, pady=Ypad)

#Arrow Keys
buttonUp.place(x=255, y=310)
buttonDown.place(x=255, y=360)
buttonLeft.place(x=220, y=330)
buttonRight.place(x=305, y=330)

def RebindNumKeys(Num):

    global isYequals
    global isWindow
    global InsertionPoint
    
    getrow()

def ReBindA():

    global isMath
    global isMath2
    global isMode
    global isVars
    global isWindow
    global isYequals

    if isMath == False and isMath2 == False and isMode == False and isVars == False and isWindow == False:

        OutputBox1.insert("insert", "abs(")
    return 'break'

def ReBindI():

    global isMath
    global isMath2
    global isMode
    global isVars
    global isWindow
    global isYequals

    if isMath == False and isMath2 == False and isMode == False and isVars == False and isWindow == False and isYequals == False:

        OutputBox1.insert("insert", "int")
    return 'break'

def ReBindP():

    global isMath
    global isMath2
    global isMode
    global isVars
    global isWindow
    global isYequals

    if isMath == False and isMath2 == False and isMode == False and isVars == False:

        OutputBox1.insert("insert", "π")
    return 'break'

def ReBindS():

    global isMath
    global isMath2
    global isMode
    global isVars
    global isWindow
    global isYequals

    if isMath == False and isMath2 == False and isMode == False and isVars == False:

        OutputBox1.insert("insert", "sin(")
    return 'break'

def ReBindShiftS():

    global isMath
    global isMath2
    global isMode
    global isVars
    global isWindow
    global isYequals

    if isMath == False and isMath2 == False and isMode == False and isVars == False:

        OutputBox1.insert("insert", "√(")
    return 'break'

def ReBindC():

    global isMath
    global isMath2
    global isMode
    global isVars
    global isWindow
    global isYequals

    if isMath == False and isMath2 == False and isMode == False and isVars == False:

        OutputBox1.insert("insert", "cos(")
    return 'break'

def ReBindT():

    global isMath
    global isMath2
    global isMode
    global isVars
    global isWindow
    global isYequals

    if isMath == False and isMath2 == False and isMode == False and isVars == False:

        OutputBox1.insert("insert", "tan(")
    return 'break'

def ReBindE():

    global isMath
    global isMath2
    global isMode
    global isVars
    global isWindow
    global isYequals

    if isMath == False and isMath2 == False and isMode == False and isVars == False:

        OutputBox1.insert("insert", "E")
    return 'break'

def ButtonInput(input):

    global isMath
    global isVars
    #OutputBox1.tag_configure("left", justify="left")
    #OutputBox1.tag_add("left", "1.0", "end")

    global InsertionPoint
    global isYequals
    global isMath2
    global isMode
    global isVars
    global isWindow

    input = str(input)

    if isYequals == True and (InsertionPoint[1] != "0" and InsertionPoint[1] != "1" and InsertionPoint[1] != "2"):

        OutputBox1.insert("insert", input)
        getrow()

    elif isWindow == True and (InsertionPoint[1] != "0" and InsertionPoint[1] != "1" and InsertionPoint[1] != "2" and InsertionPoint[1] != "3" and InsertionPoint[1] != "4" and InsertionPoint[1] != "5"):

        OutputBox1.insert("insert", input)
        getrow()

    elif isYequals == False and isWindow == False and isMode == False and isVars == False and isMath == False and isMath2 == False:

        OutputBox1.insert("insert", input)
        getrow()

    #if isMath == False and isMath2 == False and isMode == False and isVars == False:
        #OutputBox1.insert("insert", input)
        
    elif isMath == True:

        if input == "1":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Subs(")
            isMath = False

        elif input == "2":
            
            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "nDeriv(")
            isMath = False

        elif input == "3":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "fnInt(")
            isMath = False

        elif input == "4":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "tangent(")
            isMath = False

        elif input == "5":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "lim(")
            isMath = False

        elif input == "6":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Area(")
            isMath = False

        elif input == "7":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Vol(")
            isMath = False

        elif input == "8":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Cross(")
            isMath = False

    elif isMath2 == True:
        
        if input == "1":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "DaR(")
            isMath2 = False
            

        elif input == "2":
            
            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Asym(")
            isMath2 = False

        elif input == "3":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "MinMax(")
            isMath2 = False

        elif input == "4":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Find CCs(")
            isMath2 = False

        elif input == "5":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Inflection(")
            isMath2 = False

        elif input == "6":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "AvgChange(")
            isMath2 = False

        elif input == "7":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "AvgFunction(")
            isMath2 = False

        elif input == "8":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Intersect(")
            isMath2 = False

    elif isVars == True:

        if input == "1":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Y₁")
            isVars = False

        elif input == "2":
            
            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Y₂")
            isVars = False

        elif input == "3":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Y₃")
            isVars = False

        elif input == "4":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Y₄")
            isVars = False

        elif input == "5":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Y₅")
            isVars = False

        elif input == "6":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Y₆")
            isVars = False

        elif input == "7":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Y₇")
            isVars = False

        elif input == "8":

            OutputBox1.delete("1.0", "end-1c")
            OutputBox1.insert("1.0", SaveText)
            OutputBox1.insert("end-1c", "Y₈")
            isVars = False

    getrow()
    return 'break'

def UpArrow():

    RepeatArrow = 0

    PreArrow = InsertionPoint

    while int(InsertionPoint[0]) == int(PreArrow[0]) and RepeatArrow != InsertionPoint:

        RepeatArrow = InsertionPoint

        OutputBox1.mark_set("insert", "insert-1c")
        getrow()

    return 'break'

def DownArrow():

    RepeatArrow = 0

    PreArrow = InsertionPoint

    while (int(InsertionPoint[0]) == int(PreArrow[0]) or int(InsertionPoint[0]) == int(PreArrow[0]) + 1) and RepeatArrow != InsertionPoint:

        RepeatArrow = InsertionPoint

        OutputBox1.mark_set("insert", "insert+1c")
        getrow()

    if RepeatArrow != InsertionPoint:

        OutputBox1.mark_set("insert", "insert-1c")
        getrow()

    return 'break'

def LeftArrow():

    OutputBox1.mark_set("insert", "insert-1c")

    YnumList = ["₀","₁","₂","₃","₄","₅","₆","₇"]

    for i in range(8):

        if OutputBox1.get("insert-1c", "insert+1c") == f"Y{YnumList[i]}":

            OutputBox1.mark_set("insert", "insert-1c")
            getrow()
            return 'break'

    GetMoveLengthLeft("Subs")
    GetMoveLengthLeft("nDeriv")
    GetMoveLengthLeft("fnInt")
    GetMoveLengthLeft("tangent")
    GetMoveLengthLeft("lim")
    GetMoveLengthLeft("Area")
    GetMoveLengthLeft("Vol")
    GetMoveLengthLeft("Cross")
    GetMoveLengthLeft("DaR")
    GetMoveLengthLeft("Asym")
    GetMoveLengthLeft("MinMax")
    GetMoveLengthLeft("Find CCs")
    GetMoveLengthLeft("Inflection")
    GetMoveLengthLeft("AvgChange")
    GetMoveLengthLeft("AvgFunction")
    GetMoveLengthLeft("Intersect")
    GetMoveLengthLeft("sin")
    GetMoveLengthLeft("cos")
    GetMoveLengthLeft("tan")
    GetMoveLengthLeft("in")
    GetMoveLengthLeft("abs")

    getrow()
    return 'break'


def RightArrow():

    OutputBox1.mark_set("insert", "insert+1c")

    YnumList = ["₀","₁","₂","₃","₄","₅","₆","₇"]

    for i in range(8):

        if OutputBox1.get("insert-1c", "insert+1c") == f"Y{YnumList[i]}":

            OutputBox1.mark_set("insert", "insert+1c")
            getrow()
            return 'break'

    GetMoveLengthRight("Subs(")
    GetMoveLengthRight("nDeriv(")
    GetMoveLengthRight("fnInt(")
    GetMoveLengthRight("tangent(")
    GetMoveLengthRight("lim(")
    GetMoveLengthRight("Area(")
    GetMoveLengthRight("Vol(")
    GetMoveLengthRight("Cross(")
    GetMoveLengthRight("DaR(")
    GetMoveLengthRight("Asym(")
    GetMoveLengthRight("MinMax(")
    GetMoveLengthRight("Find CCs(")
    GetMoveLengthRight("Inflection(")
    GetMoveLengthRight("AvgChange(")
    GetMoveLengthRight("AvgFunction(")
    GetMoveLengthRight("Intersect(")
    GetMoveLengthRight("sin(")
    GetMoveLengthRight("cos(")
    GetMoveLengthRight("tan(")
    GetMoveLengthRight("int")
    GetMoveLengthRight("abs(")

    getrow()
    return 'break'


def GetMoveLengthLeft(Variable):

    Length = len(split(Variable))

    if OutputBox1.get(f"insert-{Length}c", "insert") == f"{Variable}":

        OutputBox1.mark_set("insert", f"insert-{Length}c")
        getrow()
        return 'break'


def GetMoveLengthRight(Variable):

    Length = len(split(Variable))

    if OutputBox1.get("insert-1c", f"insert+{Length-1}c") == f"{Variable}":

            

            OutputBox1.mark_set("insert", f"insert+{Length-1}c")
            getrow()
            return 'break'


def Math():

    global SaveText
    global SaveYequals
    global isMath
    global isMode
    global isYequals
    global isVars
    global isWindow
    global SaveWindow
    global isMath2

    if isMath == False and isMath2 == False and isMode == False and isYequals == False and isVars == False and isWindow == False:
        SaveText = OutputBox1.get("1.0", "end-1c")

    if isYequals == True:

        SetYEquals()
        SaveYequals = OutputBox1.get("1.0", "end-1c")

    if isWindow == True:

        SetWindow()
        SaveWindow = OutputBox1.get("1.0", "end-1c")

    isMath = not isMath
    
    if isMath == True:
        
        isMath2 = False
        isMode = False
        isYequals = False
        isVars = False
        isWindow = False
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", "1)Substitute\n2)Derivative\n3)Integrals\n4)Tangent\n5)Lim\n6)Area of 2 F(x)\n7)Vol of 2 f(x)\n8)Cross Section")

    elif isMath == False:
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", SaveText)

def Math2():

    global SaveText
    global SaveYequals
    global isMath
    global isMode
    global isYequals
    global isVars
    global isWindow
    global SaveWindow
    global isMath2

    if isMath == False and isMath2 == False and isMode == False and isYequals == False and isVars == False and isWindow == False:
        SaveText = OutputBox1.get("1.0", "end-1c")

    if isYequals == True:

        SetYEquals()
        SaveYequals = OutputBox1.get("1.0", "end-1c")

    if isWindow == True:

        SetWindow()
        SaveWindow = OutputBox1.get("1.0", "end-1c")

    isMath2 = not isMath2
    
    if isMath2 == True:
        
        isMath = False
        isMode = False
        isYequals = False
        isVars = False
        isWindow = False
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", "1)Domain n Range\n2)Asymptotes\n3)Min and Max\n4)Change in CC\n5)Inflection\n6)Avg r8 change\n7)Avg Function\n8)Intersections")

    elif isMath2 == False:
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", SaveText)

def Mode():

    global SaveText
    global SaveYequals
    global isMode
    global isMath
    global isYequals
    global isVars
    global isWindow
    global SaveWindow
    global isMath2

    if isMath == False and isMath2 == False and isMode == False and isYequals == False and isVars == False and isWindow == False:
        SaveText = OutputBox1.get("1.0", "end-1c")

    if isYequals == True:

        SetYEquals()
        SaveYequals = OutputBox1.get("1.0", "end-1c")

    if isWindow == True:

        SetWindow()
        SaveWindow = OutputBox1.get("1.0", "end-1c")

    isMode = not isMode

    if isMode == True:

        isMath = False
        isMath2 = False
        isYequals = False
        isVars = False
        isWindow = False
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", "ALWAYS IN \nRADIANS, NEVER \nUSE DEGREES!!!")
        
    else:
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", SaveText)

def Vars():

    global isVars
    global SaveText
    global SaveYequals
    global isMath
    global isMode
    global isYequals
    global isWindow
    global SaveWindow
    global isMath2

    if isMath == False and isMath2 == False and isMode == False and isYequals == False and isVars == False and isWindow == False:
        SaveText = OutputBox1.get("1.0", "end-1c")

    if isYequals == True:

        SetYEquals()
        SaveYequals = OutputBox1.get("1.0", "end-1c")

    if isWindow == True:

        SetWindow()
        SaveWindow = OutputBox1.get("1.0", "end-1c")

    isVars = not isVars
    
    if isVars == True:
        
        isMode = False
        isMath = False
        isMath2 = False
        isYequals = False
        isWindow = False
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", "1) Y₁\n2) Y₂\n3) Y₃\n4) Y₄\n5) Y₅\n6) Y₆\n7) Y₇\n8) Y₈")

    elif isVars == False:
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", SaveText)

def second():

    global isSecond
    global CarrotButton
    global DivideButton

    isSecond = not isSecond

    if isSecond == True:

        buttonCarrot.configure(text="π", background='#DABE33')
        CarrotButton = "π"
        buttonGraph.configure(text="3D Graph", background='#DABE33')
        buttonEqual.configure(text="ENTRY", background='#DABE33')
        buttonDivide.configure(text="e", background='#DABE33')
        DivideButton = "E"

    else:

        buttonGraph.configure(text="Graph", background='#334FDA')
        CarrotButton = "^"
        buttonEqual.configure(text="ENTER", background='#334FDA')
        buttonCarrot.configure(text="^", background='#334FDA')
        buttonDivide.configure(text="/", background='#334FDA')
        DivideButton = "/"


def Solve():

    global isSecond
    global EntryNumber
    global EntryList
    global lastResultLength
    global startValue
    global GetTextLen

    if isSecond == True and len(EntryList) > EntryNumber:

        EntryNumber += 1
        OutputBox1.delete(f'end-{len(OutputBox1.get("1.0", "end-1c")) - GetTextLen + 1}c', "end-1c")
        OutputBox1.insert("end-1c", EntryList[len(EntryList) - EntryNumber])

    elif isSecond == False:

        if isMath == False and isMath2 == False and isMode == False and isYequals == False and isVars == False and isWindow == False:
            
            startValue = len(OutputBox1.get("1.0", "end-1c")) - lastResultLength + 1

            if bool(OutputBox1.get(f'end-{startValue}c', "end-1c")):

                EntryList.append(OutputBox1.get(f'end-{startValue}c', "end-1c"))

                WhatToDo = OutputBox1.get(f'end-{startValue}c', "end-1c")
                WhatToDo = WhatToDo.split("(")

                if WhatToDo[0] == "Subs":

                    InputText = PreSolve()
                    InputText = InputText.replace("Subs(", "")
                    InputText = replaceY(InputText)
                    answer = SolvingEquationsUI.SolvingEquations(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "nDeriv":
                
                    InputText = PreSolve()
                    InputText = InputText.replace("nDeriv(", "")
                    InputText = replaceY(InputText)
                    answer = DerivativesUI.Derivatives(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "fnInt":

                    InputText = PreSolve()
                    InputText = InputText.replace("fnInt(", "")
                    InputText = replaceY(InputText)
                    answer = IntegrateUI.Integrate(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "tangent":

                    InputText = PreSolve()
                    InputText = InputText.replace("tangent(", "")
                    InputText = replaceY(InputText)
                    answer = TangentUI.Tangent(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "lim":

                    InputText = PreSolve()
                    InputText = InputText.replace("lim(", "")
                    InputText = replaceY(InputText)
                    answer = LimitsUI.Limits(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "Area":

                    InputText = PreSolve()
                    InputText = InputText.replace("Area(", "")
                    InputText = replaceY(InputText)
                    answer = AreaofTwoFunctionsUI.AreaofTwoFunctions(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "Vol":

                    InputText = PreSolve()
                    InputText = InputText.replace("Vol(", "")
                    InputText = replaceY(InputText)
                    answer = SolidsOfRevolutionUI.SolidsOfRevolution(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "Cross":

                    InputText = PreSolve()
                    InputText = InputText.replace("Cross(", "")
                    InputText = replaceY(InputText)
                    answer = CrossSectionUI.CrossSection(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "DaR":

                    InputText = PreSolve()
                    InputText = InputText.replace("DaR(", "")
                    InputText = replaceY(InputText)
                    answer = FindDomainRangeUI.FindDomainRange(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "Asym":

                    InputText = PreSolve()
                    InputText = InputText.replace("Asym(", "")
                    InputText = replaceY(InputText)
                    answer = FindAsymptotesUI.FindAsymptotes(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "MinMax":

                    InputText = PreSolve()
                    InputText = InputText.replace("MinMax(", "")
                    InputText = replaceY(InputText)
                    answer = FindmaxminUI.Findmaxmin(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "Find CCs":

                    InputText = PreSolve()
                    InputText = InputText.replace("Find CCs(", "")
                    InputText = replaceY(InputText)
                    answer = CCupOrCCdownUI.CCupOrCCdown(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "Inflection":

                    InputText = PreSolve()
                    InputText = InputText.replace("Inflection(", "")
                    InputText = replaceY(InputText)
                    answer = PointsOfInflectionUI.PointsOfInflection(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "AvgChange":

                    InputText = PreSolve()
                    InputText = InputText.replace("AvgChange(", "")
                    InputText = replaceY(InputText)
                    answer = AverageRateOfChangeUI.AverageRateOfChange(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "AvgFunction":

                    InputText = PreSolve()
                    InputText = InputText.replace("AvgFunction(", "")
                    InputText = replaceY(InputText)
                    answer = FindAverageValueOfFunctionUI.FindAverageValueOfFunction(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                elif WhatToDo[0] == "Intersect":

                    InputText = PreSolve()
                    InputText = InputText.replace("Intersect(", "")
                    InputText = replaceY(InputText)
                    answer = PointOfIntersectionUI.PointOfIntersection(InputText)
                    OutputBox1.insert("end-1c", f'\n{answer}\n')

                else:
                    
                    result = OutputBox1.get(f'end-{startValue}c', "end-1c")
                    result = HelpfulFunctions.ConvertExponent(result)
                    result = eval(result)
                    result = HelpfulFunctions.Round(result)
                    OutputBox1.insert("end-1c", f'\n{result}\n')
                EntryNumber = 0
                GetTextLen = len(OutputBox1.get("1.0", "end-1c"))
                lastResultLength = len(OutputBox1.get("1.0", "end-1c"))
    return 'break'

def PreSolve ():

    InputText = HelpfulFunctions.AddSigns(OutputBox1.get(f'end-{startValue}c', "end-1c"))
    if InputText.count("(") == InputText.count(")"):
        InputText = split(InputText)
        InputText.pop(-1)
        InputText = ''.join(InputText)

    return InputText

def Yequals():

    global SaveText
    global SaveYequals
    global isMath
    global isMode
    global isYequals
    global isVars
    global isWindow
    global SaveWindow
    global isMath2

    if isMath == False and isMath2 == False and isMode == False and isYequals == False and isVars == False and isWindow == False:
        SaveText = OutputBox1.get("1.0", "end-1c")

#could put this in the else: on line 460 instead
    if isYequals == True:

        SetYEquals()
        SaveYequals = OutputBox1.get("1.0", "end-1c")

    if isWindow == True:

        SetWindow()
        SaveWindow = OutputBox1.get("1.0", "end-1c")

    isYequals = not isYequals

    if isYequals == True:

        isMode = False
        isMath = False
        isMath2 = False
        isVars = False
        isWindow = False
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", SaveYequals)

    else:
        SetYEquals()
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", SaveText)


def SetYEquals():

    global SetYequalScreen
    SetYequalScreen = OutputBox1.get("1.0", "end-1c")
    SetYequalScreen = SetYequalScreen.split("Y")

    SetYequalScreen.pop(0)
    
    for i in range(len(SetYequalScreen)):

        SetYequalScreen[i] = SetYequalScreen[i].replace("\n", "")

    SetYequalScreen[0] = SetYequalScreen[0].replace('₁=', "")
    SetYequalScreen[1] = SetYequalScreen[1].replace('₂=', "")
    SetYequalScreen[2] = SetYequalScreen[2].replace('₃=', "")
    SetYequalScreen[3] = SetYequalScreen[3].replace('₄=', "")
    SetYequalScreen[4] = SetYequalScreen[4].replace('₅=', "")
    SetYequalScreen[5] = SetYequalScreen[5].replace('₆=', "")
    SetYequalScreen[6] = SetYequalScreen[6].replace('₇=', "")
    SetYequalScreen[7] = SetYequalScreen[7].replace('₈=', "")


def SetWindow():

    global SetWindowScreen

    SetWindowScreen = OutputBox1.get("1.0", "end-1c")
    SetWindowScreen = SetWindowScreen.split(":")

    SetWindowScreen.pop(0)

    for i in range(len(SetWindowScreen)):

        SetWindowScreen[i] = SetWindowScreen[i].replace("\n", "")
        
    SetWindowScreen[0] = SetWindowScreen[0].replace('X max', "")
    SetWindowScreen[1] = SetWindowScreen[1].replace('Y min', "")
    SetWindowScreen[2] = SetWindowScreen[2].replace('Y max', "")

    for i in range(len(SetWindowScreen)):

        SetWindowScreen[i] = HelpfulFunctions.ConvertExponent(SetWindowScreen[i])
        SetWindowScreen[i] = HelpfulFunctions.AddSigns(SetWindowScreen[i])
        

def replaceY(Input):

    global SetYequalScreen

    Input = str(Input)

    Input = Input.replace('Y₁', f'{SetYequalScreen[0]}')
    Input = Input.replace('Y₂', f'{SetYequalScreen[1]}')
    Input = Input.replace('Y₃', f'{SetYequalScreen[2]}')
    Input = Input.replace('Y₄', f'{SetYequalScreen[3]}')
    Input = Input.replace('Y₅', f'{SetYequalScreen[4]}')
    Input = Input.replace('Y₆', f'{SetYequalScreen[5]}')
    Input = Input.replace('Y₇', f'{SetYequalScreen[6]}')
    Input = Input.replace('Y₈', f'{SetYequalScreen[7]}')

    return Input

def window():

    global SaveWindow
    global isWindow
    global SaveText
    global SaveYequals
    global isMath
    global isMode
    global isYequals
    global isVars
    global isMath2

    if isMath == False and isMath2 == False and isMode == False and isYequals == False and isVars == False and isWindow == False:
        SaveText = OutputBox1.get("1.0", "end-1c")

#could put this in the else: on line 460 instead
    if isYequals == True:

        SetYEquals()
        SaveYequals = OutputBox1.get("1.0", "end-1c")

    if isWindow == True:

        SetWindow()
        SaveWindow = OutputBox1.get("1.0", "end-1c")

    isWindow = not isWindow

    if isWindow == True:

        isMode = False
        isMath = False
        isYequals = False
        isVars = False
        isMath2 = False
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", SaveWindow)

    else:
        SetWindow()
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", SaveText)


def zoom():

    print("zoom")

def calc():

    print("calc")

def graph():

    global isYequals
    global SetWindowScreen

    if isYequals == True:

        SetYEquals()

    if isWindow == True:

        SetWindow()

    global SetYequalScreen

    for i in range(len(SetYequalScreen)):
        SetYequalScreen[i] = HelpfulFunctions.AddSigns(SetYequalScreen[i])
        SetYequalScreen[i] = HelpfulFunctions.ConvertExponent(SetYequalScreen[i])

    if isSecond == False:

        GraphsUI.Graph(SetYequalScreen, SetWindowScreen)

    elif isSecond == True:

        SolidsOfRevolutionUIGraph.SolidsOfRevolution(SetYequalScreen, SetWindowScreen)

def Quit():

    global isMode
    global isMath
    global isYequals
    global SaveYequals
    global isVars
    global isMath2
    global isWindow

    if isYequals == True:

        SetYEquals()
        SaveYequals = OutputBox1.get("1.0", "end-1c")

    if isMode == True or isMath == True or isMath2 == True or isYequals == True or isVars == True or isWindow == True:

        isMode = False
        isMath = False
        isYequals = False
        isVars = False
        isMath2 = False
        isWindow = False
        OutputBox1.delete("1.0", "end-1c")
        OutputBox1.insert("1.0", SaveText)
        

def clear():

    if isMode == False and isMath == False and isMath2 == False and isYequals == False and isVars == False and isWindow == False:

        global lastResultLength
        lastResultLength = 0
        OutputBox1.delete("1.0", "end")

def delete():
    # add the overstrike to the character before the
    # insertion cursor
    global InsertionPoint
    global isYequals
    global isMath
    global isMode
    global isVars
    global isWindow
    global isMath2

    getrow()

    if isMath == True or isMath2 == True or isMode == True or isVars == True:

        pass
    
    elif isYequals == True and (InsertionPoint[1] != "0" and InsertionPoint[1] != "1" and InsertionPoint[1] != "2" and InsertionPoint[1] != "3"):

        OutputBox1.tag_add("", "insert-1c", "insert")
        OutputBox1.delete("insert-1c")
        test()

    elif isWindow == True and (InsertionPoint[1] != "0" and InsertionPoint[1] != "1" and InsertionPoint[1] != "2" and InsertionPoint[1] != "3" and InsertionPoint[1] != "4" and InsertionPoint[1] != "5" and InsertionPoint[1] != "6"):

        OutputBox1.tag_add("", "insert-1c", "insert")
        OutputBox1.delete("insert-1c")
        test()

    elif isYequals == False and isMath == False and isMath2 == False and isMode == False and isVars == False and isWindow == False:

        OutputBox1.tag_add("", "insert-1c", "insert")
        OutputBox1.delete("insert-1c")
        test()

    return "break"

def test():

    YnumList = ["₀","₁","₂","₃","₄","₅","₆","₇"]

    for i in range(8):

        if OutputBox1.get("insert-1c", "insert+1c") == f"Y{YnumList[i]}":

            OutputBox1.mark_set("insert", "insert-1c")
            getrow()
            return 'break'

    GetDeleteLength("Subs")
    GetDeleteLength("nDeriv")
    GetDeleteLength("fnInt")
    GetDeleteLength("tangent")
    GetDeleteLength("lim")
    GetDeleteLength("Area")
    GetDeleteLength("Vol")
    GetDeleteLength("Cross")
    GetDeleteLength("DaR")
    GetDeleteLength("Asym")
    GetDeleteLength("MinMax")
    GetDeleteLength("Find CCs")
    GetDeleteLength("Inflection")
    GetDeleteLength("AvgChange")
    GetDeleteLength("AvgFunction")
    GetDeleteLength("Intersect")
    GetDeleteLength("sin")
    GetDeleteLength("cos")
    GetDeleteLength("tan")
    GetDeleteLength("in")
    GetDeleteLength("abs")

    getrow()
    return 'break'


def GetDeleteLength(Variable):

    Length = len(split(Variable))

    if OutputBox1.get(f"insert-{Length}c", "insert") == Variable:

        OutputBox1.delete(f"insert-{Length}c", "insert")
        getrow()
        return 'break'


def getrow():

    global InsertionPoint
    index = OutputBox1.index(INSERT)
    InsertionPoint = index.split(".")

def check_pos():
    index = OutputBox1.index(tk.INSERT)
    index = index.split(".")

def split(word):
    return [char for char in word]

calculator.mainloop()