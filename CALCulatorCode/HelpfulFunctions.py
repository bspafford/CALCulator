from sympy import symbols
import sympy as sp
from sympy import *
from sympy import E

def split(word):
    return [char for char in word]

#make 4*x go to 4x and 2*sin(x)*cos(x) to 2sin(x)cos(x)
def AddSigns(variable):

     signlist = []
     
     variable = split(str(variable))

     whilecounter = len(variable) + len(signlist)# - 2

     i = 0
     while i <= whilecounter:

          if len(variable) > 1 and variable[i].isdigit() and ((variable[i + 1].casefold()).islower() or variable[i + 1] == "("):
               variable.insert(i + 1, "*")
          whilecounter -= 1
          i += 1
          whilecounter = len(variable) + len(signlist) - 2

     variable = ''.join(variable)
     return variable


def ConvertExponent(variable):

    variable = str(variable).replace("^", "**")
    while variable.count("√") > 0:
          variable = variable.replace("√", "sqrt")
    while variable.count("π") > 0:
          variable = variable.replace("π", "pi")
    return variable


def RemoveAndRevert(variable):

     while str(variable).count("sqrt") > 0:
          variable = str(variable).replace("sqrt", "√")

     while str(variable).count("pi") > 0:
          variable = str(variable).replace("pi", "π")

     variable = str(variable).replace("**", "^")

     variable = split(str(variable))

     for i in range(len(variable)):
          if variable[i] == "*" and variable[i + 1].isdigit() == False and variable[i - 2] != "^":
               variable[i] = ""
               
     variable = ''.join(variable)
     return variable


def Round(variable):

     numOfDecimals = 1
     variable = N(variable)

     try:
          if variable == int(variable):
               variable = int(variable)
          else:

               firsttime = True

               for i in range(len(str(variable))):

                    if str(variable)[len(str(variable)) - 1 - i] != "0" and firsttime == True:

                         numOfDecimals = len(str(variable)) - 2 - i
                         firsttime = False

     except ValueError:
          pass

     variable = round(variable, numOfDecimals)
     return variable