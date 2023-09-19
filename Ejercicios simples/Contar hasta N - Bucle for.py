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
Contar hasta N: Escribe un programa que le pida al usuario un número N
y luego cuente desde 1 hasta N utilizando un bucle for. Imprime cada
número en la pantalla.
'''

numero = int(input("ingrese un numero: "))
contador= 0

for i in range(1, numero+1):
    print(i)
