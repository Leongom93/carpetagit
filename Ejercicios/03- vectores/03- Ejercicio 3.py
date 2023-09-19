#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      user
#
# Created:     16/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
Ejercicio 3.
Implementar una función que calcule la suma de todos los números enteros
comprendidos entre cero y un número entero positivo dado.
'''

def funcion():
    numero = int(input("ingrese un numero: "))
    x= 0
    suma= 0

    while x != numero:
        suma= suma + x
        x += 1



    suma = suma + x
    print(f"La suma de todos los enteros entre 0 a {numero} es: {suma} ")

funcion()