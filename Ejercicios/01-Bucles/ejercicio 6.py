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
Ejercicio 6.
Definir una lista de números
Mostrar por pantalla el valor promedio de la lista.
No utilizar funciones sum ni len
'''

lista = [10, 20, 30 , 40 ]
suma = 0
contador = 0

for item in lista:
    suma += item
    contador += 1
    print(f"item: {item}")

promedio = suma / contador

print("La cantidad de elementos es: " + str(contador))
print("El promedio es: " + str(promedio))
