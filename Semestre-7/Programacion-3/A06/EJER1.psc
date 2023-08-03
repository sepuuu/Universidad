// Se tiene un arreglo M de N elementos que contiene enteros positivos mayores que cero. 
// a)	Intercambiar cada elemento con su vecino siguiente, si ese vecino es mayor.
// b)	Contar los elementos que son menores o mayores que sus dos vecinos
//-----------------------------------------------------------------------------------------
// SEUDOCODIGO
// ###########
// (a) Para i desde 0 hasta N-2        (b) c = 0
//	      Si M(i) < M(i+1) entonces        Para i desde 0 hasta N-1
//		     Aux = M(i)                       Si i >0  y  i < N-1 entonces
//		     M(i) = M(i+1)                       Si M(i-1) > M(i) y M(i) < M(i+1) entonces
//           M(i+1) = Aux                           c = c + 1  
//	      FinSi                                  FinSi
//     FinPara                                   Si M(i-1) < M(i)  y  M(i) > M(i+1) 
//                                                  c = c + 1
//                                               FinSi
//                                            FinSi
//                                         FinPara
//-----------------------------------------------------------------------------------------
// para usar índices desde 0 debes configurar Pseint de la siguiente forma...
// Clic Configurar, Clic en opciones del Lenguaje, Clic en ersonalizar (abajo), Clic en
// casilla Utilizar índices en arreglo y cadenas en base 0, Clic Aceptar, Clic Aceptar
//-----------------------------------------------------------------------------------------

Algoritmo Ejer1
	// definir arreglo M, llenarlo con valores al azar y mostralo
	N = Aleatorio(5, 15)
	Dimension M(N)
	Para i desde 0 hasta N-1
		M[I]=Aleatorio(10,90)
	FinPara
	Muestra(M, N)
	
	Escribir "a) intercambia elemento con siguiente si ese es mayor"
	Para i desde 0 hasta N-2
		Si M(i) < M(i+1) entonces
			Aux = M(i)
			M(i) = M(i+1)
			M(i+1) = Aux
		FinSi
	FinPara
	Muestra(M, N)
	
	Escribir "b) elementos mayores o menores a sus dos vecinos"
	c = 0
	Para i desde 0 hasta N-1	
		Si i>0  y  i<N-1 entonces	
			Si M(i-1)>M(i)  y  M(i)<M(i+1) entonces
				c = c + 1
			FinSi
			Si M(i-1)<M(i)  y  M(i)>M(i+1) entonces
				c = c + 1
			FinSi
		FinSi
	FinPara
	Escribir "cumplen la condición = " c
FinAlgoritmo

// sub algoritmo para mostrar arreglo
SubAlgoritmo Muestra(M, N)
	Escribir "M[] =" Sin Saltar
	Para i desde 0 hasta N-1
		Escribir " " M[i] Sin Saltar
	FinPara
	Escribir ""	
	Escribir ""
FinSubAlgoritmo
