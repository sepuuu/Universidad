##Devuelve verdadero si el árbol es realmente un árbol binario de búsqueda o Falso en caso contrario

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def es_arbol_binario_de_busqueda(raiz):
    return es_arbol_binario_de_busqueda_util(raiz, float('-inf'), float('inf'))

def es_arbol_binario_de_busqueda_util(raiz, min_valor, max_valor):
    if raiz is None:
        return True
    if raiz.valor <= min_valor or raiz.valor >= max_valor:
        return False
    return (es_arbol_binario_de_busqueda_util(raiz.izquierda, min_valor, raiz.valor) and
            es_arbol_binario_de_busqueda_util(raiz.derecha, raiz.valor, max_valor))

# Ejemplo de uso
raiz = Nodo(5)
raiz.izquierda = Nodo(3)
raiz.derecha = Nodo(8)
raiz.izquierda.izquierda = Nodo(2)
raiz.izquierda.derecha = Nodo(4)
raiz.derecha.izquierda = Nodo(7)
raiz.derecha.derecha = Nodo(9)

print(es_arbol_binario_de_busqueda(raiz))  # Output: True
