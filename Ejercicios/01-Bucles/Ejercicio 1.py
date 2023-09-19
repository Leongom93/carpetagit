#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     09/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
Ejercicio 1.
Pedir al usuario que ingrese un nro impar
Mientras que el usuario no ingrese un nro impar se volverá a
pedir que ingrese un nro impar
Deberá indicar por pantalla si es impar
'''

numero = int(input("ingrese un numero impar: "))


while (numero % 2 == 0):
    print("el numero ingresado es incorrecto")
    numero = int(input("ingrese un numero impar: "))

print(numero)
