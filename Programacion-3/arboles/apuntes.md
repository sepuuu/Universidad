# Árboles Binarios de Búsqueda

## Definición de árbol binario de búsqueda
Un árbol binario de búsqueda es una estructura de datos jerárquica donde cada nodo tiene un valor asociado y cumple con la propiedad de que el valor de cada nodo en el subárbol izquierdo es menor que el valor del nodo y el valor de cada nodo en el subárbol derecho es mayor que el valor del nodo.

## Estructura de un nodo del árbol
Cada nodo del árbol binario de búsqueda tiene tres componentes principales:
- Valor: El valor almacenado en el nodo.
- Subárbol izquierdo: Una referencia al subárbol izquierdo, que contiene valores menores que el valor del nodo actual.
- Subárbol derecho: Una referencia al subárbol derecho, que contiene valores mayores que el valor del nodo actual.

## Inserción en un árbol binario de búsqueda
Para insertar un nuevo nodo en un árbol binario de búsqueda, se sigue el siguiente pseudocódigo:

```
insertar(nodo, valor):
   si nodo es nulo:
       crear un nuevo nodo con el valor y devolverlo
   si valor es menor que nodo.valor:
       nodo.izquierdo = insertar(nodo.izquierdo, valor)
   si valor es mayor que nodo.valor:
       nodo.derecho = insertar(nodo.derecho, valor)
   devolver nodo
```

## Búsqueda en un árbol binario de búsqueda
Para buscar un valor en un árbol binario de búsqueda, se sigue el siguiente pseudocódigo:

```
buscar(nodo, valor):
   si nodo es nulo o nodo.valor es igual a valor:
       devolver nodo
   si valor es menor que nodo.valor:
       devolver buscar(nodo.izquierdo, valor)
   si valor es mayor que nodo.valor:
       devolver buscar(nodo.derecho, valor)
```

## Recorrido de un árbol binario de búsqueda
Hay tres tipos principales de recorrido en un árbol binario de búsqueda:
- Recorrido en orden (in-order): Se visita primero el subárbol izquierdo, luego el nodo actual y finalmente el subárbol derecho.
- Recorrido en preorden (pre-order): Se visita primero el nodo actual, luego el subárbol izquierdo y finalmente el subárbol derecho.
- Recorrido en postorden (post-order): Se visita primero el subárbol izquierdo, luego el subárbol derecho y finalmente el nodo actual.

