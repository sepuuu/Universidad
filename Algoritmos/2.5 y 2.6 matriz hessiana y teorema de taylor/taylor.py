from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def diff(xx, dx): #derivada
    return (f.subs(x,(xx + dx)) - f.subs(x,xx)) / dx

def taylor(xx, dx, t):
    der = diff(xx, dx)
    return f.subs(x,xx) + der * dx + (1 / 2 * dx) * diff(der + t, dx) * dx
    
x=symbols("x")
f=eval(input("Ingrese Funcion: "))
Xa=float(0.03)
Xb=float(0.02)
dx =float(0.003)
t  =float(0.001)

aTaylor = []
lamb = np.linspace(Xa, Xb, 100)

for i in lamb:
    aTaylor.append(float(taylor(i, dx, t)))

#Grafico
y=[]

for i in lamb:
    y.append(f.subs(x,i))

plt.plot(lamb, y, 'red')
plt.plot(lamb, aTaylor, 'blue')
plt.show()