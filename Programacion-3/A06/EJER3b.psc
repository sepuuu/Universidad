// Se tiene un arreglo  M de N  enteros. Escribe un seudocódigo  para recorrerlo y cada vez
// que se llegue a un impar que tenga un vecino par le sume 1. Por ejemplo si el arreglo es
//
// M = 14 23 16 21 45 14 15 31 44   quedará como...
// M = 14 24 16 22 46 14 16 32 44 
//
// CODIFICA TU RESPUESTA MAS ABAJO (agregando instrucciones para crear los arreglos, para
// mostrarlos y también para mostrar el o los resultados logrados con tu seudocódigo)
//-------------------------------------------------------------------------------------------
Algoritmo sumarImpares
    // Definir arreglo M, llenarlo con valores al azar y mostrarlo
    N <- Aleatorio(5, 15)
    Dimension M[N]
    
    Escribir "M[]    =" Sin Saltar
    
    Para i desde 0 hasta N-1
        M[i] <- Aleatorio(10, 40)
        Escribir " " M[i] Sin Saltar
    FinPara
    
    Escribir ""
    
    Para i desde 1 hasta N-2
        Si M[i] % 2 = 1 y M[i-1] % 2 = 0 o M[i+1] % 2 = 0 entonces
            M[i] <- M[i] + 1
        FinSi
    FinPara
    
    Escribir "M[]    =" Sin Saltar
    
    Para i desde 0 hasta N-1
        Escribir " " M[i] Sin Saltar
    FinPara
    
FinAlgoritmo


