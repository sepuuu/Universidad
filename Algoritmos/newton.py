import sympy as sp

def newton_raphson(func, guess, tol=1e-6, max_iter=100):
    # Definición de la variable simbólica
    x = sp.symbols('x')
    
    # Cálculo de la derivada de la función
    derivative = sp.diff(func, x)

    # Conversión de las funciones simbólicas a funciones numéricas
    func = sp.lambdify(x, func, "numpy")
    derivative = sp.lambdify(x, derivative, "numpy")
    
    # Algoritmo de Newton
    for i in range(max_iter):
        guess = guess - func(guess) / derivative(guess)
        if abs(func(guess)) < tol:
            print(f"La función converge a cero en el punto {guess} después de {i} iteraciones.")
            return guess
    print(f"El método no converge después de {max_iter} iteraciones.")
    return guess

# Función de prueba
x = sp.symbols('x')
f = x**x-6

# Punto de partida
guess = 2.0

newton_raphson(f, guess)
