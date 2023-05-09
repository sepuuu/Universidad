// Se tiene un arreglo  M de N  enteros. Escribe un seudocódigo para recorrerlo y cada vez
// que se llegue a un elemento  menor que su  anterior  sume el valor  de este elemento al
// siguiente y este elemento lo deje en 10. Al final debe mostrar cuantos elementos son 10
//-------------------------------------------------------------------------------------------
// SEUDOCODIGO
// ###########
// V = 0                           // inicia contador elementos con cero
// Si M[0] = 10 entonces           // si primer elemento es 10
//    V = 1                        // lo cuenta como vacío
// Fin Si                          //
// Para i desde 1 hasta N-2        // Recorre desde segundo elemento a penúltimo
//    Si M(i) < M[i-1] entonces    // Si actual es menor que el anterior 
//       M[i+1] = M[i+1] + M[i]    // suma su valor al siguiente
//       M[i] = 10                 // y deja en 10 este elemento actual
//       V = V + 1                 // cuenta un elemento cero mas
//    FinSi	                       //
// FinPara                         //
// Escribir "son 10 = ", V         //
//                                 //
// Por ejemplo, si fuese M = 12  10  39  14  26  18  11  24 
// Debería quedar como	 M = 12  10  49  10  40  10  29  24 
//-------------------------------------------------------------------------------------------
// para usar índices desde 0 debes configurar Pseint de la siguiente forma...
// Clic Configurar, Clic en opciones del Lenguaje, Clic en ersonalizar (abajo), Clic en
// casilla Utilizar índices en arreglo y cadenas en base 0, Clic Aceptar, Clic Aceptar
//-------------------------------------------------------------------------------------------

Algoritmo contarCeros
	// Definir arreglo M, llenarlo con valores al azar y mostrarlo
	N <- Aleatorio(5, 15)
	Dimension M[N]
	
	Escribir "M[]    =" Sin Saltar
	
	Para i desde 0 hasta N-1
		M[i] <- Aleatorio(10, 40)
		Escribir " " M[i] Sin Saltar
	FinPara
	
	Escribir ""
	
	ContadorCeros <- 0
	
	Si M[0] = 10 entonces
		ContadorCeros <- 1
	FinSi
	
	Para i desde 1 hasta N-2
		Si M[i] < M[i-1] entonces
			M[i+1] <- M[i+1] + M[i]
			M[i] <- 10
			ContadorCeros <- ContadorCeros + 1
		FinSi
	FinPara
	
	Escribir "M[]    =" Sin Saltar
	
	Para i desde 0 hasta N-1
		Escribir " " M[i] Sin Saltar
	FinPara
	
	Escribir ""
	Escribir "Ceros encontrados =", ContadorCeros
	
FinAlgoritmo
