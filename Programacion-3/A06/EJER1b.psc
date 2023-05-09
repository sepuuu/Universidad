// Se tiene un arreglo M de N elementos que contiene enteros positivos mayores que cero. 
// a)	Intercambiar cada elemento el menor de sus dos vecinos.
// b)	Contar los elementos cuyos dos vecinos son par
//
// CODIFICA TU RESPUESTA MAS ABAJO (agregando instrucciones para crear los arreglos, para
// mostrarlos y también para mostrar el o los resultados logrados con tu seudocódigo)
//-----------------------------------------------------------------------------------------
Algoritmo Ejer1B
	// Definir arreglo M, llenarlo con valores al azar y mostrarlo
	N = Aleatorio(5, 15)
	Dimension M(N)
	Para i desde 0 hasta N-1
		M[i] = Aleatorio(10, 90)
	FinPara
	Muestra(M, N)
	Escribir "a) Intercambiar cada elemento con el menor de sus dos vecinos"
	Para i desde 1 hasta N-2
		Si M[i-1] > M[i] y M[i+1] > M[i] entonces
			Si M[i-1] < M[i+1] entonces 
				Aux = M[i-1]
				M[i-1] = M[i]
				M[i] = Aux
			Sino
				Aux = M[i+1]
				M[i+1] = M[i]
				M[i] = Aux
			FinSi
		FinSi
	FinPara
	Muestra(M, N)
	
	Escribir "b) Contar los elementos cuyos dos vecinos son par"
	c = 0
	Para i desde 1 hasta N-2
		Si M[i-1] % 2 = 0 y M[i+1] % 2 = 0 entonces
			c = c + 1
		FinSi
	FinPara
	Escribir "Cantidad de elementos con dos vecinos pares: ", c
FinAlgoritmo

// Subalgoritmo para mostrar arreglo
SubAlgoritmo Muestra(M, N)
	Escribir "M[] = " Sin Saltar
	Para i desde 0 hasta N-1
		Escribir M[i], " " Sin Saltar
	FinPara
	Escribir ""
	Escribir ""
FinSubAlgoritmo	
	
	