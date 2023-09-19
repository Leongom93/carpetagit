#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     19/09/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
Factorial de un número: Pide al usuario que ingrese un número n y calcula su
factorial (el producto de todos los enteros positivos desde 1 hasta n)
utilizando un bucle for.
'''

numero = int(input("ingrese un numero: "))
factorial= 1

for i in range (1, numero+1):
    factorial  *= i
    print(f' {factorial} ')



