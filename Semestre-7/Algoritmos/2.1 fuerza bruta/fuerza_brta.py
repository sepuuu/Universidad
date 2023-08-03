aValores = []
aMuestras = []
x = 0
y = 0

def funcion(x,y,T): 
    #varianza = (x**2 + -11)**2 + (x+y**2-7)**2 #himmelblaus
    #varianza = (1.5 - x + x*y)**2 + (2.25 -x +x*y**2)**2+(2.625 - x + x*y**3)**2 #beale 
    varianza = 1.2*x + 1.16*y - T*(2*x**2+y**2 +(x+y)**2)
    z = varianza

    return float(z)

T = 0.0006 #preciso 
contador = 0.01 # muestreo entre interalo 0 y 5

while x <= 5.0:
    while y <= 5.0:
        iterador  = float(contador)
        if((x + y) <= 5.0 and x >= 0 and y >= 0):
            aMuestras.append(funcion(x,y,T))
            aValores.append((x, y, funcion(x, y, T)))
            #print(aValores)
        y = y+iterador
    x = x+iterador
    y=0
#print(x)
#print(y)

muestras = aMuestras.index(max(aMuestras))  
#muestras = aMuestras.index(max(aMuestras))


m1 = (aValores[muestras][0])
m2 = (aValores[muestras][1])
m3 = str(aValores[muestras][2]) 

#print( "REPORTE (x* , f(x*)) - (", m1,  ", ",m2,"),", m3 )
print(" VALOR X1= ",m1)
print("VALOR X2= ", m2)
print("VALOR F(x)= ",m3)
#print(muestras)