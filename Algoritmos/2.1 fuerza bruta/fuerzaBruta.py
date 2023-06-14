#CODIGO DE BRANCO
from operator import itemgetter
fBooth = "(x+2*y-7)**2+(2*x+y-5)**2"
fMatyas = "((26/100)*(x**2+y**2))-((48/100)*x*y)"

def fuerzaBruta(funcion,nombre):
   x = y = x = 0
   resultado = []
   for x in range(-10,11):
       for y in range(-10,11):
           if((x + y) <= 5):
                valorf = eval(funcion)
                punto = [x,y]
                resultado.append([punto,valorf])            
   s = sorted(resultado, key=itemgetter(1))
   return print("La función",nombre,"en el intervalo x,y E [-10,10] se minimiza en el punto",s[0][0])
   
fuerzaBruta(fBooth,"Booth")
fuerzaBruta(fMatyas,"Matyas")