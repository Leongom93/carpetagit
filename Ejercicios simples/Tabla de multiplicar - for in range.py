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
Tabla de multiplicar: Pide al usuario que ingrese un número y muestra su
tabla de multiplicar del 1 al 10 utilizando un bucle for.
'''

numero = int(input("ingrese un numero: "))
tabla= 0

for i in range (0, 10+1):
    tabla = numero * i
    print(f'{numero} x {i} = {tabla} ')

