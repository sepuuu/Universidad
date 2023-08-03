// Un arreglo MA de NA elementos se usa para contener una Cola, un arreglo MB de NB elementos
// se usa para contener una Pila. Seudocódigo de ciclo repetitivo para extraer de la cola los
// elementos de  valor PAR y  meterlos en la Pila. (los  de valor  IMPAR  deben permanecer en
// la Cola). Este proceso termina en cuanto no sea posible continuar
//-------------------------------------------------------------------------------------------
// SEUDOCODIGO
// ###########
// Mientras FRENTE > -1 y FINAL < NA-1 y TOPE < NB-1
//    EXTRAIDO = MA[FRENTE]
//    FRENTE = FRENTE + 1
//    SI FRENTE > FINAL entonces
//	     FRENTE = -1
//	     FINAL = -1
//    FinSi
//    Si EXTRAIDO es PAR entonces
//	     TOPE = TOPE + 1
//	     MB[TOPE] = EXTRAIDO
//    Sino
//	     FINAL = FINAL + 1
//	     MA[FINAL] = EXTRAIDO
//	     Si FRENTE = -1 entonces
//          FRENTE = 0
//        Fin SI
//    FinSi
// FinMientras
//-------------------------------------------------------------------------------------------
Algoritmo EJER2
	NA = Aleatorio(5, 10)
	Dimension MA(NA)
	Escribir "MA[] =" Sin Saltar
	Para i desde 0 hasta NA-1
		MA[i] = Aleatorio(10,90)
		Escribir " " MA[i] Sin Saltar
	FinPara
	FRENTE = 3 
	FINAL  = Aleatorio(FRENTE,NA-1)
	Escribir "    FRENTE = " FRENTE ", FINAL = ", FINAL
	
	Escribir "      " Sin Saltar
	Para i desde 0 hasta NA-1
		Escribir "  " i Sin Saltar
	FinPara
	Escribir ""
	
	NB = Aleatorio(5, 10)
	Dimension MB(NB)
	TOPE = Aleatorio(0, NB-1)
	Escribir "MB[] =" Sin Saltar
	Para i desde 0 hasta NB-1
		MB[i] = Aleatorio(10,90)
		Escribir " " MB[i] Sin Saltar
	FinPara
	Escribir "    TOPE = " TOPE 
	Escribir "      " Sin Saltar
	
	Para i desde 0 hasta NB-1
		Escribir "  " i Sin Saltar
	FinPara
	Escribir ""
	Escribir "---------------------------------------------------"

	Puede = Verdadero
	Mientras FRENTE > -1 y Puede
		Valor = MA(FRENTE)
		FRENTE = FRENTE + 1
		
		Si FRENTE > FINAL entonces
			FRENTE = -1
			FINAL = -1
		FinSi
		
		Si Valor es par entonces
			Si TOPE < 0 o FINAL = NA-1 entonces
				Puede = Falso
			Sino
				Valor = Valor + MB[TOPE]
				TOPE = TOPE + 1
				FINAL = FINAL + 1
				MA[FINAL] = Valor
				Si FRENTE < 0 entonces
					FRENTE  =  FINAL
				FinSi	
			FinSi		
		Sino
			Si TOPE < NB-1 entonces
				TOPE = TOPE + 1
				MB[TOPE] = Valor
			Sino
				Puede = Falso
			FinSi		
		FinSi			
	FinMientras		
	
	Escribir "MA[] =" Sin Saltar
	Para i desde 0 hasta NA-1
		Escribir " " MA[i] Sin Saltar
	FinPara
	Escribir "    FRENTE = " FRENTE ", FINAL = ", FINAL
	
	Escribir "      " Sin Saltar
	Para i desde 0 hasta NA-1
		Escribir "  " i Sin Saltar
	FinPara
	Escribir ""
	
	Escribir "MB[] =" Sin Saltar
	Para i desde 0 hasta NB-1
		Escribir " " MB[i] Sin Saltar
	FinPara
	Escribir "    TOPE = " TOPE 
	Escribir "      " Sin Saltar
	Para i desde 0 hasta NB-1
		Escribir "  " i Sin Saltar
	FinPara
	Escribir ""
FinAlgoritmo

