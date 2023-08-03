from sympy import *
import sympy as sym
import os

y = Symbol("y")
x = Symbol("x")
#----------Funciones-------------
fBo = "(x+2*y-7)**2+(2*x+y-5)**2"
#fBeale = "(1.5 - x + x*y)**2 + (2.25 -x +x*y**2)**2+(2.625 - x + x*y**3)**2"
#--------------------------------

#----------Datos-----------------
dx1 = 0.3 #BOOTH
x1 = 0.4 #BOOTH
e1 = 0.01

#BEALE
dx2 = 0.1 
x2 = 0.4 #punto x
e2 = 0.04 #valor error
#--------------------------------

#----------Funciones-------------
def evalua_Funcion(x,f): #Funcion para evaluar
        z = eval(f) #Evalua nuestra función
        return z

def derivar_Numero(valorx,f): #Funcion para derivar
        funcion_derivada = sym.diff(f,x) #Deriva la funcion
        resultado = evalua_Funcion(valorx,str(funcion_derivada)) #Evalua la funcion derivada
        return resultado

def calcular_Delta_x(f,dx,x,e):
    def comprobar_condicion(x,dx,e):
        y = 100
        calculo = abs(derivar_Numero(x,f) - (evalua_Funcion(x+dx,f)-evalua_Funcion(x,f))/dx)
        eval_Calculo = eval(str(calculo))
        if eval_Calculo > e:
            return True
        else:
            return False       
    while (comprobar_condicion(x,dx,e)):
         dx = dx/2
    return dx
#---------------------------------


os.system("cls")
print("---------Funcion Booth---------------------")
print ("       ",derivar_Numero(x,fBo))
print("valor de delta x para la función Booth, su derivada y valor de error ",e1," : ",calcular_Delta_x(fBo,dx1,x1,e1))
print("valor de delta x para la función Booth, su derivada y valor de error ",e2," : ",calcular_Delta_x(fBo,dx2,x2,e2))

