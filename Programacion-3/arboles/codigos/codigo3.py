##Devuelve verdadero si el árbol está completo o Falso en caso contrario

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def es_arbol_completo(raiz):
    if raiz is None:
        return True
    if raiz.izquierda is None and raiz.derecha is None:
        return True
    if raiz.izquierda is not None and raiz.derecha is not None:
        return (es_arbol_completo(raiz.izquierda) and es_arbol_completo(raiz.derecha))
    return False

# Ejemplo de uso
raiz = Nodo(5)
raiz.izquierda = Nodo(3)
raiz.derecha = Nodo(8)
raiz.izquierda.izquierda = Nodo(2)
raiz.izquierda.derecha = Nodo(4)

print(es_arbol_completo(raiz))  # Output: True
