###Devuelve la cantidad de nodos que tienen dos hijos

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos_con_dos_hijos(raiz):
    if raiz is None:
        return 0
    if raiz.izquierda is not None and raiz.derecha is not None:
        return 1 + contar_nodos_con_dos_hijos(raiz.izquierda) + contar_nodos_con_dos_hijos(raiz.derecha)
    else:
        return contar_nodos_con_dos_hijos(raiz.izquierda) + contar_nodos_con_dos_hijos(raiz.derecha)

# Ejemplo de uso
raiz = Nodo(5)
raiz.izquierda = Nodo(3)
raiz.derecha = Nodo(8)
raiz.izquierda.izquierda = Nodo(2)
raiz.izquierda.derecha = Nodo(4)
raiz.derecha.izquierda = Nodo(7)
raiz.derecha.derecha = Nodo(9)

print(contar_nodos_con_dos_hijos(raiz))  # Output: 3
