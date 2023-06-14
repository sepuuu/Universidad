from sympy import *
import numpy as np

def diff_x1(xx,yy, dx): 
    return (derivX1.subs([(x,(xx + dx)),(y,yy)]) - derivX1.subs([(x,xx),(y,yy)])) / dx

def diff_y(xx,yy, dx): #f"(x)/x2^2
    return (derivY.subs([(y,(xx + dx)),(x,yy)]) - derivY.subs([(y,yy),(x,xx)])) / dx

def diff_xy(xx,yy, dx): #f"(x)/x1x2
    return (derivX1.subs([(y,(xx + dx)),(x,yy)]) - derivX1.subs([(y,yy ),(x,xx)])) / dx

x,y = symbols("x,y")
f = eval(input("Ingrese Funcion: "))


derivX1= diff(f, x)
derivY= diff(f, y)

sols = solve((derivX1, derivY), (x,y)) #resuelve el sistema de ecuaciones
print ("------------------------")
print ("soluciones: ",sols)
print ("------------------------")

xx=float(eval(input("valor x: ")))
yy=float(eval(input("valor y: ")))
dx =float(input("valor dx: "))

H = (diff_x1(xx,yy, dx)*diff_y(xx,yy, dx))-(diff_xy(xx,yy, dx)**2)

if H <0:
    print ("H(X) = ",H," Por lo tanto es un punto silla")
elif H >0 and diff_x1(xx,yy, dx)<0:
    print ("H(X) = ",H," Por lo tanto es un maximo local")
elif H >0 and diff_x1(xx,yy, dx)>0:
    print ("H(X) = ",H," Por lo tanto es un minimo local")
elif H == 0:
    print ("H(X) = ",H," Por lo tanto no existe informacion suficiente")