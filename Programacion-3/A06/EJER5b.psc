// Un arreglo MA de NA elementos se usa para contener una COLA otro MB de NB elementos se
// usa para contener una PILA. Escribe Seudocódigo que...
// - Repite una y otra vez lo siguiente, pero solo mientras se pueda...
//   - saca un valor de la pila y al mismo tiempo extrae un valor de la cola
//   - si ambos son impares los suma y agrega esa suma a la cola (en caso contrario nada)
//
// CODIFICA TU RESPUESTA MAS ABAJO (agregando instrucciones para crear los arreglos, para
// mostrarlos y también para mostrar el o los resultados logrados con tu seudocódigo)
//-------------------------------------------------------------------------------------------
Algoritmo EJER5B
	NA = Aleatorio(10, 12)
	Dimension MA(NA)
	Escribir "MA[]   =" Sin Saltar
	Para i desde 0 hasta NA-1
		MA[i] = Aleatorio(10, 90)
		Escribir " " MA[i] Sin Saltar
	FinPara
	Escribir ""
	
	FRENTE = Aleatorio(3, NA-1)
	FINAL = Aleatorio(NA, NA-1)
	Escribir "FRENTE = " FRENTE
	Escribir "FINAL  = " FINAL
	Escribir "-----------------------------------------"
	
	NB = Aleatorio(10, 12)
	Dimension MB(NB)
	Escribir "MB[]   =" Sin Saltar
	Para i desde 0 hasta NB-1
		MB[i] = Aleatorio(10, 90)
		Escribir " " MB[i] Sin Saltar
	FinPara
	Escribir ""
	
	TOPE = Aleatorio(3, NB-1)
	Escribir "TOPE   = " TOPE
	
	Mientras FRENTE > -1 y FINAL < NA-1 y TOPE > -1
		Escribir "FRENTE= " FRENTE " FINAL= " FINAL "  TOPE= " TOPE
		VALOR_COLA = MA[FRENTE]
		VALOR_PILA = MB[TOPE]
		FRENTE = FRENTE + 1
		TOPE = TOPE - 1
		
		Si VALOR_COLA % 2 = 1 y VALOR_PILA % 2 = 1 entonces
			SUMA = VALOR_COLA + VALOR_PILA
			FINAL = FINAL + 1
			MA[FINAL] = SUMA
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

