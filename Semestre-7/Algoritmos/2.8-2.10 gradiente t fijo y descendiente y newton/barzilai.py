import numpy as np
import sympy
from sympy import *
import matplotlib.pyplot as plt

x = sympy.Symbol('x')
y = sympy.Symbol('y')
#himmelblaus (x**2 + -11)**2 + (x+y**2-7)**2
fBooth = (x+2*y-7)**2+(2*x+y-5)**2

funcion = fBooth #auxiliar para cambiar mas rapido de funcion

punto = Matrix([[float(2)],[float(-5)]])
et = 0.0001
df_x = sympy.diff(funcion,x) # derivadas parciales con respecto a cada variable
df_y = sympy.diff(funcion,y) 


grad = Matrix([[df_x],[df_y]]) # gradiente de cada funcion

def dinamicDescendent(punto, grad, et):
    t = 0.0001
    equis = []
    lay = []
    while(float(grad.subs([(x,punto[0]),(y,punto[1])]).norm()) >= et):
         grad1 = grad.subs([(x,punto[0]),(y,punto[1])])
         delta_x = -t*grad1
         equis.append(punto.row(0)[0]) # se guardan en arrays las coordenadas de x y de y
         lay.append(punto.row(1)[0])   # que se obtienen en cada iteración del algoritmo
         punto = punto + delta_x # se le suma el valor delta para ir variando el punto
         grad2 = grad.subs([(x,punto[0]),(y,punto[1])])
         resta = grad2 - grad1
         grad1 = grad2
         t = delta_x.dot(resta)/resta.dot(resta) # el valor de t se modifica en cada iteración
    equis.append(punto.row(0)[0]) # se guarda el punto final (la solucion)
    lay.append(punto.row(1)[0])
    return [equis,lay]

resultado = dinamicDescendent(punto, grad, et)
print = str(len(resultado[1]))
plt.title("Booth funcion")

x=np.linspace(-7,7,80)
y=np.linspace(-7,7,80)
x,y=np.meshgrid(x,y)
z = (x+2*y-7)**2+(2*x+y-5)**2
plt.contourf(x,y,z,levels=35) #las ondas de fondo
plt.contour(x,y,z,levels=[10,50,500],colors='yellow',linewidths=0.4)#lineas ovaladas de la onda
plt.plot(resultado[0],resultado[1],color='white') #muesta la ruta
a=(resultado[0][len(resultado[0])-1])
b=(resultado[1][len(resultado[1])-1])
plt.scatter(resultado[0],resultado[1],color="white") #puntos evaluados
plt.scatter(a,b,color="white") #punto final
plt.show()