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
Ejercicio 2.
Realizar una función que se llame area_circulo() que devuelva el área del
círculo a partir de su radio.
Utilizar el valor 3.14159 como pi
'''


def area_circulo(PI, radio):
    area= PI * radio ** 2

    return area

PI=3.14159
radio = int(input("Ingrese el radio del circulo: "))

print("El area del circulo es de: " + str(area_circulo(PI, radio)))