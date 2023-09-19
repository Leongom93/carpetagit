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
Ejercicio 7.
Definir una lista de números
Encontrar el valor minimo de la lista
Imprimir el valor
No utilizar min
'''
lista = [100, 20, 30,14, 60,12, 5, 22, 43,1, 90]


for i in range(0, len(lista)-1) :

    if (i == 0 or minimo > lista[i]):
        minimo = lista[i]


        print(f"el minimo es : {minimo}")

        print(f"--------------")

print(f"el minimo es: {minimo}")
