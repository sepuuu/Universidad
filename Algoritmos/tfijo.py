import sympy as sp

# Definir las variables de la función
x, y = sp.symbols('x y')

# Solicitar al usuario la función a optimizar
funcion = sp.sympify(input("Ingrese la función a optimizar: "))

# Calcular las derivadas parciales de la función
derivada_respecto_x = sp.diff(funcion, x)
derivada_respecto_y = sp.diff(funcion, y)

# Definir el paso del algoritmo
paso = float(input("Ingrese el tamaño de paso (paso): "))

# Inicializar las variables a un punto de partida
x_actual = float(input("Ingrese el valor inicial de x: "))
y_actual = float(input("Ingrese el valor inicial de y: "))

# Definir el criterio de convergencia
epsilon = 1e-6

# Bucle principal del algoritmo de descenso de gradiente
while True:
    # Calcular los gradientes en el punto actual
    gradiente_x = derivada_respecto_x.evalf(subs={x: x_actual, y: y_actual})
    gradiente_y = derivada_respecto_y.evalf(subs={x: x_actual, y: y_actual})
    
    # Actualizar las variables
    x_siguiente = x_actual - paso * gradiente_x
    y_siguiente = y_actual - paso * gradiente_y

    # Verificar la condición de convergencia
    if abs(x_siguiente - x_actual) < epsilon and abs(y_siguiente - y_actual) < epsilon:
        break

    # Actualizar las variables actuales
    x_actual = x_siguiente
    y_actual = y_siguiente

# Imprimir el punto óptimo
print(f'El punto óptimo es ({x_actual}, {y_actual})')
