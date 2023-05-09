// Seudocódigo de una función recursiva que muestre  uno a uno los valores mayores  que 20
// que existen en un arreglo M de N enteros, desde el último al primero, y que devuelva la
// la suma de todos los menores que 20
//
// Por ejemplo, si el contenido del arreglo fuese:  10 15 23 14 46 11 24 33 40 19 
// Debería mostrar: 40 33 24 46 23 y devolver 69 (suma de 19 + 11 + 14 + 15 + 10)
//
// CODIFICA TU RESPUESTA MAS ABAJO (agregando instrucciones para crear los arreglos, para
// mostrarlos y también para mostrar el o los resultados logrados con tu seudocódigo)
//-------------------------------------------------------------------------------------------
// SEUDOCODIGO
// ###########

Algoritmo EJER4_B
	// Define arreglo, lo llena con valores al azar y lo muestra
	N = 10
	Dimension M(N)
	Escribir "M[] =" Sin Saltar
	Para i desde 0 hasta N-1
		M[i] = Aleatorio(10, 90)
		Escribir " " M[i] Sin Saltar
	FinPara
	Escribir ""
	
	Escribir "Valores mayores a 20 desde el último recursivamente"
	suma = MayoresVeinte(M, N-1)
	Escribir ""
	Escribir "Suma menores a 20 = " suma
FinAlgoritmo

// FUNCION RECURSIVA
Funcion res <- MayoresVeinte(M, x)
	Si x < 0 entonces
		res = 0
	Sino
		Si M[x] > 20 entonces
			sumaMenores = M[x] + MayoresVeinte(M, x-1)
			Escribir M[x] " " sin saltar
		SiNo
			sumaMenores = MayoresVeinte(M, x-1)
		FinSi
		res = sumaMenores
	FinSi
FinFuncion


