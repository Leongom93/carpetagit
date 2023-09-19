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
Ejercicio 3.
Realizar una función que se llame relacion() que a partir de dos nros realicce
lo siguiente:
Si el primer nro es mayor que el segundo, devuelva 1
Si el primer nro es menor que el segundo, devuelva -1
Si ambos nros son iguales, devuelva 0
'''

def relacion(nro1, nro2):
    if nro1 < nro2:
        return 1
    elif nro1 > nro2 :
        return 2
    else :
        return 0




nro1 = input("Ingrese el numero 1: ")
nro2 = input("Ingrese el numero 2: ")

print(f"El numero devuelto es: {relacion(nro1, nro2)}")


