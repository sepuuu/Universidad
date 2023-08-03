El método main() tiene ya escrito el código necesario para realizar algunas maniobras
con lista, solo falta que escribas en la clase Lista el código de algunos métodos. En
esos métodos he dejado tantas líneas de comentario como líneas empleé yo (seguramente
tú ocuparás menos ó más, dependiendo de como diseñes la lógica de ellos)
 
Insertar por delante
- Si lista está vacía entonces el nuevo será primero y último
- Si lista no está vacía entonces el nuevo será ahora el primero

Insertar por detras
- Si lista está vacía entonces el nuevo será primero y último
- Si lista no está vacía entonces último apunta al nuevo y nuevo será ahora el último

Insertar en Orden
- Si lista está vacía entonces el nuevo será primero y último
- Si lista no está vacía entonces se debe recorrer  la lista comparando el nuevo con cada nodo
  y en cuanto se llegue a un nodo cuyo contenido sea mayor que el contenido del nuevo entonces
  se debe hacer que el anterior a ese nodo apunte  al nuevo y  que el  nuevo apunte a ese nodo
  
  Pero hay que tener en mente la posibilidad de que ningún nodo de la lista sea mayor al nuevo
  caso en el cual el último debe apuntar al nuevo y ahora ese nuevo será el último

Invertir
- Si lista no está vacía entonces se debe recorrer la lista y a cada nodo cambiarle su nexo de
  modo que apunte al anterior (obviamente, antes de hacer eso se deberá memorizar nexo al nodo
  siguiente para evitar que se pierda el resto de la lista). Se continúa recorriendo gracias a
  que se memorizó enlace al nodo siguiente y se sigue haciendo lo mismo hasta el final. 
