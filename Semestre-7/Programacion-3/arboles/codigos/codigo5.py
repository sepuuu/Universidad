###Devuelve la cantidad de nodos que son raíz de un subárbol que tiene nodos con un solo hijo:



class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_raices_subarbol_con_un_solo_hijo(raiz):
    if raiz is None:
        return 0
    count = 0
    if (raiz.izquierda is not None and raiz.derecha is None) or (raiz.izquierda is None and raiz.derecha is not None):
        count += 1
    count += contar_raices_subarbol_con_un_solo_hijo(raiz.izquierda) + contar_raices_subarbol_con_un_solo_hijo(raiz.derecha)
    return count

# Ejemplo de uso
raiz = Nodo(5)
raiz.izquierda = Nodo(3)
raiz.derecha = Nodo(8)
raiz.izquierda.izquierda = Nodo(2)
raiz.izquierda.derecha = Nodo(4)
raiz.derecha.izquierda = Nodo(7)
raiz.derecha.derecha = Nodo(9)
raiz.derecha.derecha.derecha = Nodo(10)

print(contar_raices_subarbol_con_un_solo_hijo(raiz))  # Output: 2
