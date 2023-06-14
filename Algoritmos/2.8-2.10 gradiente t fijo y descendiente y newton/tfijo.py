from sympy import *
from matplotlib import pyplot as plt
import numpy as np

fBooth = "(x+2*y-7)**2+(2*x+y-5)**2"
#(x**2 + -11)**2 + (x+y**2-7)**2 himmelblaus
def z_f():
    return (x+2*y-7)**2+(2*x+y-5)**2

def t(funcion):
    x,y = symbols("x,y") 
    f, t, n = eval(funcion), float(0.1), float(0.4) #evaluamos y definimos variables
    xy = Matrix([[5],[10]])
    dX1, dY2 = f.diff(x), f.diff(y) #derivamos x e y
    gradiente = Matrix([[dX1],[dY2]]) #gradiente
    xx, yy = [], []
    while(float(gradiente.subs([(x,xy[0]),(y,xy[1])]).norm()) >= n): #sustituimos valores y sacamos la normal 
         deltaXn = -gradiente.subs([(x,xy[0]),(y,xy[1])]) #sustituimos 
         xx.append(xy.row(0)[0]) #introducimos a arreglos
         yy.append(xy.row(1)[0])
         xy = xy + t*deltaXn #contador
    return [xx, yy] #retorna matriz bidimensional

plt.title("Funcion de Booth")
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
x,y=np.meshgrid(x,y)
z = z_f()
plt.contourf(x,y,z,levels=35)
plt.contour(x,y,z,levels=[10,50,500],colors='yellow',linewidths=0.4)
plt.scatter(1,3,color="white")
plt.plot(t(fBooth)[0],t(fBooth)[1],color='white')
plt.show()
