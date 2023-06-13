import sympy as sp

def gradiente_descendente_barzilai_borwein(funcion, valores_iniciales, tolerancia=1e-6, max_iteraciones=1000):
    x, y = sp.symbols('x y')
    funcion = sp.sympify(funcion)
    gradiente = sp.Matrix([funcion.diff(var) for var in (x, y)])

    valores = sp.Matrix(valores_iniciales)
    valor_funcion = funcion.subs({sp.symbols('x'): valores[0], sp.symbols('y'): valores[1]})
    valor_funcion_antiguo = valor_funcion + 2 * tolerancia

    iteraciones = 0
    while abs(valor_funcion_antiguo - valor_funcion) > tolerancia and iteraciones < max_iteraciones:
        grad = gradiente.subs({sp.symbols('x'): valores[0], sp.symbols('y'): valores[1]})
        if iteraciones > 0:
            s = valores - valores_antiguos
            y = grad - gradiente_antiguo
            t = abs((s.T*y)[0]/(y.T*y)[0])
        else:
            t = 0.01
        valores_antiguos = valores
        gradiente_antiguo = grad
        valores = valores - t * grad
        valor_funcion_antiguo = valor_funcion
        valor_funcion = funcion.subs({sp.symbols('x'): valores[0], sp.symbols('y'): valores[1]})
        iteraciones += 1

    return valores, iteraciones, valor_funcion

# Prueba de la función
funcion = "(x-3)**2 + (y-2)**2"
valores_iniciales = [0.0, 0.0]
resultado, iteraciones, valor_funcion = gradiente_descendente_barzilai_borwein(funcion, valores_iniciales)

print(f"El óptimo local está en {resultado}, se encontró en {iteraciones} iteraciones. El valor de la función en este punto es {valor_funcion}.")
