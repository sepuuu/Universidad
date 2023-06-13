# Definición de la clase para un nodo del ABB
class NodoABB:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para determinar si el ABB está equilibrado
def estaEquilibrado(nodo):
    # Caso base: si el nodo es nulo, se considera equilibrado
    if nodo is None:
        return True

    # Calcular la altura del subárbol izquierdo
    alturaIzquierdo = calcularAltura(nodo.izquierdo)

    # Calcular la altura del subárbol derecho
    alturaDerecho = calcularAltura(nodo.derecho)

    # Verificar la diferencia de alturas entre los subárboles
    if abs(alturaIzquierdo - alturaDerecho) > 1:
        return False

    # Verificar si los subárboles izquierdo y derecho también están equilibrados
    return estaEquilibrado(nodo.izquierdo) and estaEquilibrado(nodo.derecho)

# Función para calcular la altura de un nodo del ABB
def calcularAltura(nodo):
    # Caso base: si el nodo es nulo, la altura es 0
    if nodo is None:
        return 0

    # Calcular la altura del subárbol izquierdo
    alturaIzquierdo = calcularAltura(nodo.izquierdo)

    # Calcular la altura del subárbol derecho
    alturaDerecho = calcularAltura(nodo.derecho)

    # La altura del nodo es el máximo entre las alturas de los subárboles más 1
    return max(alturaIzquierdo, alturaDerecho) + 1

# Ejemplo de uso
nodoRaiz = NodoABB(5)
nodoRaiz.izquierdo = NodoABB(3)
nodoRaiz.derecho = NodoABB(7)
nodoRaiz.izquierdo.izquierdo = NodoABB(2)
nodoRaiz.izquierdo.derecho = NodoABB(4)
nodoRaiz.izquierdo.izquierdo.izquierdo=NodoABB(2)
# Construye tu árbol binario de búsqueda

if estaEquilibrado(nodoRaiz):
    print("El ABB está equilibrado")
else:
    print("El ABB no está equilibrado")
