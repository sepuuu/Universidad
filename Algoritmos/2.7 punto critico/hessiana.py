from sympy import symbols, hessian, Function, N

x, y = symbols('x y')

def funcion(x, y):
    # Aquí defines tu función. Por ejemplo, f = x^2 + y^2.
    return (x-1)**2+(x-y)**4

def tipo_punto_critico(f, x, y):
    H = hessian(f(x, y), (x, y))
    eigenvalues = [N(i) for i in H.eigenvals()]

    if all(val > 0 for val in eigenvalues):
        return "Es un mínimo local"
    elif all(val < 0 for val in eigenvalues):
        return "Es un máximo local"
    elif any(val > 0 for val in eigenvalues) and any(val < 0 for val in eigenvalues):
        return "Es un punto de silla"
    else:
        return "No hay información suficiente"

print(tipo_punto_critico(funcion, x, y))
