#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      inap
#
# Created:     05/09/2023
# Copyright:   (c) inap 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""

Ejercicio 8.
Definir una lista de números
Encontrar el valor máximo de la lista
Imprimir el valor
- No utilizar la funcion min
"""

lista = [10, 20, 30, 60, 5, 22, 43,101, 90]


for i in range(0, len(lista)-1) :

    if (i == 0 or maximo < lista[i]):
        maximo = lista[i]
        print(f"el maximo es : {maximo}")


print(maximo)
