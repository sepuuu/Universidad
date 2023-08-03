// Un arreglo MA de NA elementos se usa para contener una Cola, un arreglo MB de NB elementos
// se usa para contener otra Cola. Seudocódigo de ciclo  repetitivo para  extraer datos desde
// amabas colas (al mismo tiempo). Cada valor PAR extraído (desde cualquiera de ellas) deberá
// agegrarse a  la primera cola, cada valor IMPAR extraído (desde cualquiera de ellas) deberá
// agregarse a la segunda cola. Esto se repite una y otra vez mientras se pueda.
//
// CODIFICA TU RESPUESTA MAS ABAJO (agregando instrucciones para crear los arreglos, para
// mostrarlos y también para mostrar el o los resultados logrados con tu seudocódigo)
//-------------------------------------------------------------------------------------------
Algoritmo EJER2_B
	NA = Aleatorio(5, 10)
	Dimension MA(NA)
	Escribir "MA[] =" Sin Saltar
	Para i desde 0 hasta NA-1
		MA[i] = Aleatorio(10,90)
		Escribir " " MA[i] Sin Saltar
	FinPara
	Escribir ""
	
	NB = Aleatorio(5, 10)
	Dimension MB(NB)
	Escribir "MB[] =" Sin Saltar
	Para i desde 0 hasta NB-1
		MB[i] = Aleatorio(10,90)
		Escribir " " MB[i] Sin Saltar
	FinPara
	Escribir ""
	Escribir "---------------------------------------------------"
	
	FRENTE_MA = 0
	FINAL_MA = NA - 1
	FRENTE_MB = 0
	FINAL_MB = NB - 1
	
	Mientras (FRENTE_MA <= FINAL_MA) y (FRENTE_MB <= FINAL_MB)
		EXTRAIDO_MA = MA[FRENTE_MA]
		EXTRAIDO_MB = MB[FRENTE_MB]
		
		Si EXTRAIDO_MA es par entonces
			FINAL_MA = FINAL_MA + 1
			MA[FINAL_MA-1] = EXTRAIDO_MA
		Sino
			FINAL_MB = FINAL_MB + 1
			MB[FINAL_MB] = EXTRAIDO_MA
		FinSi
		
		Si EXTRAIDO_MB es par entonces
			FINAL_MA = FINAL_MA + 1
			MA[FINAL_MA] = EXTRAIDO_MB
		Sino
			FINAL_MB = FINAL_MB + 1
			MB[FINAL_MB] = EXTRAIDO_MB
		FinSi
		
		FRENTE_MA = FRENTE_MA + 1
		FRENTE_MB = FRENTE_MB + 1
	FinMientras		
	
	Escribir "MA[] =" Sin Saltar
	Para i desde 0 hasta FINAL_MA
		Escribir " " MA[i] Sin Saltar
	FinPara
	Escribir "    FRENTE_MA = " FRENTE_MA ", FINAL_MA = ", FINAL_MA
	
	Escribir "      " Sin Saltar
	Para i desde 0 hasta FINAL_MA
		Escribir "  " i Sin Saltar
	FinPara
	Escribir ""
	
	Escribir "MB[] =" Sin Saltar
	Para i desde 0 hasta FINAL_MB
		Escribir " " MB[i] Sin Saltar
	FinPara
	Escribir "    FRENTE_MB = " FRENTE_MB ", FINAL_MB = ", FINAL_MB
	Escribir "      " Sin Saltar
	Para i desde 0 hasta FINAL_MB
		Escribir "  " i Sin Saltar
	FinPara
	Escribir ""
FinAlgoritmo
