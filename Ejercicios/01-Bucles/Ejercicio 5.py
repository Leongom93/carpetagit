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
Ejercicio 5.
Definir una lista de números
Sumar todos sus valores de esa lista
Al finalizar mostrar por pantalla el total de la suma.
No utilizar función sum
'''


nros = [1, 3 , 4 , 2]
suma = 0

for item in nros:
    suma += item

print(suma)

