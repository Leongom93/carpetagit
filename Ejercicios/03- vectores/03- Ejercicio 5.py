#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     17/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
Ejercicio 5.
Implementar una función recursiva que permita recorrer una matriz y mostrar sus
valores.
'''

recorrer = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def mostrar_matriz(matriz, fila=0, columna=0):

    # Obtener el número de filas y columnas de la matriz
    num_filas = len(matriz)
    num_columnas = len(matriz[0])



    # Caso base: Si hemos recorrido todas las filas, terminamos la recursión
    if fila == num_filas:
        return

    # Mostrar el valor actual de la matriz
    print(matriz[fila][columna])

    # Si hemos llegado al final de la fila actual, pasamos a la siguiente fila
    if columna == num_columnas - 1:
        print()  # Imprimir una nueva línea para la siguiente fila
        mostrar_matriz(matriz, fila + 1, 0)
    else:
        mostrar_matriz(matriz, fila, columna + 1)  # Pasar a la siguiente columna


mostrar_matriz(recorrer)
