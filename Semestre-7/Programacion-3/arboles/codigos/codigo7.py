class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def eliminar_hojas_en_abb(raiz):
    if raiz is None:
        return None
    
    raiz.izquierdo = eliminar_hojas_en_abb(raiz.izquierdo)
    raiz.derecho = eliminar_hojas_en_abb(raiz.derecho)
    
    if raiz.izquierdo is None and raiz.derecho is None:
        return None
    
    return raiz

# Ejemplo de uso
# Creamos un ABB de ejemplo
raiz = Nodo(8)
raiz.izquierdo = Nodo(3)
raiz.derecho = Nodo(10)
raiz.izquierdo.izquierdo = Nodo(1)
raiz.izquierdo.derecho = Nodo(6)
raiz.derecho.derecho = Nodo(14)
raiz.derecho.derecho.izquierdo = Nodo(13)

# Imprimimos el ABB antes de eliminar las hojas
def imprimir_abb(raiz):
    if raiz is not None:
        imprimir_abb(raiz.izquierdo)
        print(raiz.valor, end=' ')
        imprimir_abb(raiz.derecho)

print("ABB antes de eliminar las hojas:")
imprimir_abb(raiz)
print()

# Eliminamos las hojas en cada nodo que tenga dos hojas
raiz = eliminar_hojas_en_abb(raiz)

# Imprimimos el ABB después de eliminar las hojas
print("ABB después de eliminar las hojas:")
imprimir_abb(raiz)
print()
