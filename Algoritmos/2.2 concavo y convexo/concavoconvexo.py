import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import sympy

fBooth = "(x+2*y-7)**2+(2*x+y-5)**2" 
#fBeale = "(1.5 - x + x*y)**2 + (2.25 -x +x*y**2)**2+(2.625 - x + x*y**3)**2"
x = Symbol('x') 
y = Symbol('y')

def derivar(f,cual):
    f_derivada = sympy.diff(f,cual)
    resultado = eval(str(f_derivada))
    return str(resultado)

def hessiano(fun):
    fx = derivar(fun,x)
    fy = derivar(fun,y)
    fxx = derivar(fx,x)
    fyy = derivar(fy,y)
    fxy = derivar(fx,y)
    fyx = derivar(fy,x)
    return [eval(fxx),eval(fxy),eval(fyx),eval(fyy)]

def determinante(fun):
    D = hessiano(fun)
    D1 = D[0]
    D2 = (D[0]*D[3])-(D[1]*D[2])
    return [float(D1),float(D2)] #par ordenado

def convexo_concavo(fun,n): 
    valores = determinante(fun)
    if (valores[0] < 0.0 and valores[1] >= 0.0):
        return "La funcion "+n+" es concava"
    if (valores[0] > 0.0 and valores[1] >= 0.0):
        return "La funcion "+n+" es convexa" 
    else:
        return "La funcion "+n+" no es concava ni convexa, es indeteterminable"

print(convexo_concavo(fBooth,"Booth"))
