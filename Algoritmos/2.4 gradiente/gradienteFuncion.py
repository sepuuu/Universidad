fBo = "(x+2*y-7)**2+(2*x+y-5)**2"
#fBe = "(1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2+(2.625 - x + x*y**3)**2"

def gra_funcion(funcion, nombre): 
   x = [2, 4, 6, 5]
   y = [1, 3, 5, 6]
   deltax = [0.01, 0.04, 0.06, 0.08]
   deltay = [0.01, 0.5, 0.07, 0.09]

   def eva_funcion(f, x, y):
        derivadax = eval(f)
        return derivadax

   def derivar(x, deltax, y, deltay):
        derivada_x = (eva_funcion(str(funcion), x+deltax, y) - eva_funcion(str(funcion), x, y))/deltax
        derivada_y = (eva_funcion(str(funcion), y+deltay, x) - eva_funcion(str(funcion), y, x))/deltay
        return (derivada_x, derivada_y)

   for i in range(len(x)):
       print("gradiente función", nombre, "|con x=", x[i], "|y=", y[i], 
                                          "|delta x=", deltax[i], "|delta y=",
                                          deltay[i],"=",
                                          derivar(x[i],deltax[i],y[i],deltay[i]))
   print("------------------------------------------------------------------------------")
 
gra_funcion(fBo, "Booth")