// Un arreglo MA de NA elementos se usa para contener una COLA otro MB de NB elementos se
// usa para contener una PILA. Escribe Seudocódigo que repita una y otra vez lo siguiente
// - Extrae un valor desde la cola
// - Si es par lo suma con un valor sacado desde la pila y agrega la suma a la misma cola
// - Si es impar lo mete en la pila
//
// Este proceso termina (o nunca se ejecuta) si una de esas acciones no se puede ejecutar
//-------------------------------------------------------------------------------------------
// Puede = Verdadero                            // inicia indicador lógico
// Mientras FRENTE > -1 y Puede                 // mientras cola tenga datos y se pueda
//    Valor = MA(FRENTE)                        // extraer un valor desde la cola
//    FRENTE = FRENTE + 1                       // por lo cual aumente índice de salida
//		                                        //
//    Si FRENTE > FINAL entonces                // si índice se hace mayor que el de entrada
//       FRENTE = -1                            // significa que se extrajo el único que
//       FINAL = -1                             // había en la cola y ella queda vacía, por lo
//    FinSi                                     // cual deben ponerse en -1 sus dos índices
//			                                    //
//    Si Valor es par entonces                  // si valor extraído desde la cola es par ...
//       Si TOPE < 0 o FINAL = NA-1 entonces    // si pila vacía o cola llena entonces?
//          Puede = Falso	                    // no se puede completar acción y todo acaba
//       Sino		                            // de lo contrario?
//          Valor = Valor + MB[TOPE]	        // suma valor y elemento sacado desde pila
//          TOPE = TOPE - 1	                    // por lo tanto baja TOPE
//          FINAL = FINAL + 1	                // avanza una posición en la cola
//          MA[FINAL] = Valor	                // para colocar allí esta suma resultante
//          Si FRENTE < 0 entonces	            // si la cola estaba vacía también debe
//             FRENTE  =  FINAL	                // modificar el índice FRENTE
//          FinSi                               // 	
//       FinSi		                            //
//    Sino			                            // si valor extraído desde cola era impar
//       Si TOPE < NB-1 entonces                // si hay espacio en la pila
//          TOPE = TOPE + 1                     // avanza el índice
//          MB[TOPE] = Valor                    // y coloca allí ese valor
//       Sino                                   // pero si no hay espacio en la pila
//          Puede = Falso                       // no puede completar la acción y todo acaba
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
