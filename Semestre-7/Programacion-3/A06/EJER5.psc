// Un arreglo MA de NA elementos se usa para contener una COLA otro MB de NB elementos se
// usa para contener una PILA. Escribe Seudoc�digo que repita una y otra vez lo siguiente
// - Extrae un valor desde la cola
// - Si es par lo suma con un valor sacado desde la pila y agrega la suma a la misma cola
// - Si es impar lo mete en la pila
//
// Este proceso termina (o nunca se ejecuta) si una de esas acciones no se puede ejecutar
//-------------------------------------------------------------------------------------------
// Puede = Verdadero                            // inicia indicador l�gico
// Mientras FRENTE > -1 y Puede                 // mientras cola tenga datos y se pueda
//    Valor = MA(FRENTE)                        // extraer un valor desde la cola
//    FRENTE = FRENTE + 1                       // por lo cual aumente �ndice de salida
//		                                        //
//    Si FRENTE > FINAL entonces                // si �ndice se hace mayor que el de entrada
//       FRENTE = -1                            // significa que se extrajo el �nico que
//       FINAL = -1                             // hab�a en la cola y ella queda vac�a, por lo
//    FinSi                                     // cual deben ponerse en -1 sus dos �ndices
//			                                    //
//    Si Valor es par entonces                  // si valor extra�do desde la cola es par ...
//       Si TOPE < 0 o FINAL = NA-1 entonces    // si pila vac�a o cola llena entonces?
//          Puede = Falso	                    // no se puede completar acci�n y todo acaba
//       Sino		                            // de lo contrario?
//          Valor = Valor + MB[TOPE]	        // suma valor y elemento sacado desde pila
//          TOPE = TOPE - 1	                    // por lo tanto baja TOPE
//          FINAL = FINAL + 1	                // avanza una posici�n en la cola
//          MA[FINAL] = Valor	                // para colocar all� esta suma resultante
//          Si FRENTE < 0 entonces	            // si la cola estaba vac�a tambi�n debe
//             FRENTE  =  FINAL	                // modificar el �ndice FRENTE
//          FinSi                               // 	
//       FinSi		                            //
//    Sino			                            // si valor extra�do desde cola era impar
//       Si TOPE < NB-1 entonces                // si hay espacio en la pila
//          TOPE = TOPE + 1                     // avanza el �ndice
//          MB[TOPE] = Valor                    // y coloca all� ese valor
//       Sino                                   // pero si no hay espacio en la pila
//          Puede = Falso                       // no puede completar la acci�n y todo acaba
//       FinSi	                                // 	
//    FinSi			                            // 
// FinMientras		                            // 
//-------------------------------------------------------------------------------------------
Algoritmo EJER1
	NA = Aleatorio(10,12)
	Dimension MA(NA)
	Escribir "MA[]   =" Sin Saltar
	Para i desde 0 hasta NA-1
		MA[i]=Aleatorio(10,90)
		Escribir " " MA[i] Sin Saltar
	FinPara
	Escribir ""
	
	FRENTE=Aleatorio(3, NA-1)
	FINAL =Aleatorio(NA, NA-1)
	Escribir "FRENTE = " FRENTE
	Escribir "FINAL  = " FINAL
	Escribir "-----------------------------------------"
	
	NB = Aleatorio(10,12)
	Dimension MB(NB)
	Escribir "MB[]   =" Sin Saltar
	Para i desde 0 hasta NB-1
		MB[i]=Aleatorio(10,90)
		Escribir " " MB[i] Sin Saltar
	FinPara
	Escribir ""
	
	TOPE =Aleatorio(3, NB-1)
	Escribir "TOPE   = " TOPE
	
	
	Mientras FRENTE > -1 y FINAL < NA-1 y TOPE < NB-1
		Escribir "FRENTE= " FRENTE " FINAL= " FINAL "  TOPE= " TOPE
		EXTRAIDO = MA[FRENTE]
		FRENTE = FRENTE + 1
		SI FRENTE > FINAL entonces
			FRENTE = -1
			FINAL  = -1
		FinSi
		Si EXTRAIDO es PAR entonces
			TOPE = TOPE + 1
			MB[TOPE] = EXTRAIDO
		Sino
			FINAL = FINAL + 1
			MA[FINAL] = EXTRAIDO
			Si FRENTE = -1 entonces
				FRENTE = FINAL
			Fin SI
		FinSi
	FinMientras
	
	Escribir ""
	Escribir ""
	
	Escribir "MA[]   =" Sin Saltar
	Para i desde 0 hasta NA-1
		Escribir " " MA[i] Sin Saltar
	FinPara
	Escribir ""
	
	Escribir "FRENTE = " FRENTE
	Escribir "FINAL  = " FINAL
	Escribir "-----------------------------------------"
	
	Escribir "MB[]   =" Sin Saltar
	Para i desde 0 hasta NB-1
		Escribir " " MB[i] Sin Saltar
	FinPara
	Escribir ""
	
	Escribir "TOPE   = " TOPE
	
FinAlgoritmo
