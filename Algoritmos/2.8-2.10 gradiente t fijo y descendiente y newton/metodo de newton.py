from ast import While, parse
from multiprocessing.managers import ValueProxy
from turtle import st
from sympy import *
import sys as s

def f(fun):
    funcion = parse_expr(fun, locals())
    return funcion
def gradiente(fun, x, valx):
    dx = diff (f(fun), x).subs({x:valx})
    return Matrix([[float(dx)]])

def mat_hessian(fun, x, valx):
    dx2 = diff(f(fun), x,2).subs({x:valx})
    return Matrix([[float(dx2)]])

x = symbols(input("ingresra nombrea para su variable: "))
funcion = input("ingresar funcion a evaluar (ej )"+str(x)+"**2+2")
valx = input("ingresar valor del elemento "+ str(x)+": ")
valueX = valx
valx = Matrix([[float(valx)]])

t = float(input("ingresar un valor para la variable t: "))
e = s.float_info.epsilon
while t < 0:
    t = float(input("ingresar un valor para la variable t: "))

xn1 = valx - ((t * mat_hessian(funcion, x, valueX).inv())* gradiente(funcion,x,valueX))

while True:
    if((gradiente(funcion,x,xn1[0]) - gradiente(funcion,x,valueX)).norm() <= e):
        print(xn1[0])
        break
    else:
        if((gradiente(funcion,x,xn1[0]).norm() < gradiente(funcion, x, valueX).norm())):
            g0 = gradiente(funcion,x,valueX).norm()
            g0p = (gradiente(funcion,x,valueX).norm()/(gradiente(funcion,x,xn1[0]) - gradiente(funcion,x,valueX)).norm())
            g1 = gradiente(funcion, x, xn1[0]).norm()

            tp = max(-g0p/(2*(g1-g0-g0p)),0,1)
            tp = Matrix([[float(1-tp)]])
            vale = xn1[0]
            xn1 = tp *valx * tp *xn1
            valueX = vale
