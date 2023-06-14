aValores = []
aMuestras = []
x = 0
y = 0

def funcion(x,y,T): 
    varianza = (x+2*y-7)**2+(2*x+y-5)**2 #booth
    #varianza = (1.5 - x + x*y)**2 + (2.25 -x +x*y**2)**2+(2.625 - x + x*y**3)**2 #beale 
    #varianza = (x - 2 )**2 schaffer
    z = 0.0012 * x + 0.00116 * y - float(T)*(varianza)

    return float(z)

T = 0.00004 #preciso 
contador = 0.1 # muestreo entre interalo 0 y 5

while x <= 5.0:
    while y <= 5.0:
        iterador  = float(contador)
        if(x + y) <= 5.0 and x >= 0 and y >= 0:
            aMuestras.append(funcion(x,y,T))
            aValores.append((x, y, funcion(x, y, T)))
        y = y+iterador
    x = x+iterador

muestras = aMuestras.index(max(aMuestras))


m1 = str(aValores[muestras][0]*1000)
m2 = str(aValores[muestras][1]*1000)
m3 = str(aValores[muestras][2]*1000) 

mX1 = aValores[muestras][0]*1000
mX2 = aValores[muestras][1]*1000
mX3 = aValores[muestras][2]*1000

print( "REPORTE (x* , f(x*)) - (", m1,  ", ",m2,"),", m3 )
print(" VALOR X1= ",mX1)
print("VALOR X2= ", mX2)
print("VALOR F(x)= ",mX3)