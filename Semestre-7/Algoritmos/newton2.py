import sympy as sp


# Definición de los símbolos
x = sp.symbols('x')
funcion = sp.sympify(input("Ingresa la función a optimizar: "))

# Definición de las derivadas
primera_derivada = sp.diff(funcion, x)
segunda_derivada = sp.diff(primera_derivada, x)

# Convierte las funciones simbólicas a funciones numéricas
funcion_numeric = sp.lambdify(x, funcion, "numpy")
primera_derivada_numeric = sp.lambdify(x, primera_derivada, "numpy")
segunda_derivada_numeric = sp.lambdify(x, segunda_derivada, "numpy")

# Inicialización de parámetros
x_actual = float(input("Ingresa el punto inicial x: "))
t = float(input("Ingresa un escalar t > 0: "))
error_cota = float(input("Ingresa una cota de error e > 0: "))

while True:
    x_siguiente = x_actual - t * (primera_derivada_numeric(x_actual) / segunda_derivada_numeric(x_actual))

    if abs(primera_derivada_numeric(x_siguiente)) < abs(primera_derivada_numeric(x_actual)):
        g_0 = abs(primera_derivada_numeric(x_actual))
        g_prime_0 = primera_derivada_numeric(x_actual) / (primera_derivada_numeric(x_siguiente) - primera_derivada_numeric(x_actual))
        g_1 = abs(primera_derivada_numeric(x_siguiente))
        t_prime = max(-g_prime_0 / (2 * (g_1 - g_0 - g_prime_0)), 0, 1)
        x_siguiente = (1 - t_prime) * x_actual + t_prime * x_siguiente

    if abs(x_siguiente - x_actual) <= error_cota:
        break

    x_actual = x_siguiente

print(f"El mínimo de la función se encuentra en x = {x_actual}")
