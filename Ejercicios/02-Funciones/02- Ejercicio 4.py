#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     10/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
Ejercicio 4.
Realizar una función que se llame intermedio() que a partir de dos nros
devuelva el punto intermedio. Ej. El punto intermedio entre 10 y 24 = 17; entre
12 y 50 = 31.
'''

def intermedio(nro1, nro2):
    promedio = (nro1 + nro2) /2
    return promedio

nro1 = int(input("Ingrese el numero 1: "))
nro2 = int(input("Ingrese el numero 2: "))

print("El numero intermedio es: " + str(intermedio(nro1, nro2)))