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
Ejercicio 5.
Realizar una función que se llame recortar() que reciba 3 parámetros.
1º param => nro a recortar
2º param => es el límite inferior
3º param => es el límite superior
La función debe cumplir lo siguiente:
Devolver el límite inferior si el nro es menor
Devolver el límite superior si el nro es mayor
Devolver el nro si no supera los límites
'''

def recortar(nro, inferior, superior):
    if nro < inferior:
        return inferior
    elif nro > superior:
        return superior
    else:
        return nro


nro = int(input("Ingrese el numero: "))
inferior = int(input("Ingrese el limite inferior: "))
superior = int(input("Ingrese el limite superior: "))

print("El numero es: " + str(recortar(nro, inferior, superior)))