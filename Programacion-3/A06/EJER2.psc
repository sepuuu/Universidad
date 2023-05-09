// Se tiene un arreglo  M de N  elementos. Escribe  un proceso iterativo  que obtenga la
// suma de todos los elementos que existen entre el menor y el  mayor valor  del arreglo
// (sin incluirlos). Considera casos especiales (mayor est� antes que menor, ambos est�n
// contiguos, todos los elementos son de igual valor)
//-------------------------------------------------------------------------------------------
// ###########
// Pmenor = 0                                // Inicialmente primero es el menor
// Pmayor = 0                                // y el mayor
// Para desde i=0 hasta N-1 hacer            // recorre todo el arreglo
//    Si M(i) > M(Pmayor) entonces           // si actual mayor que el de posici�n Pmayor
//       Pmayor = i                          // entonces Pmayor ahora es esta posici�n
//    Fin Si                                 // 
//    Si M(i) < M(Pmenor) entonces           // si actual menor que el de posici�n Pmenor
//       Pmenor = i                          // entonces Pmenor ahora es esta posici�n
//    Fin Si                                 //
// Fin Para                                  //
// Si Pmenor > Pmayor entonces               // ordena Pmenor y Pamayor ascendente 
//    Temp   =  Pmenor                       // 
//	  Pmenor =  Pmayor                       //
//    Pmayor = Temp                          //
// Fin Si                                    //
// Suma = 0                                  // suma inicial cero
// Si Pmayor-Pmenor >1 entonces              // Si Pmayor y Pmenor no contiguos � iguales
//    Para i desde Pmenor+1  hasta Pmayor-1	 // recorre desde justo despu�s de Pmenor
//       Suma = Suma + M(i)     	         // hasta justo antes de Pmayor
//    Fin Para                               //
// Fin Si                                    //
//-------------------------------------------------------------------------------------------
// para usar �ndices desde 0 debes configurar Pseint de la siguiente forma...
// Clic Configurar, Clic en opciones del Lenguaje, Clic en ersonalizar (abajo), Clic en
// casilla Utilizar �ndices en arreglo y cadenas en base 0, Clic Aceptar, Clic Aceptar
//-------------------------------------------------------------------------------------------

Algoritmo EJER2
	// define arreglo, lo llena con valores al azar y lo muestra
	N = Aleatorio(5, 15)
	Dimension M(N)
	Escribir "M[] = " Sin Saltar
	Para i desde 0 hasta N-1
		M[I]=Aleatorio(10,90)
		Escribir " " M[i] Sin Saltar
	FinPara
	Escribir ""
	Escribir "     " Sin Saltar
	Para i desde 0 hasta N-1
		Escribir "  " i Sin Saltar
	FinPara
	Escribir ""
	Escribir ""
	
	Pmenor = 0
	Pmayor = 0						
	Para i desde 0 hasta N-1 hacer
		Si M(i) > M(Pmayor) entonces
			Pmayor = i
		Fin Si
		Si M(i) < M(Pmenor) entonces
			Pmenor = i
		Fin Si
	Fin Para
	
	Escribir "posici�n menor = " Pmenor
	Escribir "posici�n mayor = " Pmayor

	Si Pmenor > Pmayor entonces
		Temp   =  Pmenor
		Pmenor =  Pmayor			
		Pmayor = Temp				
	Fin Si
	
	Escribir ""
	Escribir "Sumar desde " Pmenor+1 " hasta " Pmayor-1
	Suma = 0
	Si Pmayor-Pmenor >1 entonces
		Para i desde Pmenor+1  hasta Pmayor-1
			Suma = Suma + M(i)
		Fin Para						
	Fin Si
	
	Escribir "Suma entre menor y mayor (excluidos) = " Suma
FinAlgoritmo
