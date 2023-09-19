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
Suma de números pares: Escribe un programa que calcule la suma de todos
los números pares desde 1 hasta 100 utilizando un bucle for.
'''

inicio = int(input( "ingrese el inicio: "))
final = int(input("Ingrese el final: "))

suma = 0

for i in range(inicio , final+1):
    if  i % 2 == 0:
        print(f'Numero par: {i}')
        suma += i

print(f' la suma de todos los numeros pares es: {suma}')

