##Devuelve la cantidad de nodos cuyo contenido se puede incrementar en 1 sin violar la regla del árbol binario de búsqueda

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos_incrementables(raiz):
    return contar_nodos_incrementables_util(raiz, float('-inf'), float('inf'))

def contar_nodos_incrementables_util(raiz, min_valor, max_valor):
    if raiz is None:
        return 0
    if min_valor < raiz.valor < max_valor:
        return 1 + contar_nodos_incrementables_util(raiz.izquierda, min_valor, raiz.valor) + contar_nodos_incrementables_util(raiz.derecha, raiz.valor, max_valor)
    else:
        return contar_nodos_incrementables_util(raiz.izquierda, min_valor, max_valor) + contar_nodos_incrementables_util(raiz.derecha, min_valor, max_valor)

# Ejemplo de uso
raiz = Nodo(5)
raiz.izquierda = Nodo(3)
raiz.derecha = Nodo(8)
raiz.izquierda.izquierda = Nodo(2)
raiz.izquierda.derecha = Nodo(4)
raiz.derecha.izquierda = Nodo(7)
raiz.derecha.derecha = Nodo(9)

print(contar_nodos_incrementables(raiz))  # Output: 5
