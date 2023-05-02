#declaracion de arreglos y variables
aValores=[]
aMuestras=[]
x1=0
x2=0


def maxF(x1,x2,T):
    varianza= 2*x1**2+x2**2+(x1+x2)**2
    z=0.0012*x1+0.00116*x2-float(T)*(varianza)
    return z



T=input("valor de theta")
contador=input("valor de delta (recorrido de intervalo [0,5])")


while x1 <= 5.0:
    while x2 <= 5.0:
        iterador=float(contador)
        if (x1+x2)<=5.0 and x1>=0 and x2>=0:
            aMuestras.append(maxF(x1,x2,T))
            aValores.append((x1,x2,maxF(x1,x2,T)))
        x2=x2+iterador    
    x1=x1+iterador
muestras=aMuestras.index(max(aMuestras))

m1=str(aValores[muestras][0]*1000)
m2=str(aValores[muestras][1]*1000)
m3=str(aValores[muestras][2]*1000)


mx1=aValores[muestras][0]*1000
mx2=aValores[muestras][1]*1000
mx3=aValores[muestras][2]*1000

print(m1+""+m2+""+m3)
print(mx1)
print(mx2)
print(mx3)



