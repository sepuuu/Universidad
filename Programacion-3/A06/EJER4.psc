// Seudoc�digo de una funci�n recursiva que muestre uno a uno los valores PARES mayores a
// cero que existen  en un arreglo M de N enteros, pero que los muestre desde  el primero
// al �ltimo, y que adem�s devuelva la suma de todos esos pares
//
// Por ejemplo, si el contenido del arreglo fuese:  10 15 23 14 16 11 24 33 40 19 
// Deber�a mostrar: 10 14 16 24 40  y devolver 104 (que es la suma de esos pares)
//-------------------------------------------------------------------------------------------
// SEUDOCODIGO
// ###########
//
// Pares(M,x)                                // recibe arreglo e �ndice a �ltimo elemento
//    Si x < 0 entonces                      // si no hay elemento
//       Devuelve 0                          // devuelve 0
//    Sino                                   // de lo contrario
//       Valor = 0                           // inicia variable
//       Si M(x) es par entonces             // Si elemento actual es par cambia la
//          Valor = M(x)                     // variable para que contenga ese par
//       Fin Si	                             //
//       sumaPares  = Valor + Pares(M,x-1)	 // recursivamente obtiene suma de pares
//       Si Valor > 0 entonces               // si el valor actual era par entonces
//          Escribir Valor                   // muestra ese valor (despu�s de regresar
//       FinSi                               // desde el llamado a la funci�n)
//       Devuelve sumaPares                  // devuelve la suma actual
//    FinSi		
// FinPares
//-------------------------------------------------------------------------------------------
// para usar �ndices desde 0 debes configurar Pseint de la siguiente forma...
// Clic Configurar, Clic en opciones del Lenguaje, Clic en ersonalizar (abajo), Clic en
// casilla Utilizar �ndices en arreglo y cadenas en base 0, Clic Aceptar, Clic Aceptar
//-------------------------------------------------------------------------------------------

Algoritmo EJER4
	// define arreglo, lo llena con valores al azar y lo muestra
	N = 10
	Dimension M(N)
	Escribir "M[] =" Sin Saltar
	Para i desde 0 hasta N-1
		M[i] = Aleatorio(10,90)
		Escribir " " M[i] Sin Saltar
	FinPara
	Escribir ""
	
	Escribir "Pares desde primero recursivamente"
	suma = Pares(M, 9)
	Escribir ""
	Escribir "Suma pares = " suma
FinAlgoritmo

// FUNCION RECURSIVA
Funcion res <- Pares(M,x)                     // Se usa una variable para respuesta funci�n
	Si x < 0 entonces	                      // Si �ndice x apunta fuera del arreglo
		res = 0                               // devuelve 0 (no hay elemento)
	Sino                                      // En caso contrario
		Si M[x]%2 = 0 entonces               // Si actual es par
			sumaPares = M[x] + Pares(M, x-1)  // lo agrega a valor funci�n aplicada a dem�s
			Escribir M[x] " " sin saltar     // y muestra en pantalla al regresar de funci�n
		SiNo                                  // Pero si actual no es par
			sumaPares =  Pares(M, x-1)        // solo considera valor funci�n aplicada a dem�s
		FinSi                                 //
		res = sumaPares                       // Terminado todo el proceso recursivo
	FinSi                                     // Devuelve al valor obtenido 
FinFuncion
