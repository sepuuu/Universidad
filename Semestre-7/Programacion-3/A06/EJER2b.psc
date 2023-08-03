// Se tiene un arreglo  M de N  elementos. Escribe  un proceso iterativo  que obtenga la
// suma de todos los elementos que sean menores al primer elemento del arreglo pero, que
// a la vez, sean mayores al último. Por ejemplo, si al arreglo fuese...
//
// M[] = 34  12 45 16 20 32 14   los que cumplen la condicion son solamente 16, 20 y 32
//
// CODIFICA TU RESPUESTA MAS ABAJO (agregando instrucciones para crear los arreglos, para
// mostrarlos y también para mostrar el o los resultados logrados con tu seudocódigo)
//-------------------------------------------------------------------------------------------
Algoritmo EJER2B
	// Define el arreglo, llénalo con valores al azar y muéstralo
	N = Aleatorio(5, 15)
	Dimension M(N)
	Escribir "M[] = " Sin Saltar
	Para i desde 0 hasta N-1
		M[i] = Aleatorio(10, 90)
		Escribir M[i], " " Sin Saltar
	FinPara
	Escribir ""
	Escribir ""
	PrimerElemento = M[0]
	UltimoElemento = M[N-1]
	
	Escribir "Primer elemento: ", PrimerElemento
	Escribir "Último elemento: ", UltimoElemento
	
	Suma = 0
	
	Para i desde 1 hasta N-2
		Si M[i] < PrimerElemento y M[i] > UltimoElemento entonces
			Suma = Suma + M[i]
		FinSi
	FinPara
	
	Escribir "Suma de elementos menores al primer elemento y mayores al último: ", Suma
FinAlgoritmo

	
